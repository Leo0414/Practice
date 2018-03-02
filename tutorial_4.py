import cv2
import numpy as np

def add_demo(m1, m2):
    dst = cv2.add(m1, m2)
    cv2.imshow("add_demo", dst)

def subtract_demo(m1, m2):
    dst = cv2.subtract(m1, m2)
    cv2.imshow("sbutract_demo", dst)

def divide_demo(m1, m2):
    dst = cv2.divide(m1, m2)
    cv2.imshow("divide_demo", dst)

def multiply_demo(m1, m2):
    dst = cv2.multiply(m1, m2)
    cv2.imshow("divide_demo", dst)

def others(m1, m2):

    # M1 = cv2.mean(m1)  # 求均值
    # M2 = cv2.mean(m2)
    M1, dev1 = cv2.meanStdDev(m1)   #返回均值跟标准方差
    M2, dev2 = cv2.meanStdDev(m2)
    h, w = m1.shape[:2]
    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv2.meanStdDev(img)
    print(m)
    print(dev)

    # 方差小于某一个阈值表示为无效图像，无效信息

def logic_demo(m1, m2):
    dst = cv2.bitwise_and(m1, m2)
    #dst = cv2.bitwise_or(m1, m2)
    cv2.imshow("logic_demo",dst)

def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([w, h, ch], image.dtype)
    dst = cv2.addWeighted(image, c, blank, 1-c, b)
    cv2.imshow("con-bri-demo", dst)


print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
src1 = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\LinuxLogo.jpg")
src2 = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\WindowsLogo.jpg")
print(src1.shape)
print(src2.shape)
#cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("image1", src1)
# cv2.imshow("image2", src2)

# add_demo(src1, src2)
# subtract_demo(src1, src2)
#divide_demo(src1, src2)
#multiply_demo(src1, src2)
#others(src1, src2)
#logic_demo(src1, src2)
contrast_brightness_demo(src, 1.2, 10)   # 1.2为对比度，每个通道的像素值提升10
cv2.waitKey(0)
contrast_brightness_demo(src, 1.5, 00)
cv2.waitKey(0)
cv2.destroyAllWindows()
