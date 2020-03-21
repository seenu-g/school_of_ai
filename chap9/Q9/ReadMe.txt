ReadMe.txt
Project Summary
Dataset  : CIFAR10
Accuracy : 85%
Features : Dropout, Albumentation
Model    : Parameters- 298,432(Refer Q9 DNN architecture mentioned below)

Project Source Files
Untitle0.ipynb - Google Collab notebook // model is commented completely
Albumentationtransform.py  -  functions related to data trandform
gradcam.py  -   functions related to gradCAM
QuizDNN.py    -  functions that represent Q9 DNN architecture mentioned below
train_test.py - contains functions to train and test
evaluate.py  -  functions to evaluate accuracy, classwise accuracy, misclassified images
train_test_loader.py  -  functions to load data from CIFAR
show_images.py -  functions to display image in Google Collab

Instructions to run 
1.template folder contains python files related to assignment (copy to folder where Final.ipynb resides)
2. image folder contains general image used to pass as input for GradCAM. (copy image folder to folder where Final.ipynb resides )
    bird.jpeg car.jpeg cat.jpeg deer.jpg dog.jpeg frog.jpg horse.jpg plane.jpg ship.jpeg truck.jpeg

Q9 DNN architecture
x1 = Input
x2 = Conv(x1)
x3 = Conv(x1 + x2)
x4 = MaxPooling(x1 + x2 + x3)
x5 = Conv(x4)
x6 = Conv(x4 + x5)
x7 = Conv(x4 + x5 + x6)
x8 = MaxPooling(x5 + x6 + x7)
x9 = Conv(x8)
x10 = Conv (x8 + x9)
x11 = Conv (x8 + x9 + x10)
x12 = GAP(x11)
x13 = FC(x12)