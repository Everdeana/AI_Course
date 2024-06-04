import easyocr
import cv2
import numpy as np

# 전역 변수
pointList = []
gl_areaCut = False

# 이미지 불러와서 전처리
imgFile = './test_data/car4.jpg'
org_image = cv2.imread(imgFile, cv2.IMREAD_COLOR)
gray_image = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

def onChange(pos):
	pass

# 좌표를 그리는 함수
def pointDraw():
	global gl_areaCut

	tmpImg = org_image.copy()

	i = 0

	for data in pointList:
		cv2.circle(tmpImg, data, 10, (0, 0, 255), cv2.FILLED)
	
	return tmpImg


def mouse_handler(event, x, y, flags, param): # event = 마우스가 누른 것
	if event == cv2.EVENT_RBUTTONDOWN: # 마우스 올리면 -> UP / 마우스 클릭 하면 -> Down
		print("오른쪽 버튼")
		print("-"*50)
		print(f'x = {x}, y = {y}')
		print("-"*50)
		pointList.append([x, y])
		print(pointList)
	if event == cv2.EVENT_LBUTTONDOWN:
		print("왼쪽 버튼")
		print("-"*50)
		print(f'x = {x}, y = {y}')
		print("-"*50)
		pointList.pop()
		print(pointList)
	# print('x = ', x)
	# print('y = ', y)

	# 드로우로 그림그리기
	cv2.imshow('org_img', pointDraw())

# 트랙바 만들기
winnames = 'TrackBar'
cv2.namedWindow(winnames)
cv2.imshow('org_img', org_image)
cv2.createTrackbar('threshold', winnames, 127, 255, onChange)

# 이미지 검출(마우스 제어)
cv2.setMouseCallback('org_img', mouse_handler)


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

	if cv2.waitKey(1) == ord('S'):
		cv2.imwrite('./test_data/car_bin1.jpg', binary)
		
cv2.destroyAllWindows()