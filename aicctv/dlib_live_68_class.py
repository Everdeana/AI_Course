import cv2
import dlib
from functools import wraps
from scipy.spatial import distance
import time
import os

class BlinkDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.lastsave = 0
        self.hog_face_detector = dlib.get_frontal_face_detector()
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.model_path = os.path.join(self.current_dir, 'trained', 'shape_predictor_68_face_landmarks.dat')
        self.dlib_facelandmark = dlib.shape_predictor(self.model_path)

    def calculate_EAR(self, eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear_aspect_ratio = (A + B) / (2.0 * C)
        return ear_aspect_ratio

    def counter(func):
        @wraps(func)
        def tmp(*args, **kwargs):
            tmp.count += 1
            time.sleep(0.05)
            if time.time() - BlinkDetector.lastsave > 5:
                BlinkDetector.lastsave = time.time()
                tmp.count = 0
            return func(*args, **kwargs)
        tmp.count = 0
        return tmp

    @counter
    def close(self, frame):
        cv2.putText(frame, "Eyes Closed!!!!!!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)

    def run(self):
        while True:
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.hog_face_detector(gray)
            for face in faces:
                x, y, w, h = face.left(), face.top(), face.width(), face.height()  # 얼굴 좌표 추출
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 바운딩 박스 그리기

                face_landmarks = self.dlib_facelandmark(gray, face)

                for n in range(0, 68):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

                leftEye = []
                rightEye = []

                for n in range(36, 42):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    leftEye.append((x, y))
                    next_point = n + 1
                    if n == 41:
                        next_point = 36
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

                for n in range(42, 48):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    rightEye.append((x, y))
                    next_point = n + 1
                    if n == 47:
                        next_point = 42
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

                left_ear = self.calculate_EAR(leftEye)
                right_ear = self.calculate_EAR(rightEye)

                EAR = (left_ear + right_ear) / 2
                EAR = round(EAR, 2)

                if EAR < 0.19:
                    self.close(frame)
                    print(f'close count : {self.close.count}')
                    if self.close.count == 1:
                        print("Eyes Closed!")

                    elif self.close.count >= 4:
                        print("Eyes Closed!!!!!!")

            cv2.imshow("dlib Camera Test", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = BlinkDetector()
    detector.run()
