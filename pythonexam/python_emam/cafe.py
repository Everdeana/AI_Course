class Cafe:# Class --> U
	cafeName = ''
	cafeMenu = ''
	cupSize = ''
	
	def __init__(self, name, menu): # 셍성자
		print("Open")
		self.cafeMenu = menu
		self.cafeName = name

	def	ordering(self, cupSize): # 클래스 내에서 동작되는 함수들은 self 필수
		# print("주문받아요!")
		self.cupSize = cupSize
		print(f"{self.cafeName} -> 주문 : {self.cafeMenu}, 크기 :  {self.cupSize}") # 클래스 내의 변수도 self 필수

def run():
	starbucks = Cafe("스타벅스", "카페라떼")
	twosome = Cafe("투썸", "아메리카노")
	ediya = Cafe("이디야", "바닐라라뗴")

	starbucks.ordering("톨")
	twosome.ordering("레귤러")
	ediya.ordering("빅")

# run() # 클래스 테스트

