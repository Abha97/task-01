
import cv2

 

img = cv2.imread("/Task01.jpg")
cv2_imshow(img)

Original_Image = cv2.cvtColor(img, 0)
New_Image = cv2.GaussianBlur(Original_Image, (3,3), 0)

 

sobelx = cv2.Sobel(src=New_Image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=New_Image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=New_Image, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

 

cv2_imshow(sobelx)
cv2_imshow(sobely)
cv2_imshow(sobelxy)

 

edges = cv2.Canny(image=New_Image, threshold1=120, threshold2=240)
cv2_imshow(edges)

cv2.destroyAllWindows()
