import cv2
import numpy as np
from matplotlib import pyplot as plt

def back_projection_demo():
    sample = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\sample.png")
    target = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\orange.jpg")
    roi_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    # show images
    cv2.imshow("sample", sample)
    cv2.imshow("target", target)

    roiHist = cv2.calcHist([roi_hsv], [0, 1], None, [28, 32], [0, 180, 0, 256])
    cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv2.imshow("backProjection_demo", dst)


def hist2d_demo(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([image], [0, 1], None, [32, 32], [0, 180, 0, 256])
    # cv2.imshow("hist2d", hist)
    plt.imshow(hist, interpolation="nearest")
    plt.title("2D Histogram")
    plt.show()

print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
# cv2.namedWindow("input image")
# cv2.imshow("input image", src)
hist2d_demo(src)
#back_projection_demo()
cv2.waitKey(0)
cv2.destroyAllWindows()
