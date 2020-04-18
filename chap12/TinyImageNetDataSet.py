from torch.utils.data import Dataset, random_split
from DatasetFromSubset import DatasetFromSubset
from TinyImageNet import TinyImageNet
from download_extract import download_images
def get_classes(download_folder):
    classes = []
    wnids = open(os.path.join(download_folder,"wnids.txt"), "r")
    for line in wnids:
        classes.append(line.strip())
    return classes
  
def TinyImageNetDataSet(train_split = 70,test_transforms = None,train_transforms = None):

  down_url  = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
  download_images(down_url)
  classes = get_classes(url = "tiny-imagenet-200/wnids.txt")
  dataset = TinyImageNet(classes,url="tiny-imagenet-200")
  train_len = len(dataset)*train_split//100
  test_len = len(dataset) - train_len 
  train_set, val_set = random_split(dataset, [train_len, test_len])
  train_dataset = DatasetFromSubset(train_set, transform=train_transforms)
  test_dataset = DatasetFromSubset(val_set, transform=test_transforms)

  return train_dataset, test_dataset,classes


    
