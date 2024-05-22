# 라이브러리 불러오기
import pymysql
from datetime import datetime
import requests

#########################################################################################################
# DB 저장 함수
#########################################################################################################

def MemDbAdd(mail, name, telno, addr, sns):

	# DB Setting
	conn = pymysql.connect(
		host 	 = '127.0.0.1', # == host = 'localhost' --> 자기 자신 의미
		user 	 = 'mem',
		password ='@ai1234@',
		port 	 = 3306,
		db 		 = 'memdb',
		charset  = 'utf8' # 기본 변수들
	)

	# print(ipCheck())

	try:
		# 현재 날짜 구하기
		saveDate = datetime.today().strftime("%Y-%m-%d %H:%M:%S") # YYYY/mm/dd HH:MM:SS 형태의 시간 출력
		# ip 주소 확인
		saveIp = requests.get("http://ip.jsontest.com").json()['ip']

		cursor = conn.cursor()
		# insert 처리
		sql = """INSERT INTO member 
		(mail, name, telno, addr, sns, date_created, ip) 
		VALUES(%s, %s, %s, %s, %s, %s, %s)"""
		val = [mail, name, telno, addr, sns, saveDate, saveIp]
		
		cursor.execute(sql, val)
		conn.commit() # DB에 데이터 기록
		print("데이터를 기록하였습니다.")
		'''
        print(mails)
		print(names)
		print(telnos)
		print(addrs)
		print(sns)
		'''

	except:
		print("입력 에러입니다.")

	conn.close()
	

'''
# DB 기록 테스트
MemDbAdd('gmail', 
		 'testname', 
		 '0101010101', 
		 'testaddr', 
		 'testsns')
'''
