import mxnet as mx
import numpy as np
import cv2

import os
path = os.getcwd()+"/data"+"/cifar-10-batches-py"
print(path)
        
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def extractImagesAndLabels(path, filename):
    dict = unpickle(path + "/" + filename)
    images = dict[b'data']
    images = np.reshape(images, (10000, 3, 32, 32))
    labels = dict[b'labels']
    imagearray = mx.nd.array(images)
    labelarray = mx.nd.array(labels)
    return imagearray, labelarray

def extractCategories(path, filename):
    dict = unpickle(path + "/" + filename)
    return dict[b'label_names']

def saveCifarImage(array, path, file):
    try :
        # array is 3x32x32. cv2 needs 32x32x3
        array = array.asnumpy().transpose(1,2,0)
        # array is RGB. cv2 needs BGR
        array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        # save to PNG file # no wroking
        if not cv2.imwrite(path+file+".png", array):
           print("Could not write image ",path+file+".png")
        #else :
           print("wrote",path+file+".png")
    except :
        print("error in  saveCifarImage")


imgarray, lblarray = extractImagesAndLabels(path, "/data_batch_1")
print(imgarray.shape,imgarray.size)
print(lblarray.shape,lblarray.size)

categories = extractCategories(path, "/batches.meta")

save_path = os.getcwd()+ '/data_batch_1_images/'
cats = []
for i in range(0,10):
    saveCifarImage(imgarray[i], save_path, "image"+(str)(i))
    category = lblarray[i].asnumpy()
    category = (int)(category[0])
    cats.append(categories[category])
print(cats)
