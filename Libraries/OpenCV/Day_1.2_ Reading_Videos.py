# Reading VIDEOS

import cv2 as cv

capture  = cv.VideoCapture('C:/Users/revna/Downloads/dog.mp4') #loading video

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # to break out of the loop
        break

capture.release() # release the capture
cv.destroyAllWindows() #removes all videos
