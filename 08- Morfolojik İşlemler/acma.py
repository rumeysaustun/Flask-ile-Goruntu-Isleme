import cv2
import numpy as np

img=cv2.imread("C:\\Users\pc\Python Projeleri\morfolojik\static\img\morfolojik.png",0)

kernel=np.ones((5,5),np.uint8)

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow("acilmis resim",opening)

cv2.imwrite("C:\\Users\pc\Python Projeleri\morfolojik\static\img\morfolojik_acma.jpg",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
