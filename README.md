# Anime2LineArt
Anime images to hand-drawn lines
Using non-neural methods (current version is transplanted from the [APISR](https://github.com/Kiteretsu77/APISR))



## <a name="installation"></a> Installation 🔧

```shell
git clone git@github.com:Kiteretsu77/Anime2LineArt.git
cd Anime2LineArt

# Create conda env
conda create -n a2la python=3.10
conda activate a2la

# Install Pytorch and other packages needed
pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```


## <a name="regular_inference"></a> Execute ⚡
```shell
python anime2line.py -i sample_outputs -o tmp --outlier_threshold 16 --num_workers 1
```
Change the number of workers to the volume desired. \
Set **outlier_threshold** to 16-32 is decent. \
Don't input images which the resolution is too big. It will be very time consuming since there is some hard-code that will iterate all the pixels in the images. 