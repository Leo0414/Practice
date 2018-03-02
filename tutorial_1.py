import cv2
import numpy as np

def video_demo():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()   # 画面左右颠倒，产生视角差异
        frame = cv2.flip(frame, 1)   # cv2.flip()镜像变化，1为左右镜像，2为上下镜像
        cv2.imshow("video", frame)
        c = cv2.waitKey(50)
        if c ==32:   # 13回车  32空格， 27Esc
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)   # 打印图像的高、宽、通道数目
    print(image.size)    # 图像大小，等于图像宽、高、通道数目的乘积
    print(image.dtype)   # 字节位数，像素数据的数据类型uint8
    pix_data = np.array(image)
    print(pix_data)


print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
get_image_info(src)
video_demo()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.flip(gray, 1)
cv2.imwrite(r"C:\Users\Leo\Desktop\save-image\lena.jpg", src)
cv2.imwrite(r"C:\Users\Leo\Desktop\save-image\lena_gray.jpg", gray)
cv2.waitKey(0)
#cv2.destroyWindow("video")
cv2.destroyAllWindows()