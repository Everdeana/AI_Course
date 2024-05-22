import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	
from PyQt5.QtGui import *
from search_naver import *


searchMain = uic.loadUiType("ui/ui_crawling.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class SearchWin(QDialog, searchMain): # 윈도우, ui파일 둘 다 가져옴 (DIalog로 생성된 ui파일)
	# 전역변수
	searchKin = ''
	# model = QStandardItemModel() # 1번만 불러야 하기 떄문에 self.model = QStandardItemModel()로 선언하지 않고 전역변수로 선언

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		self.btn_search.clicked.connect(self.btn_search_clicked)
		self.btn_save.clicked.connect(self.btn_save_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)
		self.btn_add.clicked.connect(self.btn_add_clicked)

		

	def btn_add_clicked(self):
		# 리스트뷰에 데이터 추가
		# self.model.appendRow(QStandardItem('데이터 추가'))
		# self.lv_search.setModel(self.model)
		pass

	def btn_search_clicked(self):
		if self.le_search.text() == '':
			QMessageBox.about(self, "에러", "입력 값이 존재하지 않습니다.")
			return
		# 간결함을 위해 else를 쓰지 않고 return 후 바로 나감 --> 한 루틴에선 한 가지만 수행
		
		naverClear()
		self.searchKin = self.le_search.text()
		# print(self.le_search.text())
		
		# 검색 동작
		for i in range(100):
			page = i + 1
			sList = naverKin(self.searchKin, page)
			print('#'*20 + ' ' + str(page) + ' ' + '#'*20)
			
			print(sList)

			#리스트뷰에 보여주기
			model = QStandardItemModel()
			for data in sList:
				model.appendRow(QStandardItem(data[0]))
			self.lv_search.setModel(model)

			time.sleep(1.5)



	def btn_save_clicked(self):
		if self.searchKin == '':
			QMessageBox.about(self, "에러", "검색한 정보가 없습니다.")
			return
		# 파일로 저장
		saveKin(f'search_file/{self.searchKin}')
		QMessageBox.about(self, "저장", "검색한 정보가 저장되었습니다.")

	def btn_close_clicked(self):
		self.close() # 자기 자신만 종료
	
	def showModal(self):
		return super().exec_() # 화면 출력


		# self.btn_close.clicked.connect(self.btn_close_clicked)
		
