import cv2

image=cv2.imread("static\img\cevrilecek.jpg")

height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2),180, .9)

rotated_image = cv2.warpAffine(image, rotation_matrix,(width,height))

cv2.imshow ("Rotate image", rotated_image)

cv2.imwrite("static\img\rotate_yeni.jpg",rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
