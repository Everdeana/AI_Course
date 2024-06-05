from cvzone.HandTrackingModule import HandDetector
import cv2

# 카메라 가동
cap = cv2.VideoCapture(0)

# 얼굴 인식 함수 호출
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
            break
			
    

    cv2.imshow('Hand view', img)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


