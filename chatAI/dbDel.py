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

	sql = "DELETE FROM chat WHERE id = %s"
	val = 4
	cursor.execute(sql, val)
	conn.commit()
	

except:
	print("삭제 에러입니다.")

conn.close()