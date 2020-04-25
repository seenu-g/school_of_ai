COCO_Annotation
Please find steps to setup execute at 
https://github.com/seenu-g/school_of_ai/blob/master/chap13/COCO_annotation/ReadMe.txt
This can be executed in local laptop itself

YoloV3_Annotation_Tool
download 500 images of your unique object. Annotate the images using the Annotation tool.
Clone  repo: https://github.com/miki998/YoloV3_Annotation_Tool
Follow steps provided in ReadMe.txt present in
 https://github.com/seenu-g/school_of_ai/blob/master/chap13/YoloV3_Annotation_Tool/ReadMe.txt
Here we annotate woody character and this can be executed in laptop itself.

YoloV3 Setup
In Google collab, download repository in to git clone https://github.com/theschoolofai/YoloV3 
1. Create "weights" folder in the root (YoloV3) folder
2. Get yolov3-spp-ultralytics.pt from  https://drive.google.com/open?id=1LezFG5g3BCW6iYaV89B2i64cqEUZD7e0
   and place in "weights" folder
3. Bring images annotation files and related files to these folders
   1. Copy image files to data/customdata/images
   2. Copy label txt files to data/customdata/labels
   3. custom.names - contain string "woody"
   4. custom.shapes - contains shapes of custom
   5. custom. txt  - contain relative path to all images
   6. test.shapes - custom shapes of test images
   7. test.txt - contains relative path to all test images
4. Download 2 videos with woody character from below URLS
Toy story Woody & Buzz https://www.youtube.com/watch?v=YMgoKhFEN6s , 
Hawaiian Vacation - Trailer https://www.youtube.com/watch?v=5zQ3-ZzHndo 
Place videos under YoloV3/data/customdata

5. Run python "train.py" --data data/smalcoco/smalcoco.data --batch 10 --cache --epochs 5 --nosave

6. !python train.py --data data/customdata/custom.data --batch 10 --cache --cfg cfg/yolov3-custom.cfg --epochs 200 --nosave

7. python3 detect.py --weights weights/last.pt  --source "/content/gdrive/My Drive/school_of_ai/chap13/YoloV3/data/customdata/Toy story Woody & Buzz.mp4" --output "/content/gdrive/My Drive/school_of_ai/chap13/YoloV3/output1"
# The output video is copied under YoloV3/output1
Annotated video uploaded to https://www.youtube.com/watch?v=WmX9KPxvpFE

8. !python3 detect.py --weights weights/last.pt  --source "/content/gdrive/My Drive/school_of_ai/chap13/YoloV3/data/customdata/Hawaiian Vacation - Trailer.mp4" --output "/content/gdrive/My Drive/school_of_ai/chap13/YoloV3/output2"
# The output video is copied under YoloV3/output2
Annotated video uploaded to https://www.youtube.com/watch?v=smOn1VNoP6Q
