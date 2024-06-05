from cvzone.PoseModule import PoseDetector
import cv2

# 카메라 가동
cap = cv2.VideoCapture(0)

# 포즈 설정
detector = PoseDetector(
	staticMode		   = False,
	modelComplexity	   =1,
	smoothLandmarks	   =True,
	enableSegmentation = False,
	smoothSegmentation = True,
	detectionCon	   =0.5,
	trackCon		   =0.5
)

while True:
    ret, frame = cap.read()
    
    img = detector.findPose(frame)
    
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)
    
    print(lmList)
    print(bboxInfo) # 음수는 3차원 좌표
    
    cv2.imshow('pose', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()