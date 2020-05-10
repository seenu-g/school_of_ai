from PIL import Image,ImageOps
import os
from math import ceil
import random
import copy

def display_file_names() :
    source_dir = '/Users/srinivasang/Downloads/'
    for i in range(61,81):
        fg  = Image.open(source_dir + "Foreground/fg" + str(i) + ".png")  
        fg_mask  = Image.open(source_dir + "Foreground-Mask/mask" + str(i) + ".jpg")  
        print(i,fg.size,fg_mask.size)

def alter_fg_image(src_img_dir, src_img_filename, dest_img_folder):
  image_path = os.path.join(src_img_dir,src_img_filename)
  MAX_SIZE = 100
  try:
    # https://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes
    org_img = Image.open(image_path).convert('LA')
    width,height = org_img.size
    ratio = width/height
    new_width = MAX_SIZE
    new_height = ceil(MAX_SIZE/ratio)
    if width < height:
      new_width = ceil(MAX_SIZE*ratio)
      new_height = MAX_SIZE
    # print(ratio,src_img_filename,[width,height],[new_width,new_height])
    altered_image = ImageOps.fit(org_img,(new_width,new_height), method=Image.ANTIALIAS)
    altered_image.save(os.path.join(dest_img_folder,src_img_filename))
  except Exception as e:
    print(e)
    pass

#source_dir = '//Users/srinivasang/code/school_of_ai/chap14/'
#alter_fg_image('Foreground','fg61.png','altered')

def generate_images(source, dest):
  bg_images = os.listdir(source['Background'])
  fg_images = os.listdir(source['Foreground'])
  for bg_image_name in bg_images:
    bg_image = Image.open(os.path.join(source['Background'], bg_image_name))
    for fg_image_name in fg_images:
      # https://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
      fg_image = Image.open(os.path.join(source['Foreground'], fg_image_name)).convert('RGBA')
      for placement in range(1,21):
        x1,y1 = random.randint(1,80), random.randint(1,80)
        bg_fg = copy.deepcopy(bg_image)

        bg_fg.paste(fg_image, (x1,y1), fg_image)
        bg_fg.save(os.path.join(dest,"bg-{}-fg-{}-{}.jpg".format(bg_image_name.split('.')[0],fg_image_name.split('.')[0],placement)))

generate_images({
      'Background': os.path.join(os.curdir,'Background/'),
      'Foreground': os.path.join(os.curdir,'Foreground/')
      }, 
      dest= os.path.join(os.curdir,'generated')
    )