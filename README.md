# pytorch-macos-bench
This is a fast implementation based on mmcls to test the training speed of PyTorch x Apple Silicon GPU.

## Training
For cpu training of Resnet-50 on Imagenet.
```
PYTHONPATH=. python tools/train.py configs/resnet50/resnet50_b256_in1k.py
```
For gpu training of Resnet-50 on Imagenet.
```
PYTHONPATH=. python tools/train.py configs/resnet50/resnet50_b256_in1k_mps.py --use-mps
```

## Speed
For cpu training, M1 macbook air 2020 needs about 332 days (57s per batch). 

For gpu training, M1 macbook air 2020 needs about 81 days (14s per batch).

## Dependencies

mmcls folder is copy and modified from [mmcls@877ea30](https://github.com/open-mmlab/mmclassification/tree/877ea30).

mmcv installation:
```
python -m pip install opencv-python-headless && MMCV_WITH_OPS=1 pip install git+https://github.com/open-mmlab/mmcv.git@25602c68441d18430d649711a4f3bec576ce327e
```
