ReadMe.txt
Project Summary
Dataset  : CIFAR10
Accuracy : 89%
Model    : RESNet
Features : GradCAM, Albumentations

Project Source Files
Final.ipynb - Google Collab notebook
Albumentationtransform.py  -  functions related to data trandform
gradcam.py  -   functions related to gradCAM
model.py    -  RESNEt model
train_test.py - contains functions to train and test
evaluate.py  -  functions to evaluate accuracy, classwise accuracy, misclassified images
load_data.py  -  functions to load data from CIFAR
show_images.py -  functions to display image in Google Collab

Instructions to run 
1.template folder contains python files related to assignment (copy to folder where Final.ipynb resides)
2. image folder contains general image used to pass as input for GradCAM. (copy image folder to folder where Final.ipynb resides )
    bird.jpeg car.jpeg cat.jpeg deer.jpg dog.jpeg frog.jpg horse.jpg plane.jpg ship.jpeg truck.jpeg
