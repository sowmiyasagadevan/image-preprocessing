import cv2
image=cv2.imread(r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\data\rgb2.webp")
output=image.copy()
cv2.putText(output,"nature",(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
cv2.imshow("text",output)
cv2.waitKey(0)
