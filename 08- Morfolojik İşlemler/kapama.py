import cv2
import numpy as np

img=cv2.imread("C:\\Users\pc\Python Projeleri\morfolojik\static\img\morfolojik.png",0)

kernel=np.ones((5,5),np.uint8)

closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow("kapanmis resim",closing)

cv2.imwrite("C:\\Users\pc\Python Projeleri\morfolojik\static\img\morfolojik_kapanma.jpg",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
