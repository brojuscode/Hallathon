import cv2
import pytesseract
import csv
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
while True:
    success, img=cap.read()
    imgGray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        area=w*h
        if area >minArea:

            cv2.rectangle(img, (x,y) , (x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Numebr plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi =img[y:y+h,x:x+w]
            text_1 = pytesseract.image_to_string(imgRoi)
            print(text_1)
            with open("data.csv", 'r') as file:
            csvreader = csv.reader(file)
            for i in csvreader:
                for j in i:
                    c=0
                    for k in range(0,len(j)):
                        if(j[k]=="\t"):
                            a.append(j[c,k])
                            print(1)
                            c=k
      break  
print(a)


            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
    if(cv2.waitKey(1)& 0xFF==ord('q')):
        break