import os
import zipfile
import requests
from io import StringIO,BytesIO
from tqdm import notebook

def download_images(url):

    if (os.path.isdir("tiny-imagenet-200")):
        print ('Images already downloaded...')
        return
    r = requests.get(url, stream=True)
    print ('Downloading TinyImageNet Data' )
    zip_ref = zipfile.ZipFile(BytesIO(r.content))
    for file in notebook.tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
      zip_ref.extract(member = file)
    zip_ref.close()
    
def download_url(url,fileName):
    if(os.path.isfile(fileName)==False) :
          print ('Downloading ' + url )
          try:
                r = requests.get(url, stream=True)
                with open(fileName,'wb') as f: 
                  f.write(r.content) 
          except :
                print ("Exception to download file",fileName)
                return False
    else:
        print (fileName, " already exists in ",os. getcwd()) 
    
def extract_zipfile(download_folder,fileName):
    
    with ZipFile(fileName, 'r') as zip: 
         try:
              #zip.printdir() 
              print('Extracting file ' + fileName + ' now... to ',extracted_folder) 
              zip.extractall() 
              print('File Extraction Done!') 
              return 
         except:
              print ("Exception to Unzip file",fileName)
              return 
          
#IMAGES_URL = 'http://cs231n.stanford.edu/tiny-imagenet-200.zip'
#fileName = "tiny-imagenet-200.zip"
#download_folder = "/Users/srinivasang/code/school_of_ai/chap12/"

#download_images(IMAGES_URL)
#extract_zipfile(download_folder,fileName)

