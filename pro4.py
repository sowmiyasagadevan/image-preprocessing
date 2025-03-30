import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb2.webp")
resized=cv2.resize(img,(200,200))
cv2.imshow("fixed resizing",resized)
cv2.waitKey(0)
