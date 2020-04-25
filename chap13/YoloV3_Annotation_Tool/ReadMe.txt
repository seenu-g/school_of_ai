Download 500 images of your unique object. Annotate the images using the Annotation tool.

Clone  repo: https://github.com/miki998/YoloV3_Annotation_Tool

Step 1: 
Files present in project[ Changed and Clone]

process.py - Updated. creates txt files in yolov3 format. 
classes.txt - Updated. class of objects that you want to detect using yolov3. 

resize.py - Clone
standardize.py - Clone 
verify.py - Clone
main.py - Clone

Step 2 : Place image in folder. 
images - contains input images that are annotated. Not checked-in here. 
                          Checked-in as similar structure in main project

Step 3 : Annotate images
  Run python3 main.py
  Perform annotation in UI for 125 images and generate labels

Strpe 4: files created by program
1. Labels - contains yolk format self of the images. Checked-in here.
2. train.txt
3. custom_shapes.txt