import cv2
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 255])   # image.ravel()是用来统计图像所有频次的
    plt.show()


def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
plot_demo(src)
image_hist(src) 
cv2.waitKey(0)
cv2.destroyAllWindows()
