# Copyright (c) OpenMMLab. All rights reserved.
from .base import BaseClassifier
from .image import ImageClassifier
from .image_mps import MPSImageClassifier

__all__ = ['BaseClassifier', 'ImageClassifier', 'MPSImageClassifier']
