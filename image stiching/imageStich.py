import cv2 as cv

# image_paths is an array which contains the path of all the images that needs to be stiched
image_paths=['./image/second/1.jpg','./image/second/2.jpg','./image/second/3.jpg','./image/second/4.jpg','./image/second/5.jpg','./image/second/6.jpg','./image/second/7.jpg','./image/second/8.jpg']

# inilised a list of images where the images will be stored 
imgs = []
 
for i in range(len(image_paths)):
    imgs.append(cv.imread(image_paths[i]))

    #scaling down size of image as the image from different camera can be of differemt size
    imgs[i] = cv.resize( imgs[i], (0,0), fx = 0.2, fy = 0.2)
    

# showing the original pictures
for i in range(len(imgs)):
    cv.imshow(i,imgs[i])

 

#Main logic
stitchy=cv.Stitcher.create()
(flag,output)=stitchy.stitch(imgs)
 

# checking if the stitching procedure is successful
if flag != cv.STITCHER_OK:
    print("stitching ain't successful")
else:
    print('Your Panorama is ready!!!')
 
# final output
cv.imshow('final result',output)
 
cv.waitKey(0)