import cv2

image=cv2.imread("static\img\yaraizi.jpg")

height, width = image.shape[:2]

start_row, start_col = int (height * .25), int (width * .30)

end_row, end_col = int (height * .60), int (width * .60)

cropped = image [start_row : end_row , start_col : end_col]

cv2.imshow ("Kesilmis Resim", cropped)

cv2.imwrite("static\img\yara-kesme.jpg",cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
