import cv2
import numpy as np

img=cv2.imread("C:\\Users\pc\Python Projeleri\morfolojik\static\img\morfolojik.png",0)

kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(img,kernel,iterations=1)


cv2.imshow("genlesmis resim",dilation)


cv2.imwrite("C:\\Users\pc\Python Projeleri\morfolojik\static\img\morfolojik_genlesme.jpg",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
