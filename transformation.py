import cv2 as cv
import numpy as np

img = cv.imread('./photos/cat.jpeg')
cv.imshow('cat',img)

def translate(img,x_axis,y_axis):
    transMat = np.float32([[1,0,x_axis],[0,1,y_axis]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> left
# x --> right
# -y --> up
# y --> down
translated = translate(img ,-100,  100)
cv.imshow('translated image',translated)


#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[0:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)


    rotMat = cv.getRotationMatrix2D(rotPoint, angle , 1.0)
    dimensions = (width ,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img , -45)
cv.imshow("rotated image",rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow("rotated_rotated image",rotated_rotated)
# Resizing 

resized = cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# flipping
flip = cv.flip(img ,-1) # 1 = horizontal flip 
#  -1 = vertical flip as well as horizontal
cv.imshow('flip',flip)

# cropping

cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)