'''
# 작성일 : 2024년 5월 2일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''
'''
#에러 순서
# 1. File Name
# 2. Line
# 3. Error 
'''
try:
	x = input("숫자를 입력하세요 : ")

	y = 10 / int(x)
	print(y)
except:
	print("숫자는 0으로 나눌 수 없습니다.")
