# 라이브러리 불러오기
import cv2


# 영상 불러오기
cap = cv2.VideoCapture(0) 
'''
cap1 = cv2.VideoCapture(1) # 카메라 1개 -> 0 / 카메라 2개 -> 1 / ...
cap2 = cv2.VideoCapture(2) 
cap3 = cv2.VideoCapture(3) 
'''

# 카메라 크기 조x정
# width : 3, height : 4
cap.set(3, 1280)
cap.set(4, 720)

# 실시간으로 계속 영상 받기

while True:

    _, frame = cap.read()  # 비디오 프레임 읽기
    cv2.imshow('camera', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 회색조로 이미지 변환
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # 카메라 객체 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
