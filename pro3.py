import cv2
img=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb2.webp")
roi=img[70:170,440:540]
cv2.imshow("ROI",roi)
