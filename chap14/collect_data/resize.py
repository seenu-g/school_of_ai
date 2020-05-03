from IPython.display import Image as IMAGE
import numpy as np
from PIL import Image,ImageOps
import os
import matplotlib.pyplot as plt
import random

def resize(file_count, source_file_starts, source_extension,target_file_starts,target_extension) :
    for i in range(1,file_count):
        im = Image.open(source_file_starts + str(i) + source_extension)  
        im1 = im.resize((150,150))  
        im1.save(target_file_starts+str(i)+target_extension)
        
def overlay_bg_fg(bg_image, fg_image, output) :  
    bg = Image.open('layout3.jpeg')
    fg = Image.open('people1.png')

    bg.paste(fg, (20, 30), fg)

    bg.save(output)
    

def resize_bg() :
    print(os.getcwd())
    source_dir = os.getcwd() +"/original/living_room/"
    for i in range(1,101):
            im = Image.open(source_dir + "bg" + str(i) + ".jpeg")  
            im1 = im.resize((224,224))  
            im1.save("Resized/bg"+str(i)+".jpg")

def resize_fg() :
    print(os.getcwd())
    source_dir = os.getcwd() +"/original/"
    for i in range(1,21):
            im = Image.open(source_dir + "people" + str(i) + ".png")  
            im1 = im.resize((100,100))  
            im1.save("Resized/fg"+str(i+60)+".png")

def overlay_fg() :
    source_dir = os.getcwd() +"/Resized/"
    for i in range(1,21):
        bg = Image.open(source_dir + "bg"+str(i+60)+".jpg")
        fg = Image.open(source_dir + "fg"+str(i+60)+".png")
        bg.paste(fg, (20, 30), fg)
        bg.save("fg_bg/fg_bg"+str(i+60)+".jpg")
    
def overlay_fg_mask() :
    source_dir = os.getcwd() +"/masked/"
    for i in range(1,21):
        black = np.zeros((224,224,3))
        black_img = Image.fromarray(black,mode='RGB')
        # overlay fg-mask on bg-mask
        fg_mask = Image.open(source_dir+'mask'+str(i+60)+".png")
        fg_mask.putalpha(255)
        black_img.paste(fg_mask,(20,30),fg_mask)
        black_img.save('fg_bg_masked/fg-bg-mask'+str(i+60)+'.png')

#overlay_fg_mask()
resize_bg()