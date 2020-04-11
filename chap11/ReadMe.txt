Folder contains submission for chapter 11 assignment, present in Final.ipynb

Project Summary
Dataset  : CIFAR10
Epochs   : 24
Accuracy : 91%
Model    : Present in Chap11Renet.py
Features : OneCycleLR,GradCAM, Albumentations, 


Project Source Files
Final.ipynb - Google Collab notebook
train_test.py - contains functions to train and test. Added function that performs both train and test, updated train  function to handle scheduler
load_data.py  -  functions to load data from CIFAR.  Pass send batch_size as input
chap11Renet.py - implemented model for chap11 assignment
lr_range_test.py - function to perform lr_range_test that supports implementation of OneCycleLR 

Project Files Copied from earlier assignment(No Change)
Albumentationtransform.py  -  functions related to data trandform. 
evaluate.py  -  functions to evaluate accuracy, classwise accuracy, misclassified images. 
gradcam.py  -   functions related to gradCAM, Added function GradCAMView. 
lr_finder.py   - function to faciliate finding best learning rate. Not used in Chap11
model.py    -  RESNEt model.  Not used in Chap 11
show_images.py -  functions to display image in Google Collab.  
transform.py  -  functions related to albumentations. 
plot.py        - functions to plot graphs

Architecteure Required by aasignment 
Requirement 1
PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
Layer1 -
X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
Add(X, R1)
Layer 2 -
Conv 3x3 [256k]
MaxPooling2D
BN
ReLU
Layer 3 -
X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
Add(X, R2)
MaxPooling with Kernel Size 4
FC Layer 
SoftMax

Requirement 2
Uses One Cycle Policy such that:
Total Epochs = 24
Max at Epoch = 5
LRMIN = FIND
LRMAX = FIND
NO Annihilation



Some Tips
we choose a range of LR values, let's say 0.0001 and a large value, say 1.Now we train our model for several epochs. 
For each epoch change your LR linearly between above low and high value.

And capture the training accuracies for these epochs. Plot curve between LR values and accuracies. 
You will find a curve like mentioned in the session 11 canvas.

Pick the LR where accuracy is high. Now this LR value will act as max_lr and min_lr, you may choose as max_lr/10 or max_lr/8

Now this is your range which you have found out. 
Now create a one cycle schedule for these max and min LR values, oscillating b/w epochs 1,5 and 24 
Train your model fresh for 24 epochs

Also check https://stackoverflow.com/questions/59996859/how-to-use-pytorch-onecyclelr-in-a-training-loop-and-optimizer-scheduler-intera