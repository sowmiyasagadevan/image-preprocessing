import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb1.jpg")
(h,w,d)=img.shape
print("width={}, height={}, depth={}".format(w,h,d))
cv2.imshow("image",img)
cv2.waitKey(2)
