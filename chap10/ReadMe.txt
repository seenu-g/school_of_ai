Folder contains submission for chapter 10 assignment, present in Final.ipynb

Project Summary
Dataset  : CIFAR10
Accuracy : 91%
Model    : RESNet
Features : GradCAM, Albumentations, LRFinder, ReduceLROnPlateau

References
https://pytorch.org/docs/stable/optim.html#torch.optim.lr_scheduler.ReduceLROnPlateau
https://github.com/davidtvs/pytorch-lr-finder

Project Source Files
Final.ipynb - Google Collab notebook
Albumentationtransform.py  -  functions related to data trandform. No change from chap9
gradcam.py  -   functions related to gradCAM, Added function GradCAMView
model.py    -  RESNEt model. No change from chap9
train_test.py - contains functions to train and test. Updated to add return statement in train function
evaluate.py  -  functions to evaluate accuracy, classwise accuracy, misclassified images
load_data.py  -  functions to load data from CIFAR.  No change from chap9
show_images.py -  functions to display image in Google Collab.  No change from chap9
transform.py  -  functions related to albumentations. No change from chap9
plot.py        - functions to plot graphs
plot.py        - functions to plot graphs
lr_finder.py   - function to faciliate finding best learning rate
