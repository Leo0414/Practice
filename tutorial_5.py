import cv2
import numpy as np

def fill_color_demo(image):
    copyImage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)    # mask一定要是np.uint8
    cv2.floodFill(copyImage, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow("fill_color_demo", copyImage)

def fill_binary_demo(image):
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    # copyImage = image.copy()
    # h, w = image.shape[:2]
    # mask = np.zeros([h+2, w+2], np.uint8)    # mask一定要是np.uint8
    # cv2.floodFill(copyImage, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow("fill_binary_demo", image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:302, 101:301] = 0
    cv2.floodFill(image, mask, (105,105), (0, 180, 255), cv2.FLOODFILL_MASK_ONLY)
    cv2.imshow("filled binarydemo", image)


print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)

# face = src[50:250, 50:250]
# gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)
# backface = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# cv2.imshow("backface", backface)
# src[50:250, 50:250] = backface
# cv2.imshow("face", src)

#fill_color_demo(src)
fill_binary_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
