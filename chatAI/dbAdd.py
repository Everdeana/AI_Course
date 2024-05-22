# 라이브러리 불러오기
import pymysql
from datetime import datetime
import requests

#########################################################################################################
# DB 저장 함수
#########################################################################################################

def ChatGPTadd(human_chat, ai_chat):

	# DB Setting
	conn = pymysql.connect(
		host = '127.0.0.1', # == host = 'localhost' --> 자기 자신 의미
		user = 'chat',
		password='@ai7371@',
		port = 3306,
		db = 'chatdb',
		charset = 'utf8' # 기본 변수들
	)

	# print(ipCheck())

	try:
		# 현재 날짜 구하기
		saveDates = datetime.today().strftime("%Y-%m-%d %H:%M:%S") # YYYY/mm/dd HH:MM:SS 형태의 시간 출력
		# ip 주소 확인
		saveIps = requests.get("http://ip.jsontest.com").json()['ip']

		cursor = conn.cursor()
		# insert 처리
		sql = "INSERT INTO chat (human_chat, ai_chat, dates, ips) VALUES(%s, %s, %s, %s)"
		val = (human_chat, ai_chat, saveDates, saveIps)
		
		# sql = "INSERT INTO chat VALUES(%s, %s, %s, %s, %s)"
		# val = ('3', '오늘 날씨 어때?', '좋아', '2024-05-10 15:23:00', '1.1.1.1') # id 값을 비운 채로 쿼리를 실행하면 id값에 상관 없이 데이터 저장
		
		cursor.execute(sql, val)
		conn.commit() # DB에 데이터 기록
		print("데이터를 기록하였습니다.")

	except:
		print("입력 에러입니다.")

	conn.close()

