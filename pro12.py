import argparse
import cv2
import imutils
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True,help=r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\program\data.jpg")
args=vars(ap.parse_args())
image = cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh=cv2.threshold(gray,220,220,cv2.THRESH_BINARY_INV)[1]
cnts =cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours (cnts)
output=image.copy()
text = "i found {} objects!.format"(len(cnts))
cv2.putText(output ,text,(10,25),cv2.FONT_HERsHEY_SIMPLEX,0.7,(240,0,159),2)
cv2.imshow("contours",output)
cv2.waitKey(0)
