import cv2
image=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb1.jpg")
output=image.copy()
cv2.rectangle(output,(450,80),(550,180),(0,0,225),2)
cv2.imshow("Rectangle",output)
cv2.waitKey(0)
