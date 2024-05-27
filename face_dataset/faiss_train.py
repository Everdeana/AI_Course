###########################################################
# 프로그램명 : dlib 라이브러리를 이용한 face 추출 프로그램(dataset)
# 개발일자 : 2024년 05월 27일
# 개발버젼 : v 1.1.2
# 개발자명 : 장국진
# 라이브러리 : face recognition, dlib, faiss-cpu:1.7.3
##########################################################

# 라이브러리 불러오기
import os
import numpy as np
from PIL import Image # pillow : 이미지 처리 라이브러리
import faiss
import face_recognition

def read_file(path):
    img_path = []
    # 데이터 가져오기
    for paths, subdirs, files in os.walk(path): # 디렉토리, 파일 탐색 -> 현재 디렉토리의 하부 파일을 전부 가져옴
        # print('paths = ', paths)
        # print('subdirs = ', subdirs)
        # print('files = ', files)
        # print('#'*70)

        # 파일명을 변수에 넣기
        for name in files:
            img_path.append(os.path.join(paths, name))

    return img_path

# 전처리된 데이터 불러오기
dataset_imgs = read_file('./dataset')

print('-' * 50)
print('데이터셋 경로')
for data in dataset_imgs:
    print(data)
    
print('-' * 50)

# faiss에 얼굴 정보를 등록하고 벡터DB로 변환
faceEncode = []
img_paths = []

for path in dataset_imgs:
    path = path.replace('\\', '/')
    print(path)
    # 얼굴 이미지 불러오기
    img = face_recognition.load_image_file(path)
    # print(img)
	# Encode
    face_encode = face_recognition.face_encodings(img)[0]
    # print(face_encode)
    # exit() # 테스트용(1번만 실행)
	
	# Encoding 된 정보를 변수에 저장\
    faceEncode.append(face_encode)
    img_paths.append(path)
    
print("검출된 얼굴은 총 {}개 입니다.".format(len(faceEncode)))

# 인코딩 (벡터DB)로 생성
# 인코딩(문제 : numpy형식, 답 : numpy형식 필요)
# 람다함수로 처리
train_labels = np.array(
    [img.split('/')[-2] for img in img_paths] # 경로 출력
)

# print(train_labels)
# 데이터 구조 확인
print("faceEncode : ", type(faceEncode)) # <class 'list'>
print("train_labels : ", type(train_labels)) # <class 'numpy.ndarray'>

# 인코딩 위한 변환 작업
faceEncode = np.array(faceEncode, dtype=np.float32)
print(faceEncode.shape, train_labels.shape) # (102, 128) (102,)

# Vector DB로 저장
face_index = faiss.IndexFlatL2(128) # faiss 엔진에 방금 위에서 확인한 구조(128)로 저장

# 가장 가까운 위치에 있는 값을 계싼 -> 거리가 멀어지면 unknown처리
# 벡터 적용
# 총 5개의 인덱스 검출
face_index.add(faceEncode)

# 예측하기
# 얼굴 인식
test_img = face_recognition.load_image_file('test_img/city.jpg')
test_face = face_recognition.face_locations(test_img)
if len(test_face) != 1:
    print("테스트 얼굴에 1개의 얼굴만 존재해야 합니다.")
    exit()
    
# 얼굴만 잘라내기(시계방향)
top, right, bottom, left  = test_face[0]
print(top, right, bottom, left)

# 범위 확장
top -= 20
right += 20
bottom += 20
left -= 20

# 얼굴 부붐만 추출
face_cut = test_img[top:bottom, left:right]

# Encoding
test_en = face_recognition.face_encodings(face_cut)[0]
print(type(test_en))

# numpy로 변환
test_en = np.array(test_en, dtype=np.float32).reshape(-1, 128) # .reshape(-1, 128) ====> (128) -> (101, 128)

######예측하는 부분##########################################################################################################################

# 예측
val, result = face_index.search(test_en, k=5) # faiss 엔진에서 test_en에 가장 근접한 5개 추출

# 값 검풀
label = [train_labels[i] for i in result[0]]
print(label)

############################################################################################################################################
# 128bit vector encoding