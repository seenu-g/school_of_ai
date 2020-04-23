Learn about COCO classes:
http://cocodataset.org/#home

Download yolov3.weights from https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/

YOLO accepts three sizes:

320×320 it’s small so less accuracy but better speed
609×609 it’s bigger so high accuracy and slow speed
416×416 it’s in the middle and you get a bit of both.

Project Files
coco.names - contains classed in COCO dataset
yolo_object_detection.py - python file
yolov3.weights - trained model, the core of the algorithm to detect the objects.
room_ser.jpb - sample image
IMG_2144.jpg - new image
annotated_IMG_2144.jpg - annotated image