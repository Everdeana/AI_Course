from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
import cv2
import dlib
from scipy.spatial import distance
import time
import os
from functools import wraps

# 사용할 테이블 설정
from .models import WebUser # 현재 위치의 WebUser

class BlinkDetector:
    def __init__(self):
        self.lastsave = 0
        self.hog_face_detector = dlib.get_frontal_face_detector()
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.model_path = os.path.join(self.current_dir, 'shape_predictor_68_face_landmarks.dat')
        if not os.path.exists(self.model_path):
            raise RuntimeError(f"Unable to open {self.model_path}")
        self.dlib_facelandmark = dlib.shape_predictor(self.model_path)
        self.close_count = 0

    def calculate_EAR(self, eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear_aspect_ratio = (A + B) / (2.0 * C)
        return ear_aspect_ratio

    def counter(func):
        @wraps(func)
        def tmp(self, *args, **kwargs):
            tmp.count += 1
            time.sleep(0.05)
            if time.time() - self.lastsave > 5:
                self.lastsave = time.time()
                tmp.count = 0
            return func(self, *args, **kwargs)
        tmp.count = 0
        return tmp

    @counter
    def close(self, frame):
        cv2.putText(frame, "Eyes Closed!!!!!!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)

    def detect_and_draw_landmarks(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.hog_face_detector(gray)
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_landmarks = self.dlib_facelandmark(gray, face)
            for n in range(0, 68):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            leftEye = [(face_landmarks.part(n).x, face_landmarks.part(n).y) for n in range(36, 42)]
            rightEye = [(face_landmarks.part(n).x, face_landmarks.part(n).y) for n in range(42, 48)]
            left_ear = self.calculate_EAR(leftEye)
            right_ear = self.calculate_EAR(rightEye)
            EAR = (left_ear + right_ear) / 2
            EAR = round(EAR, 2)
            if EAR < 0.19:
                self.close(frame)
        return frame

detector = BlinkDetector()

# 영상 스트림 생성 함수
def stream():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
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

    return HttpResponse('adduser 링크')