import numpy as np
from PIL import Image
import random
import copy
import PIL

black = np.zeros((224,224))
bg_file_name = f'Background/bg1.jpg'
fg_file_name =f'Foreground/f61.png'
mask_file_name =f'Fg-Mask/mask1.jpg'

outfile = open("mapping.txt","a+")
bg = Image.open(bg_file_name)
start = 1

for j in  range(61,62): #1 foreground image  ---------------You should choose your numbers. Place only 20 images no flipped one-------
     
    fg = Image.open(f'Foreground/fg{str(j)}.png').convert('LA')
    mask = Image.open(f'Fg-Mask/mask{str(j)}.jpg').convert('LA')

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

        fg1.putalpha(255)
        bg1.paste(fg1,(r1,r2))
        flipfg.putalpha(255)
        bg2.paste(flipfg,(r1,r2))
        m1.putalpha(255)
        black_img1.paste(m1,(r1,r2))
        flipmask.putalpha(255)
        black_img2.paste(flipmask,(r1,r2))
            
        bg1.save(f"Fg-Bg/fg-bg{str(start)}.jpg",optimize=True, quality=30)
        black_img1.save(f"Fg-Bg-Mask/fg-bg-mask{str(start)}.jpg",optimize=True, quality=30) 
        outfile.write(bg_file_name + ' fg'+ str(j)+'.png' + ' mask'+ str(j)+'.jpg' + ' fg-bg' + str(start)+'.jpg' + ' fg-bg-mask' +str(start)+'.jpg' + '\n')
        start+=1
        
        bg2.save(f"Fg-Bg/fg-bg{str(start)}.jpg",optimize=True, quality=30)
        black_img2.save(f"Fg-Bg-Mask/fg-bg-mask{str(start)}.jpg",optimize=True, quality=30)
        outfile.write(bg_file_name + ' fg'+ str(j)+'.png' + ' mask'+ str(j)+'.jpg' + ' fg-bg' + str(start)+'.jpg' + ' fg-bg-mask' +str(start)+'.jpg'+ '\n')
        start+=1
        print(start)
        
outfile.close()