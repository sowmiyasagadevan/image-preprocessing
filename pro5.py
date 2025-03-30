import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb1.jpg")
(h,w,d)=img.shape
r=300.0/w
dim=(300,int(h*r))
resized=cv2.resize(img,dim)
cv2.imshow("ratio resize" , resized)
cv2.waitKey(0)
