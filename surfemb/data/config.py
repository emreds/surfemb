from collections import defaultdict


class DatasetConfig:
    model_folder = 'models'
    train_folder = 'train'
    test_folder = 'test'
    img_folder = 'rgb'
    depth_folder = 'depth'
    img_ext = 'png'
    depth_ext = 'png'


config = defaultdict(lambda *_: DatasetConfig())

config['tless'] = tless = DatasetConfig()
tless.model_folder = 'models_cad'
tless.test_folder = 'test_primesense'
tless.train_folder = 'train_primesense'

config['tless2'] = tless2 = DatasetConfig()
tless2.model_folder = 'models_cad'
tless2.test_folder = 'test'
tless2.train_folder = 'train_pbr'

config['hb'] = hb = DatasetConfig()
hb.test_folder = 'test_primesense'

config['itodd'] = itodd = DatasetConfig()
itodd.depth_ext = 'tif'
itodd.img_folder = 'gray'
itodd.img_ext = 'tif'
