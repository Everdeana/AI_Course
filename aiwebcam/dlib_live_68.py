import cv2  
import dlib  
from functools import wraps  
from scipy.spatial import distance  
import time  
import os


cap = cv2.VideoCapture(0) 

lastsave = 0  

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])  
    B = distance.euclidean(eye[2], eye[4])  
    C = distance.euclidean(eye[0], eye[3])  
    ear_aspect_ratio = (A+B)/(2.0*C)  
    return ear_aspect_ratio

hog_face_detector = dlib.get_frontal_face_detector()  
# dlib_facelandmark = dlib.shape_predictor("./trained/shape_predictor_68_face_landmarks.dat")  

# 현재 스크립트 파일의 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.realpath(__file__))
# shape_predictor_68_face_landmarks.dat 파일의 절대 경로를 만듭니다.
model_path = os.path.join(current_dir, 'trained', 'shape_predictor_68_face_landmarks.dat')

# 절대 경로를 사용하여 모델 파일을 엽니다.
dlib_facelandmark = dlib.shape_predictor(model_path)


def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1  
        time.sleep(0.05)  
        global lastsave  
        if time.time() - lastsave > 5:  
            lastsave = time.time()  
            tmp.count = 0  
        return func(*args, **kwargs)  
    tmp.count = 0  
    return tmp  

@counter  
def close():
    cv2.putText(frame, "Eyes Closed!!!!!!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)  

while True:
    _, frame = cap.read()  
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    faces = hog_face_detector(gray)  
    for face in faces:  
        x, y, w, h = face.left(), face.top(), face.width(), face.height()  # 얼굴 좌표 추출
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 바운딩 박스 그리기

        face_landmarks = dlib_facelandmark(gray, face)  

        for n in range(0, 68):
            x = face_landmarks.part(n).x  
            y = face_landmarks.part(n).y  
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        leftEye = []  
        rightEye = []  

        for n in range(36,42):  
            x = face_landmarks.part(n).x  
            y = face_landmarks.part(n).y  
            leftEye.append((x,y))  
            next_point = n+1  
            if n == 41:  
                next_point = 36  
            x2 = face_landmarks.part(next_point).x  
            y2 = face_landmarks.part(next_point).y  
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)  

        for n in range(42,48):  
            x = face_landmarks.part(n).x  
            y = face_landmarks.part(n).y  
            rightEye.append((x,y))  
            next_point = n+1  
            if n == 47:  
                next_point = 42  
            x2 = face_landmarks.part(next_point).x  
            y2 = face_landmarks.part(next_point).y  
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)  

        left_ear  = calculate_EAR(leftEye)  
        right_ear = calculate_EAR(rightEye)  

        EAR = (left_ear+right_ear)/2  
        EAR = round(EAR,2)  

        if EAR<0.19:  
            close()  
            print(f'close count : {close.count}')  
            if close.count == 1:  
                print("Eyes Closed!")  
                
            elif close.count >= 4:  
                print("Eyes Closed!!!!!!")  
        		# print(EAR)  

    cv2.imshow("dlib Camera Test", frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()  
