import cv2
import numpy as np

print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
cv2.namedWindow("input image")
cv2.imshow("input image", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
