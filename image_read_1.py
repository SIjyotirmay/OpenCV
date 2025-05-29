import cv2 as cv

img=cv.imread("./photos/cute-kitten-4k-im.jpg")

cv.imshow('cat',img)

cv.waitKey(0)