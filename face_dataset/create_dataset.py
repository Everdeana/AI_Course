import os
import pandas as pd
import shutil

# 데이터 불러오기
def createFolder(dir):
    try:
        if not os.path.exists(dir): # T/F
            os.makedirs(dir)
    except OSError:
        print("Error : " + OSError)

#원본 디렉토리에 파일 불러오기
orgPath = "./org_data"
file_list = os.listdir(orgPath)
print(file_list)

# Dataset Directory 만들기
createFolder("./dataset")


# 디렉토리 생성
for file in file_list:
    # print(file)
    # 문장 분리
	spFile = file.split('_')
	print("순번 : ", spFile[0])
	print("한글이름 : ", spFile[1])
	print("영문이름 : ", spFile[2])
	
	# 폴더 생성
	createFolder(f"./dataset/{spFile[2]}")