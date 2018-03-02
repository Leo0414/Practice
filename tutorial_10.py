import cv2
import numpy as np

def equalHist_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(gray)
    cv2.imshow("equal-demo", dst)

def clahe_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv2.imshow("clahe_demo", dst)

def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16,1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            # index
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist

def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    match2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    match3 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
    print(type(match1))
    print("巴氏距离： %s, 相关性： %s, 卡方： %s" % (match1, match2, match3))
# 巴氏距离：越小越相似
# 相关性：越大越相似
# 卡方：越大越不相似




print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\rice.png")
#cv2.namedWindow("input image")
# cv2.imshow("input image", src)
# equalHist_demo(src)
# clahe_demo(src)

image1 = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
image2 = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lenanoise.png")
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
hist_compare(image1, image2)


cv2.waitKey(0)
cv2.destroyAllWindows()
