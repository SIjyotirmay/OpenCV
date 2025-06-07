import cv2 as cv
import numpy as  np

img = cv.imread('./photos/cat.jpeg')
cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blank = np.zeros(img.shape,dtype = 'uint8')
cv.imshow('blank',blank)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(img, 125 , 175)
cv.imshow('cat cannny edges',canny)


#ret, thresh = cv.threshold(gray, 125 , 255, cv.THRESH_BINARY)
#cv.imshow('thresh',thresh)
contours , hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('Countours Drawn', blank)

cv.waitKey(0)