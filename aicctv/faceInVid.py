# 라이브러리 불러오기
import cv2  
import dlib  
from functools import wraps  
from scipy.spatial import distance  # 거리 계산을 위한 scipy 라이브러리 distance 모듈

import time  

# 영상 불러오기
cap = cv2.VideoCapture("Alessandro Nesta.mp4") 
'''
cap1 = cv2.VideoCapture(1) # 카메라 1개 -> 0 / 카메라 2개 -> 1 / ...
cap2 = cv2.VideoCapture(2) 
cap3 = cv2.VideoCapture(3) 
'''

lastsave = 0  # 마지막으로 저장된 시간 초기화

#########################################################################################################################################################
def calculate_EAR(eye):  # 눈 거리를 계산하는 함수 정의
    A = distance.euclidean(eye[1], eye[5])  # 왼쪽 눈의 세로 길이 계산
    B = distance.euclidean(eye[2], eye[4])  # 왼쪽 눈의 가로 길이 계산
    C = distance.euclidean(eye[0], eye[3])  # 눈의 대각선 길이 계산
    ear_aspect_ratio = (A+B)/(2.0*C)  # 눈의 EAR(Eye Aspect Ratio) 계산
    return ear_aspect_ratio

# dlib 인식 모델 정의
hog_face_detector = dlib.get_frontal_face_detector()  # dlib 얼굴 탐지 모델 로드
dlib_facelandmark = dlib.shape_predictor("./trained/shape_predictor_68_face_landmarks.dat")  # dlib 얼굴 특징점 예측 모델 로드

def counter(func):  # 함수 실행 횟수를 계산하는 데코레이터 정의
    @wraps(func)  # 데코레이터를 사용하여 함수의 메타데이터 보존
    def tmp(*args, **kwargs):
        tmp.count += 1  # 함수 호출 횟수 증가
        time.sleep(0.05)  # 0.05초 대기
        global lastsave  # 전역 변수 사용을 위해 global 키워드 사용
        if time.time() - lastsave > 5:  # 5초 이상 경과하면
            lastsave = time.time()  # 현재 시간을 저장
            tmp.count = 0  # 함수 호출 횟수 초기화
        return func(*args, **kwargs)  # 데코레이트된 함수 반환
    tmp.count = 0  # 함수 호출 횟수 초기화
    return tmp  # 데코레이터 함수 반환

@counter  # 카운터 데코레이터를 사용하여 close 함수 데코레이션
def close():
    cv2.putText(frame, "Eyes Closed!!!!!!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)  # 화면에 텍스트 표시
#########################################################################################################################################################

# 카메라 크기 조정
# width : 3, height : 4
cap.set(3, 1280)
cap.set(4, 720)

# 실시간으로 계속 영상 받기
while True:

    _, frame = cap.read()  # 비디오 프레임 읽기

	# 원본 영상
    frame = cv2.flip(frame, 1)

    # cv2.imshow('camera', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 회색조로 이미지 변환
    # cv2.imshow('gray', gray)
    
    faces = hog_face_detector(gray)  # 얼굴 검출
    for face in faces:  # 검출된 얼굴에 대해 반복
        face_landmarks = dlib_facelandmark(gray, face)  # 얼굴 특징점 검출
        leftEye = []  # 왼쪽 눈 특징점 초기화
        rightEye = []  # 오른쪽 눈 특징점 초기화

        for n in range(36,42):  # 오른쪽 눈 특징점을 반복하여 추가
            x = face_landmarks.part(n).x  # 특징점의 x 좌표
            y = face_landmarks.part(n).y  # 특징점의 y 좌표
            leftEye.append((x,y))  # 왼쪽 눈의 특징점 리스트에 추가
            next_point = n+1  # 다음 특징점의 인덱스
            if n == 41:  # 마지막 특징점이면
                next_point = 36  # 다음 특징점을 첫 번째 특징점으로 설정
            x2 = face_landmarks.part(next_point).x  # 다음 특징점의 x 좌표
            y2 = face_landmarks.part(next_point).y  # 다음 특징점의 y 좌표
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)  # 눈 주변에 선 그리기

        for n in range(42,48):  # 왼쪽 눈 특징점을 반복하여 추가
            x = face_landmarks.part(n).x  # 특징점의 x 좌표
            y = face_landmarks.part(n).y  # 특징점의 y 좌표
            rightEye.append((x,y))  # 오른쪽 눈의 특징점 리스트에 추가
            next_point = n+1  # 다음 특징점의 인덱스
            if n == 47:  # 마지막 특징점이면
                next_point = 42  # 다음 특징점을 첫 번째 특징점으로 설정
            x2 = face_landmarks.part(next_point).x  # 다음 특징점의 x 좌표
            y2 = face_landmarks.part(next_point).y  # 다음 특징점의 y 좌표
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)  # 눈 주변에 선 그리기

        left_ear  = calculate_EAR(leftEye)  # 왼쪽 눈의 EAR 계산
        right_ear = calculate_EAR(rightEye)  # 오른쪽 눈의 EAR 계산

        EAR = (left_ear+right_ear)/2  # 양쪽 눈의 EAR 평균 계산
        EAR = round(EAR,2)  # EAR 값을 소수점 둘째 자리까지 반올림

        if EAR<0.19:  # EAR 값이 임계값보다 작으면
            close()  # 눈을 감지한 횟수 증가 및 DROWSY 텍스트 표시
            print(f'close count : {close.count}')  # 눈을 감지한 횟수 출력
            if close.count == 1:  # 눈을 감지한 횟수가 1번이면
                print("Eyes Closed!")  # 운전자가 졸고 있는 상태로 판단
                
            elif close.count >= 4:  # 눈을 감지한 횟수가 4번이면
                print("Eyes Closed!!!!!!")  # 운전자가 졸고 있는 상태로 판단
        print(EAR)  # EAR 값을 출력

    cv2.imshow("Face In mp4", frame)  # 비디오 프레임 출력

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # 카메라 객체 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기