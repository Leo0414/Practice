import cv2
import numpy as np

def access_pixel(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s\nheith : %s\nchannels : %s"%(width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv2.imshow("pixels_demo", image)


def inverse(image):
    dst = cv2.bitwise_not(image)
    cv2.imshow("inverse demo", dst)


def create_image_demo():
    # img = np.zeros([400, 400, 3], np.uint8)
    # img[:, :, 0] = np.ones([400, 400])*255
    # img[:, :, 2] = np.ones([400, 400])*255
    # cv2.imshow("new image", img)

    # img = np.zeros([400, 400, 1], np.uint8)
    # img[:, :, 0] = np.ones([400, 400]) * 127
    # img = np.ones([400, 400, 1], np.uint8)
    # img = img * 127
    # cv2.imshow("new image", img)
    # cv2.imwrite(r"C:\Users\Leo\Desktop\save-image\np.new.jpg", img)

    m1 = np.ones([3, 3], np.uint8)
   # cv2.convertScaleAbs(m1)
    m1.fill(122.2388)
    print(m1)

    m2 = m1.reshape([1, 9])
    print(m2)

    m3 = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]], np.int32)
    m3.fill(9)
    print(m3)

print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")  # blue, green, red
cv2.namedWindow("input image")
cv2.imshow("input image", src)
t1 = cv2.getTickCount()
#access_pixel(src)
#inverse(src)
create_image_demo()
t2 = cv2.getTickCount()
time = (t2 - t1)/cv2.getTickFrequency()*1000
print("time:%s ms"%(time))
cv2.waitKey(0)
cv2.destroyAllWindows()