# 만들어놓은 DB의 데이터 조회

# 라이브러리 불러오기
import pymysql

def MemDbList(qry):
	rst = '' # 데이터 전송방법 2 -->전역변수로 선언

	# DB Setting
	conn = pymysql.connect(
		host	 = '127.0.0.1', # == host = 'localhost' --> 자기 자신 의미
		user 	 = 'mem',
		password = '@ai1234@',
		port	 = 3306,
		db		 = 'memdb',
		charset	 = 'utf8' # 기본 변수들
	)

	try:
		cursor = conn.cursor()

		if qry == '':
			sql = """select id, mail, name, telno, addr, sns
			from member
			"""
		else:
			sql = f"""select id, mail, name, telno, addr, sns
			from member where
			(mail	like '%{qry}%' or
			 name	like '%{qry}%' or
			 telno	like '%{qry}%' or
			 addr	like '%{qry}%' or
			 sns	like '%{qry}%' )
			"""
			
		
		cursor.execute(sql)
		rst = cursor.fetchall() # 결과 rst에 저장
		for data in rst:
			# print(data[1])
			print(data)

		# conn.close()
		# return rst

	except:
		print("조회 에러입니다.")
		return # return을 해주지 않으면 아래로 넘어가버림 --> finally
	
	finally:
		conn.close()
		return rst

# 데이터 조회 Test
data = MemDbList('gmail')
print('data = ', data)