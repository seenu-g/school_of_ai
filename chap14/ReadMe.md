Solving requirements provided in Assignment_Requirements.txt required multiple iterations going up and Down
to ensure that we do not create garbage.

Describe Data files and source files. Then explains activity

Data files
1. Dataset output is present in Google Drive
https://drive.google.com/drive/folders/1W4B4YRgMHXstVExFzE6An1rz2DkowVrj?usp=sharing
2. Foreground also present in https://github.com/seenu-g/school_of_ai/tree/master/chap14/Background
3. Background also present in https://github.com/seenu-g/school_of_ai/tree/master/chap14/Foreground
4. Mask images also present in https://github.com/seenu-g/school_of_ai/tree/master/chap14/Mask

Display samples images corresponding to fg, bg,mask,fg-bg,fg-bg-mask and depth as part of
calculate_Mean_StdDeviation.ipynb, which also contains Calculations of mean and standard deviation

fg-Bg
Mean               : [0.65830478 0.61511271 0.5740604 ]
Standard Deviation : [0.24408717 0.2542491  0.26870159]
fg-Bg-Mask
Mean               : [0.04608837 0.04608837 0.04608837]
Standard Deviation : [0.20544916 0.20544916 0.20544916]
Depth
Mean               : [0.50911522 0.50911522 0.50911522]
Standard Deviation : [0.28174302 0.28174302 0.28174302]

Python Collab Files
1.Overlap_and_maks.ipynb - generate fg-bg, fg-bg-mask images including flip
2.DepthMapsTrial.ipynb - generate depth images
3.create_dataset.ipynb - merges ZIP files of my dataset
4.calculate_Mean_StdDeviation.ipynb - Calculate mean and standard deviation for  5 zip image files of the dataset
5.generate_labels.ipynb - generate labels for  5 zip image files of the dataset

# Activity 1: Data Generation (Overlap_and_maks.ipynb)
Step 1: Collected 100 background images.(naming format as bg_<<n>>.png))
Step 2: Collected 20 foreground images, removed it's background and made it transparent.(naming format  as fg_<<n>>.png)
Step 3: Create mask for each of foreground images using GIMP (naming format  as mask_<<n>>.jpg)
Step 4: Overlay foreground, foreground_mask on background, background-mask, flip to generate (fg_bg.img and fg_bg_mask.jpg)
Step 5: Package as .ZIP files and Perform Calculations for mean and standard deviation

# Activity 2: Generate Depth images for fg-bg images(DepthMapsTrial.ipynb)
Step 1 : unpackage ZIP
Step 2 : Setup Code-repo and already trained model file. Make code changes for our needs
Step 3 : Generate Depth images
Step 4 : Package as ZIP file

