import cv2 as cv

arno = cv.imread("C:/Users/revna/Desktop/KJ Somaiya/SY/Sem 4/WP/Mini-Project/Images/Arnolfini.jpg") #reads image

cv.imshow('Arno', arno)

def rescaleFrame(frame, scale =0.75): #75% reduced
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(arno)
cv.imshow('Rescaled Image', resized_image)

cv.waitKey(0)