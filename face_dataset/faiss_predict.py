# 라이브러리 불러오기
import os
import numpy as np
from PIL import Image
import faiss
import face_recognition

################################################
# labels
################################################
# 디렉토리에 있는 파일을 불러오는 함수
def read_file(path):
    img_path = []
    # 데이터 가져오기
    for paths, subdirs, files in os.walk(path):
        # print('paths =', paths)
        # print('subdirs =', subdirs)
        # print('files =', files)

        # 파일명을 변수에 넣기
        for name in files:
            img_path.append(os.path.join(paths, name))

    return img_path

# 벡터 DB 불러오기
face_index = faiss.read_index('./train/face_20240527.bin')

# 정답 불러오기
dataset_imgs = read_file('./dataset')

img_paths = []
for path in dataset_imgs:
    path = path.replace('\\', '/')
    img_paths.append(path)

# 람다함수
train_labels = np.array(
    [img.split('/')[-2] for img in img_paths]
)

# 예측하기
# 얼굴인식
test_img = face_recognition.load_image_file('test_img/city.jpg')
test_face = face_recognition.face_locations(test_img)
if len(test_face) != 1:
    print("테스트 얼굴에 1개의 얼굴만 존재해야 합니다.")
    exit()

# 얼굴만 잘라내기(시계방향)
top, right, bottom, left = test_face[0]
print(top, right, bottom, left)

# 범위 확장
top = top - 20
right = right + 20
bottom = bottom + 20
left = left - 20

# 얼굴부분만 추출
face_cut = test_img[top:bottom, left:right]

pil_img = Image.fromarray(face_cut)
pil_img.save('./train_res/test.jpg')
img = face_recognition.load_image_file('./train_res/test.jpg')

# 인코딩
test_en = face_recognition.face_encodings(img)[0]

# 넘파이
test_en = np.array(test_en, dtype=np.float32).reshape(-1, 128)
# (128) -> (1, 128)

# 예측
val, result = face_index.search(test_en, k=5)

# 값검출
label = [train_labels[i] for i in result[0]]
print(label)

