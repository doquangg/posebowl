import os
import csv

# Set paths to image and label directories
TRAIN_LABELS_PATH = '../../posebowl_files/labels/train'
TRAIN_CSV = '../../posebowl_files/labels/train_labels.csv'

# Set image width and height
WIDTH = 1280
HEIGHT = 1024

# Sanity Check
if not (os.path.isdir(TRAIN_LABELS_PATH) and os.path.isfile(TRAIN_CSV)):
    print("One or more paths is not valid.")

# Create new labels with bounding boxes
with open(TRAIN_CSV, 'r') as train_csv:

    # Open the train_csv
    train_csv_reader = csv.reader(train_csv, delimiter=',')

    for idx, line in enumerate(train_csv_reader):

        label_path = line[0].split('.')[0] + '.txt'

        if idx != 0:

            with open(os.path.join(TRAIN_LABELS_PATH, label_path), 'w') as label_output:    
            
                # line[0] = image_id, line[1] = xmin, line[2] = ymin, line[3] = xmax, line[4] = ymax
                # new_line[0] = image_id, new_line[1] = center_x, new_line[2] = center_y, new_line[3] = width, new_line[4] = height
                for idx in range(1, len(line)):
                    line[idx] = float(line[idx])
                    
                new_line = line
                
                # Transforming bounding boxes
                new_line[1] = ((line[3] - line[1]) / 2 + line[1]) / WIDTH
                new_line[2] = ((line[4] - line[2]) / 2 + line[2]) / HEIGHT
                new_line[3] = (line[3] - line[1]) / WIDTH
                new_line[4] = (line[4] - line[2]) / HEIGHT
    
                label_output.write("0 %f %f %f %f" % (new_line[1], new_line[2], new_line[3], new_line[4]))
    
                label_output.close()
