import numpy as np 
import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
def fuck():
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
            cv2.putText(frame,"face",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)
            roi_gray=gray[y:y+w,x:x+w]
            roi_color=frame[y:y+h,x:x+h]
            eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
            smile=smile_cascade.detectMultiScale(roi_gray,1.5,35)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),5)
                cv2.putText(roi_color,"eyes",(ex,ey),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
            for (x1,y1,w1,h1) in smile:
                cv2.rectangle(roi_color,(x1,y1),(x1+w1,y1+h1),(0,255,0),5)
                cv2.putText(roi_color,"smile",(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
                    
        
        cv2.imshow('face-detection',frame)
        if cv2.waitKey(1)==ord('a'):
            break

    cap.release()
    cv2.destroyAllWindows()