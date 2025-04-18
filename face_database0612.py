from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True, help=r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\program\New folder\haarcascade_frontalface_default.xml")
ap.add_argument("-o", "--output", required=True, help=r"C:\Users\sowmiyasagadevan\OneDrive\Desktop\intenship\program\New folder\database")
args = vars(ap.parse_args())

detector = cv2.CascadeClassifier(args["cascade"])

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
total = 0

while True:
    frame = vs.read()
    orig = frame.copy()
    frame = imutils.resize(frame, width=400)
    rects = detector.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in rects:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) &0xFF
    if key == ord("k"):
        p = os.path.sep.join([args["output"],"{}.png".format(str(total).zfill(5))])
        cv2.imwrite(p, orig)
        total += 1
    elif key == ord("q"):
        break
print("[INFO] {} face images stored".format(total))
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()



















    
