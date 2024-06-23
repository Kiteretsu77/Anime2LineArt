# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import torch
from torch.nn import functional as F


root_path = os.path.abspath('.')
sys.path.append(root_path)


def np2tensor(np_frame):
    return torch.from_numpy(np.transpose(np_frame, (2, 0, 1))).unsqueeze(0).cuda().float()/255

def tensor2np(tensor):
    # tensor should be batch size1 and cannot be grayscale input
    return (np.transpose(tensor.detach().squeeze(0).cpu().numpy(), (1, 2, 0))) * 255

def filter2D(img, kernel):
    """PyTorch version of cv2.filter2D

    Args:
        img (Tensor): (b, c, h, w)
        kernel (Tensor): (b, k, k)
    """
    k = kernel.size(-1)
    b, c, h, w = img.size()
    if k % 2 == 1:
        img = F.pad(img, (k // 2, k // 2, k // 2, k // 2), mode='reflect')
    else:
        raise ValueError('Wrong kernel size')

    ph, pw = img.size()[-2:]

    if kernel.size(0) == 1:
        # apply the same kernel to all batch images
        img = img.view(b * c, 1, ph, pw)
        kernel = kernel.view(1, 1, k, k)
        return F.conv2d(img, kernel, padding=0).view(b, c, h, w)
    else:
        img = img.view(1, b * c, ph, pw)
        kernel = kernel.view(b, 1, k, k).repeat(1, c, 1, 1).view(b * c, 1, k, k)
        return F.conv2d(img, kernel, groups=b * c).view(b, c, h, w)
    