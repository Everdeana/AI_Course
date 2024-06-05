from cvzone.HandTrackingModule import HandDetector
import cv2

# 카메라 가동
cap = cv2.VideoCapture(0)

# 손 인식 함수 호출
detector = HandDetector(
	staticMode 		= False,
	maxHands		= 2,
	modelComplexity = 1, 
	detectionCon	= 0.5,
	minTrackCon		= 0.5
)

while True:
    rtn, frame = cap.read()

    hands, img = detector.findHands(frame, draw=True, flipType=True)
    
    if hands:
        for hand in hands:
            print(hand)
            # break
            handpoint = hand['lmList']
            handtype = hand['type']
            
            print("손위치 : ", handtype)
            
            point4 = handpoint[4]
            point8 = handpoint[8]
            
            print(point4, point8)
            
            length, info, img = detector.findDistance(point4[:2], point8[:2], img, color = (0, 0, 255), scale = 10)
            print('distance = ', length)

    cv2.imshow('Hand view', img)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


