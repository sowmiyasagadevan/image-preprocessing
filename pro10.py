import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb2.webp")
output=img.copy()
cv2.line(output,(60,20),(4000,200),(0,65,25),5)
cv2.imshow("line",output)
cv2.waitKey(0)
