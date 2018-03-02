import cv2
import numpy as np


def bi_demo(image):
    dst = cv2.bilateralFilter(image, 0, 100, 15)  # d是distence
    cv2.imshow("bi_demo", dst)

def shift_demo(image):
    dst = cv2.pyrMeanShiftFiltering(image, 10, 50)
    cv2.imshow("shift_demo", dst)


print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\example.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
# bi_demo(src)
shift_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
