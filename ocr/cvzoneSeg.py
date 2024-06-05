import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cv2

# 카메라 가동
cap = cv2.VideoCapture(0)

segmentor = SelfiSegmentation(model = 0)

while True:
    ret, frame = cap.read()
    
    imgOut = segmentor.removeBG(frame, imgBg=(255, 255, 255), cutThreshold=0.5)
    
    imgStacked = cvzone.stackImages([frame, imgOut], cols=2, scale=1)
    
    cv2.imshow('seg1', frame)
    cv2.imshow('seg2', imgOut)
    cv2.imshow('seg3', imgStacked)
    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()