# Activity 3: Packaging 5 independently generated 80K images to created 400K images (erges ZIP files of my dataset)
Step 1. Merage Output of activity 1 and activity 2 in to single ZIP file( 5 files instead of 10
Step 2. Calculate mean and standard deviation across all 5 ZIP files(calculate_Mean_StdDeviation.ipynb)
Step 3: Generate Labels in the order  FG BG FG-BG FG-BG-Mask Depth (generate_labels.ipynb)

# Activity 1:Data Preparation
Prepare image set with foreground(fg), background(bg), mask(fg-mask), fg_bg and fg_bg_mask

## Step 1: Collected 100 background images.(naming format as bg_<<n>>.png))
1. Chose Living Room as a background image theme 
2. Downloaded 100 different types living rooms as .JPG files
3. Resized all to 224x224. 
Did some dance to have most background image size  around 10-20 kb.

## Step 2: Collected 20 foreground images, removed it's background and made it transparent.(naming format  as fg_<<n>>.png)
1. chose Humans as foreground image theme.
2. Downloaded  100 different types of humans(single, human) as .PNG files
3. Removed their background using PPT(Tried with Gimp and failed to remove transparency. Took help as my powerpoint was old version)
4. Save processed image as .PNG (PNG images have 4 channels-4th channel represents transparency )
5. Image dimesntionsize was between 100-120 px and maintained apect ratio.
Most foregound images  are of size 5-10 kb approx. 

## Step 3: Create mask for each of foreground images using GIMP (naming format  as mask_<<n>>.jpg)
1.Select the transparent foreground image, go to colors and select invert colors. It will give white image with black background.
2.Then select threshold, vary the threshold values till you get complete white mask.
3.Then exported mask as .JPG files

## Step 4a: Overlay foreground on background and generate (naming format fg_bg.jpg)
[ As our team has 5, we separated and created 80000 images, leading to 400K images in total]
1. For each background images, 
   1. we took 20 foreground images,
   2. their flips, For flips we used PIL modules Image.FLIP_LEFT_RIGHT function.(see it as fg_bg_flip)
   3. and overlapped fg images 20 times at 20 random positions over bg images
  [bg.paste(fg, (r1,r2),fg), where bg is background image, fg is foreground image, (r1,r2) are the top-left overlayed position.]
   4. Optimize image, reduce it quality to 30, so that to use less storage space
{Remember that Step 4a and Step 4b were done together. So (r1,r2) remained common across both)
## Step 4b: Generate masks for overlayed image (naming format fg_bg_mask.jpg)
1.  Generate black background of the same size as background images
2.  Overlayed the foreground mask on top of it.
3.  Repeated step 3 and Step 4 here ( see it as creation of fg_bg_mask and fg_bg_mask)

Generation took 10 minutes for 80K images. [At end of fighting and getting things right]

## Step 5 : Package and Do Calulations
1. Confirmed that 80K images are generated(400K images in total as group) across fg_bg and fg_bg_mask
2. Merged the folders and zipped it.[Lot of fun and have to be carful.Learnt to extract single image from Zip file]
 [ Wrote within my own drive and Collab stopped working. Have to clean files. 
   Have to place generated image in Step 4 to place them at content folder(drive.mount('/content/gdrive'))
   Generated Zip alone was stored in my drive as data_Part3.ZIP]
3. Calculate Mean and Standard Deviation of fg-bg images.

For 80K images, data_Part3.ZIP size was 572 MB
Time taken to generate 80K images : 10 minutes

# Activity 2: Generate Depth images for fg-bg images
Here we tried to leverage pre-trained model to generate depth images.[ we have no depth camera]
https://github.com/ialhashim/DenseDepth
[Selected other background images and then move to living room theme, 
as this repo seems to be build on NYU dataset that contains living rooms]

## Code mofifications [ Modification are present in Google Collab itself]
1. layer.py - upgrade for c tf>2.0, Renamed "resize_images" as "resize"
2. utils.py - added resize(448,448), since 224 is very small, result is half the size of output. So we doubled the size.
              display Images - we converted the images to grayscale and saved the image.
3. test.py - change to incorporate
    1. Removed the glob that took direct images path as input, as we cannot load 400K images
    2. Processed the images as batches. 200 images per batch.
    3. While running 80k/200 times,  Collab crashed. We change start number at crash based on images already processed


## Step 1 : Unzip image file to content folder(drive.mount('/content/gdrive'))
## Step 2 : Clone Depth model output from
         wget https://s3-eu-west-1.amazonaws.com/densedepth/nyu.h5 -O ./DepthModel/nyu.h5
## Step 3 : Generate depth images using modified code from test.py
## Step 4 : Zip images  and the generated Zip alone was stored in my drive as Depth_Part3.ZIP ]

Zipped the entire folder
Each depth image size is 2-3kb. Each of 5 zip files took around 260-290 MB of storage. 
It took around 3-4 hours to generate depth for 80k images.

For 80K images, Depth_Part3.zip size was 236 MB. 
Time taken to generate 80K images[ intermittent crashes]: 6 hours

# Activity 3: Packaging
Merge fg-bg and depth images in to 5 Zip files(instead of 10(5+5)) 
[ done for data_part3.zip in create_dataset.ipynb
1. Unzip  data_Part3.ZIP to folders under content folder(drive.mount('/content/gdrive')
2. Unzip  Depth_Part3.zip to folder under content folder(drive.mount('/content/gdrive')
3. Merge folders under content folder
4. Create new Zip files that got store in my drive as data_part3.zip

# Activity 4: Calculate Mean and Standard Deviation 
[done for data_part1.zip ,....,....,...,data_part5.zip in calculate_Mean_StdDeviation.ipynb]
1. Unzip files under content folder(drive.mount('/content/gdrive')
2. Calculate mean and standard deviation
3. Generate Labels(generate_labels.ipynb) that containspath of all images. 
It is in a order FG BG FG-BG FG-BG-Mask Depth

# Folder Content and size
Background
bg1.jpg, bg2.jpg,------------------------------------------------------------,bg99.jpg,bg 100.jpg
Foreground
bg1.jpg, bg2.jpg,------------------------------------------------------------,bg99.jpg,bg100.jpg[Team]
bg61.jpg, bg62.jpg,------------------------------------------------------------,bg79.jpg,bg80.jpg[Team]
Dataset
--data_part1.zip
                  --data1
                         --Fg-Bg
                                ------fg-bg<<1-80K>>.jpg
                         --Fg_Bg-Mask
                                ------fg-bg-mask<<1-80k>>.jpg
                         --Depth
                                ------depth.jpb<<1-80k>>.jpg
--data_part2.zip
                  --data2
                         --Fg-Bg
                                ------fg-bg<<80-160K>>.jpg
                         --Fg_Bg-Mask
                                ------fg-bg-mask<<80-160k>>.jpg
                         --Depth
                                ------depth.jpb<<80-160k>>.jpg
--data_part4.zip
                  --data4
                         --Fg-Bg
                                ------fg-bg<<160-240K>>.jpg
                         --Fg_Bg-Mask
                                ------fg-bg-mask<<160-240K>>.jpg
                         --Depth
                                ------depth.jpb<<160-240K>>.jpg----data_part5.zip

--data_part3.zip
                  --data3
                         --Fg-Bg
                                ------fg-bg<<240-320K>>.jpg
                         --Fg_Bg-Mask
                                ------fg-bg-mask<<240-320K>>.jpg
                         --Depth
                                ------depth.jpb<<240-320K>>.jpg

--data_part5.zip
                  --data5
                         --Fg-Bg
                                ------fg-bg<<320-400K>>.jpg
                         --Fg_Bg-Mask
                                ------fg-bg-mask<<320-400K>>.jpg
                         --Depth
                                ------depth.jpb<<320-400K>>.jpg


total 4024M
-rw------- 1 root root 810M May 10 08:28 data_part1.zip
-rw------- 1 root root 804M May 10 08:29 data_part2.zip
-rw------- 1 root root 798M May 10 08:28 data_part3.zip
-rw------- 1 root root 807M May 10 10:14 data_part4.zip
-rw------- 1 root root 807M May 10 08:28 data_part5.zip

Background samples
![Background samples](https://github.com/seenu-g/school_of_ai/blob/master/chap14/result_display/Background.jpg?sanitize=true)
Foreground samples
![Foreground samples](https://github.com/seenu-g/school_of_ai/blob/master/chap14/result_display/Foreground.jpg?sanitize=true)
Mask samples
![Mask samples](https://github.com/seenu-g/school_of_ai/blob/master/chap14/result_display/mask.jpg?sanitize=true)
Fg-Bg samples
![Fg-Bg-Mask samples](https://github.com/seenu-g/school_of_ai/blob/master/chap14/result_display/Fg-Bg.jpg?sanitize=true)
Fg-Bg-Mask samples
![Fg-Bg-Mask samples](https://github.com/seenu-g/school_of_ai/blob/master/chap14/result_display/Fg-Bg-Mask.jpg?sanitize=true)
Depth samples
![Depth samples](https://github.com/seenu-g/school_of_ai/blob/master/chap14/result_display/Depth.jpg?sanitize=true)
