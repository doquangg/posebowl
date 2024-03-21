import os
import glob
from random import shuffle


IMAGES_PATH = os.path.join('..', '..', '..', 'posebowl_data', 'images')
LABELS_PATH = os.path.join('..', '..', '..', 'posebowl_data', 'labels')

# Data Split
NUM_IMAGES  = 25801
TRAIN_SPLIT = 0.85
VAL_SPLIT   = 0.10
TEST_SPILT  = 0.05

images_paths = glob.glob(os.path.join(IMAGES_PATH, 'train', '*.png'))
labels_paths = glob.glob(os.path.join(LABELS_PATH, 'train', '*.txt'))

index_shuffle = list(range(len(images_paths)))
shuffle(index_shuffle)

for idx in index_shuffle:

    # Train data
    if idx < int(NUM_IMAGES*TRAIN_SPLIT):
        pass

    # Val data
    elif int(NUM_IMAGES*TRAIN_SPLIT) <= idx and idx < int(NUM_IMAGES*(TRAIN_SPLIT+VAL_SPLIT)):

        new_image_path = os.path.join(IMAGES_PATH, 'val', images_paths[idx].split('\\')[-1])
        new_label_path = os.path.join(LABELS_PATH, 'val', labels_paths[idx].split('\\')[-1])
        os.rename(images_paths[idx], new_image_path)
        os.rename(labels_paths[idx], new_label_path)

    # Test data
    else:

        new_image_path = os.path.join(IMAGES_PATH, 'test', images_paths[idx].split('\\')[-1])
        new_label_path = os.path.join(LABELS_PATH, 'test', labels_paths[idx].split('\\')[-1])
        os.rename(images_paths[idx], new_image_path)
        os.rename(labels_paths[idx], new_label_path)
