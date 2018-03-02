import cv2
import numpy as np

def blur_demo(image):   # 均值模糊，用于去噪
    dst = cv2.blur(image, (15, 1))   # (15, 1)为卷积核的大小
    cv2.imshow("blur_image", dst)


def median_blur_demo(image):  #中值模糊,中值模糊用于去除椒盐噪声效果很好
    dst = cv2.medianBlur(image, 5)   # 5
    cv2.imshow("median_blur_demo", dst)

def custom_blur_demo(image):
    #kernel = np.ones([5, 5], np.float32)/25   # 经过卷积之后，像素值不能溢出，故而要除以25
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) / 9  #
    #  锐化卷积核，符合原则：元素为基数奇数，元素之和为1或0，为0时一般在做边缘或梯度，总和为1时一般在做增强锐化的工作

    dst = cv2.filter2D(image, -1, kernel=kernel)     # anchor是锚点，即卷积核中心，一般为【0，0】
    cv2.imshow("custom_blur_demo", dst)


print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lenanoise.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
#blur_demo(src)
#median_blur_demo(src)
custom_blur_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
