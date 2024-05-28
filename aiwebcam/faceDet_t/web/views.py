from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

# opencv 라이브러리 불러오기
import cv2
import dlib
import matplotlib.patches as patches
import numpy as np

# 사용할 테이블 설정
from .models import WebUser

# 인공지능 faiss 라이브러리 호출
from faiss_predict import face_detect

# 오케
class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.image = None
        self.detections = None

    def load_image(self, image):
        self.image = image

    def detect_faces(self, upsample_num_times=1):
        if self.image is None:
            raise ValueError("Image not loaded.")
        self.detections = self.detector(self.image, upsample_num_times)
        return self.detections

    def draw_faces(self):
        if self.detections is None:
            raise ValueError("No faces.")
        for det in self.detections:
            x, y, w, h = det.left(), det.top(), det.width(), det.height()
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)

face_detector = FaceDetector()

def video_feed(request):
    return StreamingHttpResponse(stream(request),
    content_type='multipart/x-mixed-replace;boundary=frame')

# 영상을 보내는 함수
def stream(request):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 인식할 수 없습니다.")
            break

        # cv2.imwrite('./train/test.jpg', frame)        

        # 얼굴인식 처리
        # Dlib을 사용하여 얼굴 검출
        face_detector.load_image(frame)
        face_cnt = face_detector.detect_faces()

        if len(face_cnt) == 1:
            uname = face_detect(frame)

            if uname != "unknown":
                adduser = WebUser()
                adduser.names = uname
                adduser.telnos = '000-0000-0000'
                adduser.save()

        # 얼굴을 프레임에 그림
        face_detector.draw_faces()

        # 서버로 데이터를 전송
        # 이미지를 binary 웹에서 전송이 가능한 형태
        image_bytes = cv2.imencode('.jpg',frame)[1].tobytes()
        # 서버로 전송
        yield(b'--frame\r\n'
        b'Content-type:image/jpeg\r\n\r\n' + image_bytes
        + b'\r\n')

# Create your views here.
def index(request):
    return render(request, 'webcam_main.html')

def adduser(request):
    # 데이터베이스에 자료 저장
    # insert into WebUser (names, telnos) values (%s, %s)
    # ...
    adduser = WebUser()
    adduser.names = '홍길동'
    adduser.telnos = '000-0000-0000'
    adduser.save()
    return HttpResponse('adduser 등록')

def face_test(request):
    print(face_detect('./test_img/1.jpg'))
    return HttpResponse('face_test 함수')
