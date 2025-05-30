import cv2 as cv

img = cv.imread("./photos/cute-kitten-4k-im.jpg")
cv.imshow('cat',img)

def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions, interpolation= cv.INTER_AREA)


resized_image = rescaleframe(img,0.5)
cv.imshow('resized image',resized_image)


def changeRes(width,height):
    # only for live video
    capture.set(3,width)
    capture.set(4,height)





capture = cv.VideoCapture("./videos/tanushrees_video.mp4")

while True:
    isTrue, frame = capture.read()
 
    frame_resized = rescaleframe(frame, scale = 0.2)

    cv.imshow('video',frame)
    cv.imshow('Resized Video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()