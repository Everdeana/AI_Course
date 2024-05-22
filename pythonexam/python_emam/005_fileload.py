'''
# 작성일 : 2024년 5월 2일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

fileload = open('save.txt', 'r', encoding='utf8') 

# print(fileload)

while True:
	line = fileload.readline()

	if not line: # 라인에 데이터 없으면
		break

	print(line, end='') # 라인이 있으면 출력 후 뒤에(end)엔터값

fileload.close()

# readlines는 모든 데이터를 한번에 불러오기 때문에
# \n을 제거해야 하므로 잘 사용하지 X
# python re / VASA - 1