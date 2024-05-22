'''
# 작성일 : 2024년 5월 2일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

import pickle # Python의 객체를 넣을 수 있음

pFile = open('pFile.pickle', 'wb') # 바이너리

saveData = {
	"name" : "홍길동",
	"age" : 35,
	"lang" : "Python"
}

pickle.dump(saveData, pFile) # 저장

pFile.close()