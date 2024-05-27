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
dataset_img = read_file('./dataset')

print('-' * 50)
print('데이터셋 경로')
for data in dataset_img:
    print(data)
    
print('-' * 50)

# faiss에 얼굴 정보를 등록하고 벡터DB로 변환
