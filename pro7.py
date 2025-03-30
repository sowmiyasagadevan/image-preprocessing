import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb1.jpg")
blurred=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("blurred" , blurred)
cv2.waitKey(0)
