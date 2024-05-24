import os
import pandas as pd
import shutil
from datetime import datetime

# 오늘 날짜, 시간 구하기
nowDate = datetime.today().strftime("%Y%m%d_%H%M%S")

print(nowDate)

os.rename('./dataset', f'./dataset_{nowDate}')

# 데이터 불러오기
def createFolder(dir):
    try:
        if not os.path.exists(dir): # T/F
            os.makedirs(dir)
    except OSError:
        print("Error : " + OSError)

#원본 디렉토리에 파일 불러오기
orgPath = "./org_data"
fileList = os.listdir(orgPath)
# print(fileList)

# Dataset Directory 만들기
createFolder("./dataset")

dataset_labels = {}  # Initialize an empty dictionary

# 파일 생성
saveFile = open('./dataset/labels.txt', 'w', encoding='utf8')

# 디렉토리 생성 함수
for file in fileList:
    # print(file)
    # 문장 분리
	spFile = file.split('_')
	print("순번 : ", spFile[0])
	print("한글이름 : ", spFile[1])
	print("영문이름 : ", spFile[2])
	
	# 폴더 생성
	createFolder(f"./dataset/{spFile[2]}")
    
	# 라벨만들기
	dataset_labels[spFile[2]] = spFile[1]
    # 파일 저장

	print(f'{spFile[2]}, {spFile[1]}', file=saveFile)

# 데이터셋 딕셔너리
print(dataset_labels)
saveFile.close()

# 원본파일 Dataset에 처리하는 루틴
#원본 디렉토리에 파일 불러오기
orgPath = "./org_data"
fileList = os.listdir(orgPath)
for dir in fileList:
    files = os.listdir(orgPath + f'/{dir}')
    print('*'*100)
    print(dir)
    print('*'*100)
    print(files)
