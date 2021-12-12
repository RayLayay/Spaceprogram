
import cv2 as cv

def face_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器
    face_detect = cv.CascadeClassifier('C:/Users/12562/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray,1.02,5,0,(50,50),(200,200))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color = (0,0,255),thickness=2)
    cv.imshow('result',img)

cap = cv.VideoCapture('2.gif')

while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(10):
        break

cv.destroyAllWindows()
cap.release()