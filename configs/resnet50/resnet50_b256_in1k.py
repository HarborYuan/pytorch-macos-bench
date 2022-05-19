_base_ = [
    '../_base_/models/resnet50.py',
    '../_base_/datasets/imagenet_bs32.py',
    '../_base_/schedules/imagenet_bs256.py',
    '../_base_/default_runtime.py'
]

data = dict(
    samples_per_gpu=256,
    train=dict(ann_file='data/imagenet/meta/train.txt', ),
)

log_config = dict(interval=5)
evaluation = dict(interval=1, metric='accuracy', save_best='auto')
checkpoint_config = dict(interval=10, max_keep_ckpts=2)
