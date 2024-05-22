'''
# 작성일 : 2024년 5월 2일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

import pickle

loadFile = open('pFile.pickle', 'rb') # 바이너리로 Write 됐으므로 바이너리로 Read

memData = pickle.load(loadFile)

print(memData)

loadFile.close()
