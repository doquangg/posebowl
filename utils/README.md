# Utils

### create_posebowl_data_labels.py and posebowl_data_split.py

Begin by navigating to the directory which will store both your training data
and their corresponding labels. Create two folders, labeled ```images``` and
```labels``` if you have not already done so. 

In the ```images``` directory, create three folders: ```val```, ```test```, and
```train```. Move all available posebowl training images into ```train```.

Create those same three folders in the ```labels``` directory. Additionally,
move the ```train_labels.csv``` file to the same level as the ```val```, 
```test```, and ```train``` folders. 

Run ```create_posebowl_data_labels.py``` first, after changing the paths to the
```TRAIN_LABELS_PATH``` and ```TRAIN_CSV``` variables to ensure the script works
correctly. This script will create individual data labels for the labels within 
 ```train_labels.csv``` in the form of ```.txt``` files. 

Then, run ```posebowl_data_split.py```, making sure to update ```IMAGES_PATH```
and ```LABELS_PATH```, to split the data and labels into validation, training, 
and testing data. 

If you have already previously ran both of these scripts, and wish to generate
new testing and validation data, please delete the both your images and label
directory and repeat the same process as outlined above.