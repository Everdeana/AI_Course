# 라이브러리 불러오기
import os
import numpy as np
from PIL import Image
import faiss
import face_recognition

# 디렉토리 처리하는 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("에러 : 디렉토리 생성에러. " + directory)

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

# 학습데이터 전처리
train_images = read_file('./org_data')
# print(train_images)
print('-' * 50)
print('학습할 데이터 파일 경로')
print('-' * 50)
for data in train_images:
    print(data)
print('-' * 50)

# 불러온 이미지에서 얼굴만 추출
# 1개를 먼저 처리 후 이상이 없으면 for
for path_img in train_images:
    # numpy 형태로 변환( 이미지 -> 숫자로)
    img = face_recognition.load_image_file(path_img)
    # print(img)
    # print(img.shape)

    # 얼굴 검출
    img_face = face_recognition.face_locations(img)
    print(path_img, len(img_face), img_face)

    # 찾은 얼굴을 Crop 처리
    if len(img_face) != 1:
        print("얼굴이 한명만 검출되어야 합니다.")
        exit()

    # 좌표
    top, right, bottom, left = img_face[0]
    print('top =', top)
    print('right =', right)
    print('bottom =', bottom)
    print('left =', left)
    top = top - 20
    right = right + 20
    bottom = bottom + 20
    left = left - 20

    # numpy slicing 할때
    face_img = img[top:bottom, left:right]
    # 얼굴저장(잘라진 이미지 파일을 불러온것과 같은 효과)
    pil_img = Image.fromarray(face_img)
    # pil_img.save('cut_img.jpg')

    # 저장하기
    path = path_img
    dir_path = os.path.dirname(path)
    file_name = os.path.basename(path)
    # 경로 지정 통일
    dir_path = dir_path.replace('\\', '/')
    dir_path = dir_path.split('/')[-1].split('_')[-1]
    print("dir_path =", dir_path)
    print("file_name =", file_name)

    # dataset 경로
    save_path = f'./dataset/{dir_path}/{file_name}'
    print(save_path)
    pil_img.save(save_path)
