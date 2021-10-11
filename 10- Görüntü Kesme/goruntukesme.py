import cv2

image=cv2.imread("static\img\kesme.jpg")

height, width = image.shape[:2]

start_row, start_col = int (height * .07), int (width * .42)

end_row, end_col = int (height * .90), int (width * .90)

cropped = image [start_row : end_row , start_col : end_col]

cv2.imshow ("Kesilmis Resim", cropped)

cv2.imwrite("static\img\kesme_yeni.jpg",cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
