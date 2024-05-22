#################################################################
# 네이버 지식인 자동 크롤링 시스템
# 일자 : 2024년 5월 7일
# lib : pyqt5, requests, beautifulsoup4, selenium
#################################################################

import csv # 엑셀 파일로 데이터 저장
from urllib.request import urlopen # URL 정보 받아오기 위해 import
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus # 특수문자 변환(한글 인코딩)
import requests
import codecs
import time

# csv로 저장할 배열
searchList = [] # 전역 변수

'''
def getSearchList():
	global searchList
	searchList = []
'''

def naverClear():
	global searchList
	searchList = []

def naverKin(search, i):
	'''
	# global searchList
	# searchList = [] # 반복 할때마다 클리어하므로 이렇게 짜면 X
	'''

	'''
	import sys # PyQt는 시스템 정보를 사용
	from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
	from PyQt5 import uic # ui파일 open	
	'''
	'''
	# 입력창
	# search = input("지식인 검색어를 입력하세요 : ")
	# print("검색어 : ", search)
	# search = "AC밀란"
	'''

	'''
	# URL에서 정보 가져오기
	query = quote_plus(search) # 한글 변환
	print("검색어 변환 : ",query)
	url = "https://kin.naver.com/search/list.naver?query="
	'''

	url = f"https://kin.naver.com/search/list.naver?query={quote_plus(search)}&page={i}"
	print("url : ", url)

	# 인터넷에서 정보 가져오기(request)
	# html = urlopen(url).read() # html 코드를 분석할 때 --> BeautifulSoup
	# 위와 같이 코딩을 하면 정상적으로 응답을 했는지 알 수 없다
	html = requests.get(url) # Response를 알기 위해 requests 사용
	print("html : ", html)

	# BS4로 특정부분 검색 후 정보 가져오기
	# if HTTP response status codes != 200 --> 종료
	# https://developer.mozilla.org/ko/docs/Web/HTTP/Status

	# if html.status_code >= 200 or html.status_code < 300: <-- 이렇게 사용하기도 함
	if html.status_code == 200:
		htmlcode = html.text
		# print(htmlcode)
		# 선언
		soup = bs(htmlcode, 'html.parser')
		
		# <ul class="basic1"> 찾는 과정
		ul = soup.select_one('ul.basic1') # BeautifulSoup --> 필요한 부분만 잘라서 가져옴

		# li 추출
		titles = ul.select('li>dl>dt>a')


	# 데이터 값 가져오기
	for title in titles:
		print(title.text) # 텍스트만
		print(title.attrs['href'])

		# 임시 공간에 저장 --> 1차원 배열에 배열을 하나 더 넣으려면
		

		tmp = []
		tmp.append(title.text)
		tmp.append(title.attrs['href'])
		searchList.append(tmp)
	
	return searchList

def saveKin(search):
	'''
	# 엑셀 파일로 저장
	# with open("search.csv", 'w') as file:
	# 	writer = csv.writer(file)
	# 	writer.writerow(searchList)
	'''

	# 엑셀 파일로 저장
	f = codecs.open(f'{search}.csv', 'w', encoding='UTF-8')# cp949 형식의 파일 생성
	csvWriter = csv.writer(f)

	csvWriter.writerow(['제목', '링크'])

	for data in searchList:
		# 한줄씩 저장
		csvWriter.writerow(data)

	f.close()

####################################################################################
# 함수 테스트
####################################################################################
'''
search = input("검색어 : ")

for i in range(10):
	page = i + 1
	naverKin(search, page)
	print('#'*20 + ' ' + str(page) + ' ' + '#'*20)
	time.sleep(1.5)
'''