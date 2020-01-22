
#Which box value shall be used in img.crop such that the colorful Python Logo is completely visible
# Which Operation will hide the Colorful Python logo completely?

from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRZpTmijaNOH6MmycM_eiPKcEl5mVvbwl7a8YKVGpEEMIanDcSt')
img = Image.open(BytesIO(response.content))
display(img) # comment this line and image till not be displayed
print(img.format, img.size, img.mode)

im = Image.new(mode = "RGB", size = (200, 200)) 
#im.show() 

box1 = (150, 150, 300, 300)
box2 = (200, 100, 250, 200)
box3 = (100, 0, 200, 200)
box4 = (100, 400, 200, 200)
box5 = (0, 0, 100, 100)
box6 = (200, 0, 200, 200)
box7 = (0, 0, 200, 200)
box8 = (100, 100, 200, 200)
box9 = (100, 250, 400, 300)
boxDisplay = (0,0, 610,203)
boxDisplay = (0,0, img.size[0]+10,img.size[1]+10)
region = img.crop(boxDisplay)
display(region) # comment this line and image till not be displayed

