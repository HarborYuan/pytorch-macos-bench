from ..builder import CLASSIFIERS
from .image import ImageClassifier


@CLASSIFIERS.register_module()
class MPSImageClassifier(ImageClassifier):

    def forward_train(self, img, gt_label, **kwargs):
        img = img.to("mps")
        gt_label = gt_label.to("mps")
        return super().forward_train(img, gt_label, **kwargs)

    def simple_test(self, img, **kwargs):
        img = img.to("mps")
        return super().simple_test(img, **kwargs)
