import numpy as np
import cv2 as cv
import imutils #is used for resizing images
import datetime

gun_cascade=cv.CascadeClassifier(r'C:\Users\HP\OneDrive\Desktop\python projects\gun detection\cascade (1).xml')
camera=cv.VideoCapture(0)
first_frame=None
gun_exists=None

while True:
    ret,frame=camera.read()
    frame=imutils.resize(frame,width=500)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #convert color blue green red to gray scale
    gun=gun_cascade.detectMultiScale(gray,1.3,5,minSize=(100,100)) #detecting gun in the frame
    
    if len(gun)>0:
        gun_exists=True
    for (x,y,w,h) in gun:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
    if first_frame is None:
        first_frame=gray
        continue
    cv.imshow("Security feed",frame)
    key=cv.waitKey(1) & 0xFF
    if key==ord('q'):
        break
if gun_exists:
    print("gun detected")
else:
    print("gun not detected")
camera.release()
cv.destroyAllWindows()
#this program detects gun in the frame captured by the camera
#it uses haar cascade classifier for gun detection

    