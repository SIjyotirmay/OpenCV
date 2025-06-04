import cv2 as cv
#  5 essential functions of openCV
img = cv.imread("./photos/cat.jpeg")
cv.imshow('cat',img)
#converting to grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#Blur
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)#(7,7) or (3,3) is kernel size

cv.imshow('blur',blur)

#Edge Cascade

canny = cv.Canny(img , 125 ,175)
cv.imshow('canny edges',canny)

canny2 = cv.Canny(blur , 125 ,175)
cv.imshow('canny2 edges',canny2)

#Dilating the image
dilated = cv.dilate(canny2,(7,7),iterations = 3)
cv.imshow('dilated edges',dilated)


#Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('eroded',eroded)

#resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)