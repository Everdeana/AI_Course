import cv2
import dlib

cap = cv2.VideoCapture(0)

hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("./trained/shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = hog_face_detector(gray)
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face_landmarks = dlib_facelandmark(gray, face)

        # 여기서 얼굴 랜드마크를 사용하여 필요한 작업을 수행할 수 있습니다.

    cv2.imshow("dlib Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
