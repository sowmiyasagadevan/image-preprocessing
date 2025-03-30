import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb2.webp")
(b,g,r)=img[100,50]
print("r={},g={},b={}".format(r,g,b))
cv2.imshow("image" ,img)
