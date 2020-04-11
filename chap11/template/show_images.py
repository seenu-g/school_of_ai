import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision


# functions to show an image
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))

def show_images(dataset, classes):
    dataiter = iter(dataset)
    images, labels = dataiter.next()
    img_list = range(5, 10)
    #print('shape:', images.shape)
    '''for i in range(10):
        index = [j for j in range(len(labels)) if labels[j] == i]
        imshow(torchvision.utils.make_grid(images[index[0:5]],nrow=5,padding=2,scale_each=True),classes[i])'''
        
    img_list = range(5, 10)
    imshow(torchvision.utils.make_grid(images[img_list]))