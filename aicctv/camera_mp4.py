# 라이브러리 불러오기
import cv2


# 영상 불러오기
cap = cv2.VideoCapture("Alessandro Nesta.mp4") 
# 실시간으로 계속 영상 받기

while True:

    _, frame = cap.read()  # 비디오 프레임 읽기
    
	# 프레임 정보
    pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    frame_count =  cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("현재진행프레임 : ", pos_frame)
    cv2.putText(frame, str(pos_frame), (20, 700), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)  # 화면에 DROWSY 텍스트를 표시합니다.
    cv2.putText(frame, str(frame_count), (1000, 700), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)  # 화면에 DROWSY 텍스트를 표시합니다.
	

    print("현재전체프레임 : ", frame_count)
    

    cv2.imshow('camera', frame)
    
	# 흑백 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 회색조로 이미지 변환
    
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()  # 카메라 객체 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
