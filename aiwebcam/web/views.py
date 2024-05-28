from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
import cv2

# 사용할 테이블 설정
from .models import WebUser # 현재 위치의 WebUser

# 인공지능 faiss 라이브러리 호출
from faiss_predict import face_detect

from face_detector import BlinkDetector

detector = BlinkDetector()

# 영상 스트림 생성 함수
def stream(request):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라 인식 불가")
            break

        cv2.imwrite('./train/test.jpg', frame)
        print(face_detect('./train/test.jpg'))


        frame = detector.detect_and_draw_landmarks(frame)
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')

def index(request):
    return render(request, 'webcam_main.html')

def adduser(request):
    # DB에 자료 저장
    adduser=WebUser()
    adduser.names = '장국진'
    adduser.telnos = '010-1234-5678'
    adduser.save()

    return HttpResponse('adduser 등록')

def face_test(request):
    print(face_detect('./test_img/city.jpg'))
    return HttpResponse('face_test 함수')
