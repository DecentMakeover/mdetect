from .voc import VOCDataset
from .registry import DATASETS


@DATASETS.register_module
class IDD(VOCDataset):
    CLASSES =( ' person', 'rider',' car' ,'truck','bus','motorcycle','bicycle','autorickshaw','animal','traffic light','traffic sign', 'vehicle fallback','caravan', 'trailer', 'train')

    