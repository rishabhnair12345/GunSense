import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('C:\\Users\\risha\\Documents\\GunSense\\cascade.xml')
camera = cv2.VideoCapture(0)

firstFrame = None

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to read frame from camera")
        break

    frame = imutils.resize(frame, width=1000)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    gunExist = False

    if len(gun) > 0:
        gunExist = True

        for (x, y, w, h) in gun:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray = gray[y: y + h, x: x + w]
            roi_color = frame[y: y + h, x: x + w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if gunExist:
        print("Gun detected")
    else:
        print("Gun not found")

# Release the camera and destroy all windows
camera.release()
cv2.destroyAllWindows()
