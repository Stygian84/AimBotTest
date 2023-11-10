import cv2 as cv
import numpy as np

purple = np.uint8([[[255,0,255 ]]])
hsv_purple = cv.cvtColor(purple,cv.COLOR_BGR2HSV)
print( hsv_purple )