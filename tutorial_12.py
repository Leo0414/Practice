import cv2
import numpy as np


def template_demo():
    tpl = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\sample.png")
    target = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\orange.jpg")
    cv2.imshow("template image", tpl)
    cv2.imshow("target image", target)
    methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv2.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if md == cv2.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv2.rectangle(target, tl, br, (0, 0, 255), 2)
        #  cv2.imshow("match-" + np.str(md), target)
        cv2.imshow("result-" + np.str(md), result)



print('\tOpenCV Python\t'.center(50,'-'))
src = cv2.imread(r"C:\Users\Leo\Desktop\opencv-python\lena.png")
# cv2.namedWindow("input image")
# cv2.imshow("input image", src)
template_demo()
cv2.waitKey(0)
cv2.destroyAllWindows()
