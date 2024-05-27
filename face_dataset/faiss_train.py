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
print("faceEncode : ", type(faceEncode))
print("train_labels : ", type(train_labels))


    

# 128bit vector encoding