import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	
from PyQt5.QtGui import *
import os
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud as WC
from wordcloud import STOPWORDS

'''
import os

print(os.getcwd())
'''
'''
# 그래프 테스트
plt.plot([1, 2, 3, 4]) # 1차원 배열
lt.show()
'''
'''
# 그래프 테스트
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
'''

def clean_text(inputString):
    text_rmv = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’\'·]', ' ', inputString)
    return text_rmv

# 특정 경로에 있는 CSV파일만 불러오기
path = "./search_file/"# . <-- 자기 자신

# 워드 클라우드 자동 저장 함수
def wordCloudView():

	# listdir은 현재 경로에 있는 모든 파일을 확인
	file_list = os.listdir(path)
	print(file_list)
	# 디렉토리의 파일중에서 CSV 파일만 따로 배열로 처리 : 람다
	'''
	fileList = []
	for file in file_list:
	    
		if file.endswith('.csv'):
        	fileList.append(file)
		print(file_list)
	'''
	# 람다함수
	fileList1 = [file for file in file_list if file.endswith('.csv')]
		
	# 배열의 여러 csv 파일을 자동 병합해서 하나의 df 파일로 만드는 처리
	dfCsv = pd.DataFrame()
	for i in fileList1:
		data = pd.read_csv(path + i, encoding='cp949')
		dfCsv = pd.concat([dfCsv, data]) # 병합

	dfCsv = dfCsv.reset_index(drop = True) # 위에서 병합시 인덱스 재정렬이 필요함 ex)0123 0123 --> 0123 4567

	# drop : 특정 컬럼 삭제
	dfCsv = dfCsv.drop(['링크'], axis = 'columns') # DataFrame에서 링크를 제거 --> axis = 축
	# pandas 형식 --> list
	listCsv = dfCsv['제목'].astype(str).tolist()

	# 리스트의 문자열을 하나의 문자열로 만드는 방법
	# wordStr = ' '.join(word for word in listCsv)
	wordStr = ' '.join(listCsv)

	# 문자열 걸러내기
	wordStr = clean_text(wordStr)

	spwords = set(STOPWORDS)  # 제외할 단어
	spwords.add('AC밀란')  # 제외하고 싶은 단어 추가
	spwords.add('AC')  
	spwords.add('밀란') 
	spwords.add('레알')
	spwords.add('마드리드')
	spwords.add('레알마드리드')
	spwords.add('챔피언스')  
	spwords.add('리그')  
	spwords.add('챔피언스리그')
	spwords.add('스쿼드')  
	spwords.add('질문')  
	spwords.add('대해서') 
	spwords.add('알려주세요') 
	spwords.add('피파') 
	spwords.add('피파4') 
	spwords.add('피파온라인4')
	spwords.add('피파온라인')

	wc1 = WC(
    	# font_path = "/system/Library/Fonts/AppleSDGothicNeo.ttc", # mac
    	font_path = "C:\Windows\Fonts\malgun.ttf", # windows
    	background_color = 'white',
    	stopwords=spwords,
    	width = 540,
    	height = 390,
    	random_state = 40,
    	# stopwords = ['AC]
	)

	# WordCloud에 우리가 생성한 단어를 적용
	wc1.generate(wordStr)

	wc1.to_file("search_file/word.png")

wordMain = uic.loadUiType("ui/ui_wordCloud.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class WordWin(QDialog, wordMain): # 윈도우, ui파일 둘 다 가져옴 (DIalog로 생성된 ui파일)

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn_wordCloud.clicked.connect(self.btn_wordCloud_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)

	def btn_wordCloud_clicked(self):
		wordCloudView()
		# 불러오기
		self.lb_img.setPixmap(QPixmap('./search_file/word.png'))
	
	def btn_close_clicked(self):
		self.close() # 자기 자신만 종료
	
	def showModal(self):
		return super().exec_() # 화면 출력
