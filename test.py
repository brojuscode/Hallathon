import cv2
from PIL import Image
import threading
import smtplib     # Library for email sending
import ssl
from email.message import EmailMessage
import imghdr
frameWidth = 640
frameHeight =400
minArea=500
color=(255,0,255)
runOnce=False
faceCascade =cv2.CascadeClassifier("face.xml")
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
while True:
    success, img=cap.read()
    imgGray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        area=w*h
        if area >minArea:

            cv2.rectangle(img, (x,y) , (x+w,y+h),(255,0,0),2)
            cv2.putText(img,"WITHOUT HELMET",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            if runOnce == False:
                print("Mail send initiated")
                # To call alarm thread
                runOnce = True
            if runOnce == True:
                print("Mail is already sent once")
                runOnce = True
            imgRoi =img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
    if(cv2.waitKey(1)& 0xFF==ord('q')):
        break