from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

# 카메라 가동
cap = cv2.VideoCapture(0)

# 얼굴 인식 함수 호출
detector = FaceMeshDetector(
	staticMode 		= False,
	maxFaces		= 2,
	minDetectionCon = 0.5, 
	minTrackCon		= 0.5
)

while True:

	rtn, frame = cap.read()

	img, faces = detector.findFaceMesh(frame, draw=True)
	print(len(faces))

	# 얼굴이 있다면
	if faces:
		for face in faces:
			# print(face) # mash
			leftEyeUpPoint = face[159]
			leftEyeDownPoint = face[23]

			leftEyeVerticalDistance, info = detector.findDistance(leftEyeUpPoint, leftEyeDownPoint)

			print(leftEyeVerticalDistance)

	cv2.imshow('window', img)

	if cv2.waitKey(1) == ord('q'):
		break

cv2.destroyAllWindows()