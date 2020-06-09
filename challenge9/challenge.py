# import packages to fetch distinguishing features
import numpy as np
import cv2
from matplotlib import pyplot as plt

# get 100 most distinguishing points of both photos
# fix the proportions between both photos
# compare distance to every other point
# come up with a 'similarity score' to return


def main(first, second):
    image1 = cv2.imread(first)
    image2 = cv2.imread(second)
    corners1 = returnCorners(image1)
    corners2 = returnCorners(image2)
    corners1 = normalize(corners1)
    corners2 = normalize(corners2)
    return similarityScore(corners1, corners2)



def normalize(corners):
    np_arr_to_return = numpy.zeros((100,2))
    multiplierX = 1
    multiplierY = 1
    greatestValueIndexX = 0;
    greatestIndexValueX = 0;
    greatestValueIndexY = 0;
    greatestIndexValueY = 0;
    # find greatest x value and set mulitplier
    for i in corners:
        if(corners[i][0]  > greatestIndexValueX):
            greatestIndexValueX = corners[i][0]
            greatestValueIndexX = i
        if(corners[i][1]  > greatestIndexValueY):
            greatestIndexValueY = corners[i][1]
            greatestValueIndexY = i

    multiplerX = greatestIndexValueX
    # find greatest x value
    # find greatest y value
    d = 5
    return np_arr_to_return

def similarityScore(corners1, corners2):
    # match 1 point from one to another point
    return 4

def returnCorners(image):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
    corners = np.int0(corners);
    np_arr = numpy.zeros((100,2))
    for i in corners:
        x,y = i.ravel()
        np_arr[i][0] = x
        np_arr[i][1] = y
    return np_arr
