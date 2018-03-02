import cv2
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 255])
    plt.show()


def threshlod_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    print("threshold value %s" % ret)
    plot_demo(image)
    cv2.imshow("binary_demo", binary)

print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\orange.jpg")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
threshlod_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
