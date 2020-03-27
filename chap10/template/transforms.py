from torchvision import transforms
import albumentations as A
import albumentations.pytorch as AP
import random
import numpy as np
class AlbumentationTransforms:
  """
  Helper class to create test and train transforms using Albumentations
  """
  def __init__(self, transforms_list=[]):
    transforms_list.append(AP.ToTensor())

    self.transforms = A.Compose(transforms_list)


  def __call__(self, img):
    img = np.array(img)
    #print(img)
    return self.transforms(image=img)['image']

  def get_transforms(channel_means,channel_stdevs) :
    train_transform = AlbumentationTransforms([
                                          A.Rotate((-30.0, 30.0)),
                                          A.HorizontalFlip(),
                                          A.Normalize(mean=channel_means, std=channel_stdevs),
                                          A.Cutout(num_holes=1, max_h_size=16,max_w_size = 16,p=1) # fillvalue is 0 after normalizing as mean is 0
                                          ])
    test_transform = AlbumentationTransforms([A.Normalize(mean=channel_means, std=channel_stdevs)])
    return train_transform,test_transform