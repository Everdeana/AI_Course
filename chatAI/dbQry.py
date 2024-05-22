# 만들어놓은 DB의 데이터 조회

# 라이브러리 불러오기
import pymysql


# DB Setting
conn = pymysql.connect(
	host = '127.0.0.1', # == host = 'localhost' --> 자기 자신 의미
	user = 'chat',
	password='@ai7371@',
	port = 3306,
	db = 'chatdb',
	charset = 'utf8' # 기본 변수들
)

try:
	cursor = conn.cursor()

	sql = "select * from chat"
	cursor.execute(sql)
	rst = cursor.fetchall()
	for data in rst:
		# print(data[1])
		print(data)

except:
	print("조회 에러입니다.")

conn.close()