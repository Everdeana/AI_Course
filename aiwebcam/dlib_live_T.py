import dlib
import cv2
import os

class FaceDetector:
    def __init__(self, detector_path, predictor_path):
        self.detector = dlib.get_frontal_face_detector()
        if not os.path.exists(predictor_path):
            raise FileNotFoundError(f"File '{predictor_path}' not found.")
        self.predictor = dlib.shape_predictor(predictor_path)
        self.image = None
        self.detections = None

    def load_image(self, image):
        self.image = image

    def detect_faces(self, upsample_num_times=1):
        if self.image is None:
            raise ValueError("Image not loaded.")
        self.detections = self.detector(self.image, upsample_num_times)

    def draw_faces(self):
        if self.detections is None:
            raise ValueError("No faces.")
        for det in self.detections:
            x, y, w, h = det.left(), det.top(), det.width(), det.height()
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 실시간 영상에서 얼굴 검출 예시
if __name__ == "__main__":
    predictor_path = os.path.abspath("./aicctv/trained/shape_predictor_68_face_landmarks.dat")

    face_detector = FaceDetector(detector_path="", predictor_path=predictor_path)

    # 영상 소스 가져오기 (카메라를 사용)
    cap = cv2.VideoCapture(0)

    # 카메라 크기 조정
    cap.set(3, 1280)
    cap.set(4, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 원본 영상 (좌우 반전)
        frame = cv2.flip(frame, 1)
        
        # Dlib을 사용하여 얼굴 검출
        face_detector.load_image(frame)
        face_detector.detect_faces()

        # 얼굴을 프레임에 그림
        face_detector.draw_faces()

        # OpenCV를 사용하여 원본 영상 표시
        cv2.imshow('camera', frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
