import cv2
import pytesseract
import csv
import smtplib     # Library for email sending
import ssl
from email.message import EmailMessage
a=[]
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Hp\AppData\Local\Tesseract-OCR\tesseract.exe'
frameWidth = 640
frameHeight =400
minArea=500
color=(255,0,255)
faceCascade =cv2.CascadeClassifier("numberplate.xml")
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
def send_mail_function2():
    email_sender = 'loc22drone@gmail.com'
    email_password = 'urhnzxrusokvtncc'
    email_receiver = a[5]
    subject = 'EMERGENCY'
    body = """"
    THERE IS A POSSIBILITY OF GUNSHOTS OF ABOVE 80 DECIBELS HEARD AT 36.13379407735641 LATITUDE AND 72.69994205020329 LONGITUDE
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("MAIL SENT SUCCESSFULY")

while True:
    success, img=cap.read()
    imgGray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        area=w*h
        if area >minArea:

            cv2.rectangle(img, (x,y) , (x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi =img[y:y+h,x:x+w]
            text_1 = pytesseract.image_to_string(imgRoi)
            print(text_1)
            print(len(text_1))
            if(len(text_1)==14):
               # print("hel")
                with open("data.csv", 'r') as file:
                    csvreader = csv.reader(file)
                    for i in csvreader:
                        #print(i)
                       # print("in csv")
                      #  print(text_1,"---------",i[0])
                        if((text_1.strip())==(i[0].strip())):
                            #print("text verified")
                            a=i
                            if(a[0]==text_1):
                                if(a[3]=="no" or a[4]=="no"):
                                    send_mail_function2()
                                    break

            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
    if(cv2.waitKey(1)& 0xFF==ord('q')):
        break