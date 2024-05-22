################################################################################################################################
# 작성일 : 2024년 5월 1일
# 파일명 : print 테스트
# 개발자 : 장국진
# 사용 라이브러리 : request
################################################################################################################################
'''
주석 종류
'''

# 주석 처리 --> 블럭 선택 후 ctrl + /

# 문자 출력
print("테스트1")
print('테스트2')

# 숫자 출력
print(5+4)

# 변수
# test_var = "var테스트" (X) ------> 카멜 습관화 ↓
testVar = "var테스트"
print(testVar)

# 전역변수 --> 앞에 G 포함
G_TESTVAR = "11"
gTestVar = "22"

# Python Type
age = 26
print(age)
print(type(age))

# 입력

# iTest = input("숫자를 입력하세요: ")
# print("입력된 숫자는 " + iTest + " " + iTest + "입니다." )
# print(iTest)
# print(type(iTest))

# # fstring
# print(f"입력된 숫자는 {iTest} {iTest} 입니다." )
# # 여러줄
# print(f"""입력된 숫자는 {iTest} {iTest} 입니다.
# 테스트 입니다. {iTest}
# """ )

# 실수
pi = 3.14
print(pi)
print(type(pi))

# 실수 계산 방법
pi = 3.141592654
# 		 123456789
round_pi = round(pi, 5)
print(round_pi)

# 정수 -> 실수
aa = 1
print(aa)
print(type(aa))

aa = 1.
print(aa)
print(type(aa))

# 여러번 출력
print("#"*20)

# 문자열 개수 확인
aTest = "테스트 1234" # 한글도 1자리 --> 유니코드
print(aTest)
print(len(aTest))

# 형변환 연산자
# int --> str / str --> int
fStr = "1.2345"
print(fStr)
print(type(fStr))

fFlot = float(fStr)
print(fFlot)
print(type(fFlot))

print("#"*20) ################################################################################

sStr = "23456"
print(sStr)
print(type(sStr))

sInt = int(sStr)
print(sInt)
print(type(sInt))

print("#"*20) ################################################################################

iInt = 34567
print(iInt)
print(type(iInt))

iStr = str(iInt)
print(iStr)
print(type(iStr))

# 질문
a = 100_000 # ,000, --> 반점 자리에 _ 넣으면 숫자로 인식
print(a)
print(type(a))

# 참 거짓 처리
tof = 5 > 10
print(tof)
print(type(tof))

# 숫자 함수 --> abs, pow, max, min, round
print(max(6, 8, 10, 4, 2))
print(min(6, 8, 10, 4, 2))
print(abs(-100)) 
print(pow(4, 2))
