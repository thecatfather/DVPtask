# from skimage.feature import canny
import skimage.io as io
import cv2
import numpy as np
import glob

def contains_blue(img):
    # Convert the image to HSV colour space
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # Define a range for blue color
    hsv_l = np.array([100, 150, 0])
    hsv_h = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, hsv_l, hsv_h)

    return cv2.countNonZero(mask) > 100


def classify(t_color):
    correct = 0
    all = 0
    for img_path in glob.glob("H:\perception\cones_images/"+t_color+"*.png"):
        all+=1
        p_color = "yellow"
        img = io.imread(img_path)
        if(contains_blue(img)):
            p_color = "blue"
        if(p_color==t_color):
            correct+=1
    print("got %d correct out of %d for color %s" % (correct, all, t_color))

if __name__ == '__main__':
    classify("blue")
    classify("yellow")
    