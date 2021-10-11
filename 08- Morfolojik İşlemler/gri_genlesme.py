import cv2
import numpy as np

img=cv2.imread("C:\\Users\pc\Python Projeleri\morfolojik\static\img\griresim.jpg",0)

kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(img,kernel,iterations=1)

cv2.imshow("asinmis resim",dilation)

cv2.imwrite("C:\\Users\pc\Python Projeleri\morfolojik\static\img\gri_genlesme.png",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
