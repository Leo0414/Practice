import cv2
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv2.imshow("noise image", image)


print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)

t1 = cv2.getTickCount()
gaussian_noise(src)
t2 = cv2.getTickCount()
time = (t2 - t1) / cv2.getTickFrequency() * 1000
print("time:", time)

dst = cv2.GaussianBlur(src, (5, 5), 0)    # 高斯模糊对高斯噪声有抑制作用
cv2.imshow("Gaussian Blur", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
