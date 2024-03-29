# Imports
import os
import glob
from numpy import random
################################################################################

# Set paths to image and label directories
IMAGES_PATH = '../../posebowl_files/images'
LABELS_PATH = '../../posebowl_files/labels'

# Sanity Check
if not (os.path.isdir(IMAGES_PATH) and os.path.isdir(LABELS_PATH)):
    print("One or more paths is not valid.")

# Data Splits
NUM_IMAGES  = 25801 # This amount corresponds to the number of images from all
                    # the provided .tar files; if the length of images_paths is
                    # not equal to this, you may need to reset your images
                    # folder
                    
# Please, for the love of god, make sure these add up to 1.
TRAIN_SPLIT = 0.85
VAL_SPLIT   = 0.10
TEST_SPILT  = 0.05

# Useful constants
VAL_UPPER_LIM  = 1 - TRAIN_SPLIT
VAL_LOWER_LIM  = 1 - TRAIN_SPLIT - VAL_SPLIT

# Set paths to files
images_paths = glob.glob(os.path.join(IMAGES_PATH, 'train', '*.png'))
labels_paths = glob.glob(os.path.join(LABELS_PATH, 'train', '*.txt'))

# Generate NUM_IMAGES random numbers to be used in the sorting of labels and
# images; rand produces numbers strictly between 0 and 1
random_list = random.rand(NUM_IMAGES)

###############################################################################
# The idea for assignment is kinda similar to a hashmap, but I didn't implement
# this because I'm lazy. Each index within random_list corresponds to its 
# respective file within images_paths and labels_paths, such that assigning the
# ith label and image is done by bounds-checking the random number generated
# at the ith index in random_list.
################################################################################

# Iterate through random list
for entry in range(len(random_list)):
    
    # Set the image and label being targeted
    image_file = os.path.basename(images_paths[entry])
    label_file = os.path.basename(labels_paths[entry])
    
    # Set the random number of the entry-th image and label
    num = random_list[entry]
    
    # If the relation: 
    # 1 - TRAIN_SPLIT - VAL_SPLIT < num <= 1 - TRAIN_SPLIT
    # is satisfied, keep the image and its corresponding label in the val
    # folders; that is, all images and labels corresponding to nums
    # falling within [1 - TRAIN_SPLIT, 1 - TRAIN_SPLIT - VAL_SPLIT) will be 
    # moved to the val folder
    if num <= VAL_UPPER_LIM and num > VAL_LOWER_LIM:
        
        # Set new image and label paths
        new_image_path = os.path.join(IMAGES_PATH, 'val', image_file)
        new_label_path = os.path.join(LABELS_PATH, 'val', label_file)
        
        # Move image and label
        os.rename(images_paths[entry], new_image_path)
        os.rename(labels_paths[entry], new_label_path)
        
        continue
        # move to val
        
    # All others number then must fall between [1 - TRAIN_SPLIT - VAL_SPLIT, 0]
    # and will be moved to the test folder. 
    elif num <= VAL_LOWER_LIM and num >= 0:
        
        # Set new image and label paths
        new_image_path = os.path.join(IMAGES_PATH, 'test', image_file)
        new_label_path = os.path.join(LABELS_PATH, 'test', label_file)
        
        # Move image and label
        os.rename(images_paths[entry], new_image_path)
        os.rename(labels_paths[entry], new_label_path)
        
        continue
        
    # If neither of these conditions are fulfilled, that means num falls into
    # [1, 1 - TRAIN_SPLIT], which means the data will remain in the training
    # folders.