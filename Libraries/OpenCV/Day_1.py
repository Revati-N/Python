# TO LOAD/READ IMAGES

import cv2 as cv #imports image

arno = cv.imread("/Images/Arnolfini.jpg") #reads image

cv.imshow('Arnolfini', arno) #function to show image

cv.waitKey(0) #waits till any key is pressed to close the tab.
