import cv2
import numpy as np
#import easyocr

frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("pak.xml")
minArea = 500

cap =cv2.VideoCapture(0)
cap.set(3,frameWidth) # 3 is for width and frameWidth = 640, we can directly put 360 as well in place of frameWidth in cap.set()
cap.set(4,franeHeight) # 4 is for height and we already have made the frameHeight variable = 480
cap.set(10,150) # 10 is the id for brightness and 130 is its parameter
count = 0

while True:
    success , img  = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # this will change the color of the webcam input

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) # here we are making a rectangle around the number plate detecting in our image
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2) # here we are putting the text over the detected plate
            imgRoi = img[y:y+h,x:x+w] # y:y+h is the total height, x:x+w gives the region of the number plate, we are defing our regin of interest
            cv2.imshow("Result",imgRoi) # displaying or regin of interest
    cv2.imshow("Live",img) # Live
    if cv2.waitKey(1) & 0xFF ==ord('s'): # pressing 's' will save the detected number plate
        cv2.imwrite("IMAGES"+str(count)+".jpg",imgRoi) # giving name to our saved image
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2) # after pressing 's' this will display SCAN SAVED on the screen
        cv2.imshow("Live",img)
        cv2.waitKey(500)
        count+=1
        #cap.release()
        #cv2.destroyAllWindows()
        #break;
    #image=cv2.imread('IMAGES.jpg',0)
    #nump=np.asarray(image)
    #reader = easyocr.Reader(['en'])
    #result = reader.readtext(nump)
    #print(result)
