'''
# 작성일 : 2024년 5월 1일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

def AddFunc(x, y):
	z0 = x + y
	z1 = x - y
	z2 = x * y
	z3 = x // y
	z4 = x % y
	return z0, z1, z2, z3, z4 # 여러 변수들을 받을 수 있음

# a0, a1, a2, a3, a4 = AddFunc(5, 4)

# print(a0)
# print(a1)
# print(a2)
# print(a3)
# print(a4)

print("-"*60)

a0, _, a2, _, a4 = AddFunc(5, 4) # 데이터는 받았지만 사용 X

print(a0)
# print(a1)
print(a2)
# print(a3)
print(a4)

print("-"*60)

def AddFunc1(x, y = 3): #  default값 설정
	b1 = x + y
	return b1

print(AddFunc1(5)) # default값 있으므로 y 입력 없으면 y에 3 저장

print("-"*60)

#########################################################################################################
# 자료형 : 배열(list) --> 추가/삭제 가능, 튜플(tuple) --> 추가/삭제 불가능, 딕셔너리(dictionary)
# 배열 [], 튜플 (), 딕셔너리 {}
# 딕셔너리 구조 --> json과 유사한 형태 --> 데이터 송수신시 json 사용하므로 python에선 딕셔너리 많이 사용
# 배열 + 딕셔너리 = 데이터 전송

arrList = [[10, 20, 30], [20, 21, 22], [30, 31, 32]] # 인공지능에선 2차원배열(다중배열) 사용
print(arrList)
print(type(arrList))

# 앞에서 ->  0	 1   2	 3	 4
arrList1 = [10, 20, 30, 40, 50]
# 뒤에서 ->	-5	-4	-3	-2	-1
print(arrList1[0])
print(arrList1[-1])

print("-"*60)

# 슬라이싱(배열, PANDAS) --> [첫번째 : 마지막 : 증감]
# 앞에서 ->  0, 1, 2, 3, 4
arrList1 = [1, 2, 3, 4, 5] # 3, 4, 5만 슬라이싱
# 뒤에서 ->	-5,-4,-3,-2,-1
sliceList1 = arrList1[2:]
print(sliceList1)
revList = arrList1[3::-1] # 역순 출력
print(revList)

print("-"*60)

# set
data1 = set([10, 20, 30, 40, 40, 40])
print(data1)

print("-"*60)

# 연산
#  = [0, 1, 2]
a1 = [1, 2, 3]
b1 = [4, 5, 6]
print(a1)
print(b1 * 3)

a1[2] = 7
print(a1)

del(a1[1])
print(a1)

a1.append(44) # 마지막 추가
print(a1)

a1.pop() # 마지막 삭제
print(a1)

print("-"*60)

# 배열 숫자 카운트
data11 = [10, 20, 30, 40, 40, 40]
print(data11.count(40))

print("-"*60)

# 반복문
aLoop = [10, 20, 30, 40, 50]
for data in aLoop:
	print('순번:', data)

print("-"*60)

for idx, data1 in enumerate(aLoop): # 인덱스까지 가져옴
	print(idx + 1, ':', data1)
	
print("-"*60)

aLoop = [10, 20, 30, 40, 50]
aLoop.reverse() # 참조하는 경우 원본 수정됨
print(aLoop) # 원본이 날아감

print("-"*60)

# 딕셔너리 --> {"key" : value, ...}
dic = {'name' : '홍길동', 'age' : 14, 'total' : 99.2}
print(dic['name']) # str
print(dic['age']) # int
print(dic['total']) # float

print("-"*60)

for k in dic.keys(): # key값만 가져옴
	print(k)

print("-"*60)

for v in dic.values(): # value값만 가져옴
	print(v)



#조건문
# a = 10
# b = 3

a = [10, 20, 30]

if a: # a에 데이터가 있으면
	print("-"*20)
	print(a)
	print("-"*20)
else:
	print("-"*20)
	print('일치하지 않음')
	print("-"*20)
# DB에서 많이 사용

# pickle