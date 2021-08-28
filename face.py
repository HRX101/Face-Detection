import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
img1=cv2.imread('face.jpg',1)
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.5,35)
for(x,y,w,h) in faces:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img1)
cv2.waitKey() 