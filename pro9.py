import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb2.webp")
output=img.copy()
cv2.circle(output,(300,150),20,(255,0,0),-1)
cv2.imshow("circle",  output)
cv2.waitKey(0)
