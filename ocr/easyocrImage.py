import easyocr
import cv2
import numpy as np

# 이미지 불러와서 전처리
imgFile = './test_data/car1.jpg'
org_img = cv2.imread(imgFile, cv2.IMREAD_COLOR)
gray_image = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

def onChange(pos):
	pass

# 트랙바 만들기
winnames = 'TrackBar'
cv2.namedWindow(winnames)
cv2.imshow('org_img', org_img)
cv2.createTrackbar('threshold', winnames, 127, 255, onChange)

# 트랙바 제어
while cv2.waitKey(1) != ord('q'):
	pos = cv2.getTrackbarPos('threshold', winnames)
	ret, binary = cv2.threshold(gray_image, pos, 255, cv2.THRESH_BINARY)
	# cv2.imshow('gray_img', gray_image)
	# cv2.waitKey(0)
	# cv2.imshow('winnames', binary) # 트랙바 창 따로
	cv2.imshow(winnames, binary) # 이미지 창에 트랙바

	if cv2.waitKey(1) == ord('s'):
		cv2.imwrite('./test_data/car_bin.jpg', binary)
		
cv2.destroyAllWindows()