import cv2
import numpy as np

img=cv2.imread("C:\\Users\pc\Python Projeleri\morfolojik\static\img\griresim.jpg",0)

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(img,kernel,iterations=1)

cv2.imshow("asinmis resim",erosion)

cv2.imwrite("C:\\Users\pc\Python Projeleri\morfolojik\static\img\gri_asinma.png",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
