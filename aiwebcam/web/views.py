from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

# OpenCV 라이브러리 불러오기
import cv2
# import dlib  
# from functools import wraps  
# from scipy.spatial import distance  
# import time  

def video_feed(request):  # stream 함수를 streaming
	return StreamingHttpResponse(stream(), content_type = 'multipart/x-mixed-replace;boundary=frame') # content_type = 전송 규격

# Create your views here.

# 얼굴 인식 처리

# 영상을 보내는 함수
def stream():
	cap = cv2.VideoCapture(0)

	while True:
		ret, frame = cap.read()
		if not ret:
			print("카메라를 인식할 수 없습니다.")
			break

		# 서버로 데이터를 전송
		# 이미지를 binary WEB에서 전송 가능한 형태
		image_bytes = cv2.imencode('.jpg', frame)[1].tobytes() # . --> 히든파일

		# 서버로 전송 - yield : 공백일 떄까지 계속 실행
		yield(b'--frame\r\n'
		b'Content-type:image/jpeg\r\n\r\n'
		+ image_bytes + b'r\n')  # b = binary


def index(request): # web 함수는 request 필수
	# return HttpResponse("Web Main Page ")
	return render(request, 'webcam_main.html')