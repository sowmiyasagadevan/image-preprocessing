import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb1.jpg")
(h,w,d)=img.shape
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,-45,0.5)
rotated=cv2.warpAffine(img,M,(w,h))
cv2.imshow("Opencv Rotation" , rotated)
cv2.waitKey(0)
