import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('Blank',blank)

# paint the image 
blank[200:300, 300:400] = 0,0,255

#Draw a ractangle 
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)

# draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40,(0,0,255),thickness=-1)

#Draw  a line
cv.line(blank , (0,0),(blank.shape[1]//2,blank.shape[0]//2), (0,255,255),thickness=3)

cv.line(blank , (100,250),(300,400),(255,255,255),thickness=2)


#write test
cv.putText(blank, 'Hello my name is Jyotirmay',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(34,55,90),2)
cv.imshow('Green',blank)
cv.waitKey(0)