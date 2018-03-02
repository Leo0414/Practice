import cv2
import numpy as np

def color_space_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    cv2.imshow("yuv",yuv)
    Ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("Ycrcb", Ycrcb)

print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
color_space_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
