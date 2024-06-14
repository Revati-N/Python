import cv2 as cv
import numpy as np

#Original Image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#To colour full picture: 
'''
blank[:] = 0,255,0
cv.imshow('Green', blank)
'''

'''
#To colour small part of picture: 

blank[200:300, 200:300] = 0,255,0
cv.imshow('Green', blank)
'''

'''
# For a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness=3)
cv.imshow('Line', blank)
'''

cv.waitKey(0)