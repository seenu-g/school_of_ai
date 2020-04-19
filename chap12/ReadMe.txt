
Submission A for chapter 12 assignment, present in https://github.com/seenu-g/school_of_ai/blob/master/chap12/Trial3.ipynb
submission A for chapter 12 assignment, present in https://github.com/seenu-g/school_of_ai/blob/master/chap12/annotation%20/num_of_clusters.ipynb

Project Summary
Dataset : Tiny-ImageNet. 
Download URL : http://cs231n.stanford.edu/tiny-imagenet-200.zip
Model : updated ResNet model present in chap12ResNet.py
Test Accuracy : 55

Test set: Average loss: 0.0075, Accuracy: 18890/33000 (57.24%)
Accuracy of the network on the 10000 test images: 55 %

New Files Added
DatasetFromSubset.py - Load dataset specific to test and val
TinyImageNet.py - Custom Dataset that inherits from DataSet present in torch.utils.data
download_extract.py - download from URL, Extract from Zip file
TinyImageNetDataset.py - Not used, code is used in Google Colab Notebook
chap12ResNet.py - updated ResNet model using in this architecture

File used (copied) from https://github.com/seenu-g/school_of_ai/tree/master/chap11/template without change
Albumentationtransform.py  -  functions related to data transform. 
evaluate.py  -  functions to evaluate accuracy. 
gradcam.py  -   functions related to gradCAM, Added function GradCAMView. Not used in Chap12
lr_finder.py   - function to faciliate finding best learning rate. Not used in Chap12
model.py    -  RESNEt model.  Not used in Chap 12
show_images.py -  functions to display image in Google Collab. Not used in Chap 12 
transform.py  -  functions related to albumentations. 
plot.py        - functions to plot graphs. Not used in Chap 12
