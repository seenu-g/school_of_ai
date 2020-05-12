import numpy as np
from PIL import Image
import random
import copy
import PIL

black = np.zeros((224,224))
bg_file_name = f'Background/bg1.jpg'
fg_file_name =f'Foreground/fg1.png'
mask_file_name =f'Mask/mask1.jpg'

import os
current_dir = os.getcwd()
path = os.path.join(current_dir, 'Fg-Bg') 
if(os.path.exists(path)==False) :
   os.mkdir(path) 
path = os.path.join(current_dir, 'Fg-Bg-Mask') 
if(os.path.exists(path)==False) :
    os.mkdir(path) 

outfile = open("audit.txt","a+")
start = 240001
for i in range(1,101): 
    bg = Image.open(f'Background/bg{str(i)}.jpg')
    for j in  range(61,81): 
            fg = Image.open(f'Foreground/fg{str(j)}.png').convert('RGBA')
            mask = Image.open(f'Mask/mask{str(j)}.jpg').convert('RGBA')

            for k in range(1,21): #---------------------Randomly Placing 20 times(Same for all)--------------------------------
            
                r1 = random.randint(1, 120)
                r2 = random.randint(1, 120)
                bg1 = copy.deepcopy(bg)
                bg2 = copy.deepcopy(bg)
                fg1 = copy.deepcopy(fg)
                m1 = copy.deepcopy(mask)
                black_img1 = Image.fromarray(black,mode='1')
                black_img2 = Image.fromarray(black,mode='1')

                flipfg = fg1.transpose(PIL.Image.FLIP_LEFT_RIGHT) #flip image
                flipmask = m1.transpose(PIL.Image.FLIP_LEFT_RIGHT) #flip mask

                bg1.paste(fg1,(r1,r2),fg1)
                bg2.paste(flipfg,(r1,r2),flipfg)
                black_img1.paste(m1,(r1,r2),m1)
                black_img2.paste(flipmask,(r1,r2),flipmask)
                    
                bg1.save(f"Fg-Bg/fg-bg{str(start)}.jpg",optimize=True, quality=30)
                black_img1.save(f"Fg-Bg-Mask/fg-bg-mask{str(start)}.jpg",optimize=True, quality=30) 
                outfile.write(' bg'+ str(i)+'.jpg' + ' fg'+ str(j)+'.png' + ' mask'+ str(j)+'.jpg' + ' fg-bg' + str(start)+'.jpg' + ' fg-bg-mask' +str(start)+'.jpg' + '\n')
                start+=1
                
                bg2.save(f"Fg-Bg/fg-bg{str(start)}.jpg",optimize=True, quality=30)
                black_img2.save(f"Fg-Bg-Mask/fg-bg-mask{str(start)}.jpg",optimize=True, quality=30)
                outfile.write(' bg'+ str(i)+'.jpg' + ' fg'+ str(j)+'.png' + ' mask'+ str(j)+'.jpg' + ' fg-bg' + str(start)+'.jpg' + ' fg-bg-mask' +str(start)+'.jpg'+ '\n')
                start+=1
                print(start)
                
                del r1 
                del r2 
                del bg1 
                del bg2 
                del fg1 
                del m1 
                del flipfg
                del flipmask 
                del black_img1 
                del black_img2
            del fg
            del mask
    del bg
        
outfile.close()