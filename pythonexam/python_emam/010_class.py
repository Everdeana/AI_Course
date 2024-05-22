'''
# 작성일 : 2024년 5월 2일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

'''
class Cafe:# Class --> U
	coffee = "아이스커피"
	juice = "생과일주스"

	def	ordering(self): # 클래스 내에서 동작되는 함수들은 self 필수
		# print("주문받아요!")
		print("주문 : " + self.coffee) # 클래스 내의 변수도 self 필수

	def	ordering1(self): # 클래스 내에서 동작되는 함수들은 self 필수
		print("주문 : " + self.juice) # 클래스 내의 변수도 self 필수

starbucks = Cafe()
twosome = Cafe()
ediya = Cafe()

tarbucks.ordering()
twosome.ordering1()
ediya.ordering()
'''

'''
elas Cafc:# Class --> U
	def __init__(self, menu): # 셍성자
		print("Open")
		self.menu = menu

	def	ordering(self): # 클래스 내에서 동작되는 함수들은 self 필수
		# print("주문받아요!")
		print("주문 : " + self.menu) # 클래스 내의 변수도 self 필수

starbucks = Cafe("카페라떼")
twosome = Cafe("아메리카노")
ediya = Cafe("바닐라라뗴")

tarbucks.ordering()
twosome.ordering()
ediya.ordering()
'''

'''
elas Cafc:# Class --> U
	def __init__(self, menu): # 셍성자
		print("Open")
		self.menu = menu

	def	ordering(self): # 클래스 내에서 동작되는 함수들은 self 필수
		# print("주문받아요!")
		print("주문 : " + self.menu) # 클래스 내의 변수도 self 필수

starbucks = Cafe("카페라떼")
twosome = Cafe("아메리카노")
ediya = Cafe("바닐라라뗴")

tarbucks.ordering()
twosome.ordering()
ediya.ordering()
'''

'''
class Cafe:# Class --> U
	menu = ''
	cupSize = ''
	
	def __init__(self, menu): # 셍성자
		print("Open")
		self.menu = menu

	def	ordering(self, cupSize): # 클래스 내에서 동작되는 함수들은 self 필수
		# print("주문받아요!")
		self.cupSize = cupSize
		print(f"주문 : {self.menu}, 크기 :  {self.cupSize}") # 클래스 내의 변수도 self 필수
'''
# 초기화c 때 "커피명"
# ordering 할 때 "사이즈"
from cafe import run

# menu = '1234' # 클래스가 독립되어있으므로 영향 X


run()
