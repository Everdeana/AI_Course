# 라이브러리 불러오기
import os
import numpy as np
from PIL import Image # pillow : 이미지 처리 라이브러리
import faiss
import face_recognition

# 디렉토리 처리하는 함수
# 데이터 불러오기
def createFolder(dir):
    try:
        if not os.path.exists(dir): # T/F
            os.makedirs(dir)
    except OSError:
        print("Error : " + OSError)

# 디렉토리에 있는 파일을 불러오는 함수
def read_file(path):
    img_path = []
    # 데이터 가져오기
    for paths, subdirs, files in os.walk(path): # 디렉토리, 파일 탐색 -> 현재 디렉토리의 하부 파일을 전부 가져옴
        print('paths = ', paths)
        print('subdirs = ', subdirs)
        print('files = ', files)
        print('#'*70)

        # 파일명을 변수에 넣기
        for name in files:
            img_path.append(os.path.join(paths, name))

    return img_path
# 학습 데이터 전처리
train_images = read_file('./org_data')
# print(train_image)
print('-' * 50)
print('학습할 데이터 파일 경로')
for data in train_images:
    print(data)
    
print('-' * 50)

# 불러온 이미지에서 얼굴만 추출
# 1개를 먼저 처리 후 이상이 없으면 for
for path_img in train_images: # for문으로 감싸기 전에 테스트 1번 한 후에 감싸기
	# path_img = train_images[0]

	# numpy 형태로 변환(이미지 -> 숫자)
	img = face_recognition.load_image_file(path_img)
	# print(img)
	# print(img.shape)

	# 얼굴 검출
	img_face = face_recognition.face_locations(img) # 얼굴을 검출한 후 사진을 분리할 때 약간의 공간을 주고 분리해야 한다.
	print(path_img, len(img_face), img_face)

	# 찾은 얼굴을 Crop 처리 # 특정 부분을 자름
	'''
	# <방법 1>
	# if len(img_face) > 0:
	#     if len(img_face) > 1:
	#         print("한 명 이상의 이미지가 검출되었습니다.")
	#         exit()
	'''
	'''
	# <방법 2>
	# if len(img_face) == 0 or len(img_face) > 1:
	#         print("얼굴이 한 명만 검출되어야 합니다.")
	#         exit()
	'''

	# <방법 3>
	if len(img_face) != 1:
			print("얼굴이 한 명만 검출되어야 합니다.")
			exit()

	# 좌표
	top, right, bottom, left = img_face[0]# 이미지의 좌표를 시계방향으로 가져옴
	print('top = ', top)
	print('right = ', right)
	print('bottom = ', bottom)
	print('left = ', left)

	# line 52 -> 이미지 공백 포함해서 자르기
	# top -> 빼야 공간이 생김 -> 좌표가 위로 올라감
	# right -> 더해야 공간이 생김 -> 좌표가 오른쪽으로 감
	top = top - 20
	right = right + 20
	bottom = bottom + 20
	left = left - 20

	# 자르기
	# numpy slicing 할 때
	face_img = img[top:bottom, left:right] # top부터 bottom까지, left부터 right까지 이미지를 자름

	# 얼굴 저장
	# https://supermemi.tistory.com/entry/Python-PIL-PIL-%EC%9D%B4%EB%AF%B8%EC%A7%80-Numpy-%EB%B0%B0%EC%97%B4-%EB%B3%80%ED%99%98-%EB%B0%8F-%EC%A0%80%EC%9E%A5-Imagefromarray-nparray-npasarray
	pil_img = Image.fromarray(face_img) # pillow 사용
	pil_img.save('cut_img.jpg') # 메모리에 있는걸 저장할 때 -> .save

	# 저장하기
	# face_save = path_img
	# print("원본이미지 = ", )

	path = path_img
	dir_path = os.path.dirname(path)
	file_name = os.path.basename(path)

	# 윈도우에서만 사용 가능
	# print("dir_path = ", dir_path.split('\\')[-1])
	# print("file_name = ", file_name)

	# 경로 지정 통일 -> 1줄로 처리
	# dir_path = dir_path.replace('\\', '/')
	# print("dir_path = ", dir_path.split('/')[-1].split('_')[-1]) # 영어 이름만 추출하기 위해서
	# print("file_name = ", file_name)

	# 경로 지정 통일 -> 변수에 저장하여 처리
	dir_path = dir_path.replace('\\', '/')
	dir_path = dir_path.split('/')[-1].split('_')[-1]
	print("dir_path = ", dir_path) # 영어 이름만 추출하기 위해서
	print("file_name = ", file_name)



	# dataset 경로
	save_path = f'./dataset/{dir_path}/{file_name}'
	print(save_path)
	pil_img.save(save_path)


