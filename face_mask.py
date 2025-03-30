import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier("C:/Users/sowmiyasagadevan/Downloads/haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("C:/Users/sowmiyasagadevan/Downloads/haarcascade_mcs_mouth.xml")
bw_threshold = 80
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
weared_mask_font_color = (255, 255, 255)
not_weared_mask_font_color = (0, 0, 255)
thickness = 2
font_scale = 1
weared_mask = "Thank you for wearing a mask!"
not_weared_mask = "Please wear a MASK to prevent COVID-19"
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, black_and_white = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        cv2.putText(img, "No face found...", org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            mouth_region_gray = roi_gray[h // 2 : h, :]
            mouth_rects = mouth_cascade.detectMultiScale(mouth_region_gray, 1.5, 5)

            if len(mouth_rects) == 0:
                cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
            else:
                cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)
    cv2.imshow('Mask Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
