There can be one annotation for every object in image. Each annotation seems to have it own segmentation and BBBox

id - id of segmentation and BBox marked objects for which we are specifying the annotations , within image
image_id - corresponds to the imageid that we have in the image section
segmentation - contains x and y that correspond for vertices of polygon around every object for segmentation masks.
bbox- Bounding box - x and y co-ordinate of the top left and the height and width of the rectangle
area - area of the bounding box. It is a pixel value
iscrowd - can be 0 or 1. It is zero with dog images where there is one annotation. When there is more annotation, the value seems to set to 1.
