import numpy as np
import cv2
from matplotlib import pyplot as plt

# shi tomasi corner detector
# link https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
# need to be able to compare
np_arr = numpy.zeros((3,100,2))
for x in arange(3):
    image = cv2.imread('example' + str(x)+ ".jpg");
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
    corners = np.int0(corners);
    for i in corners:
        x,y = i.ravel()
        np_arr[x][i][0] = x
        np_arr[x][i][1] = y
