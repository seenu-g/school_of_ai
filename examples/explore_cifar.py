import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

def load():
	 # Transformation for Training
    train_transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
	# Transformation for Test
    test_transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    use_cuda = torch.cuda.is_available()

    dataloaderargs = dict(shuffle=True, batch_size=128, num_workers=4, pin_memory=True) if use_cuda else dict(shuffle=True, batch_size=64)
    
    trainset = torchvision.datasets.CIFAR10(root='./data',train=True,download=True,transform=train_transform)
    testset = torchvision.datasets.CIFAR10(root='./data',train=False,download=True,transform=test_transform)
    classes = ('plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    trainloader = torch.utils.data.DataLoader(trainset, **dataloaderargs)
    testloader = torch.utils.data.DataLoader(testset, **dataloaderargs)
    return classes,trainloader,testloader

# functions to show an image
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))

classes,trainloader,testloader = load()
print('number of elements in trainloader',len(trainloader.dataset))
print('number of elements in testloader',len(testloader.dataset))

dataiter = iter(trainloader)
images,labels = dataiter.next()
img_list = range(5, 10)
print('shape:', images.shape)

import os
path = os.getcwd()+"/data"+"/cifar-10-batches-py"
print(path)

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

meta_file= path+ "/" +'batches.meta'
dict1 = unpickle(meta_file)
print (dict1) #{b'num_cases_per_batch': 10000, b'label_names': [b'airplane', b'automobile', b'bird', b'cat', b'deer', b'dog', b'frog', b'horse', b'ship', b'truck'], b'num_vis': 3072}
#print('num_cases_per_batch',dict1[b'num_cases_per_batch']) 
#print('label_names', dict1[b'label_names']) 
#print('num_vis',dict1[b'num_vis']) 

filenames = []
for file in os.listdir(path):
    filename = os.fsdecode(file)
    if filename.endswith( ('.html', '.meta')): 
        temp = filename
    else :
        filenames.append(filename)

filenames_array = []
for filename in filenames :
    temp_file = path + "/" + filename
    dictT = unpickle(temp_file)
    #print ('\n' , dictT[b'filenames'])
    for dict_item in dictT:
       item_list = dictT[dict_item]
       with open(filename + ".txt", "w") as output:
           for item in item_list:
              output.write(str(item)+'\t')
           #print('written',len(item_list), 'of items to', filename + ".txt",'\n' ) 

