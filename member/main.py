'''
DS
1. AI-HUB
2. Google Dataset Search
3. Roboflow
'''

import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	

from memAdd import MemAddWin
from memEdit import MemEditWin
from memdbList import MemDbList
from memdbDel import MemDbDel

form_main = uic.loadUiType("ui/main.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수


class MyWindow(QMainWindow, form_main): # 윈도우, ui파일 둘 다 가져옴

	delIdx 		= ''
	editIdx 	= ''
	editMail 	= ''
	editName 	= ''
	editTelno 	= ''
	editAddr 	= ''
	editSns 	= ''

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		# tbl_mem 초기화
		self.tbl_mem.setRowCount(8)
		self.tbl_mem.setColumnCount(6)
		self.tbl_mem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.tbl_mem.setHorizontalHeaderLabels(
			["id", "mail", "name", "telno", "addr", "sns"]
		)
		self.tbl_mem.cellClicked.connect(self.cellclicked_event) # 키보드로 움직였을 때 이벤트 추가

		self.btn_search.clicked.connect(self.btn_search_clicked)
		self.btn_add.clicked.connect(self.btn_add_clicked)
		self.btn_edit.clicked.connect(self.btn_edit_clicked)
		self.btn_del.clicked.connect(self.btn_del_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)

	def cellclicked_event(self, row, col): # --> 클릭 위치 표시
		print(f"row = {row}, col = {col}")
		try:
			# 삭제
			self.delIdx = self.tbl_mem.item(row, 0).text() # col은 무조건 0 --> Index 값이 필요하기 때문
			print("idx = ", self.delIdx)
			# 수정
			self.editIdx 	= self.tbl_mem.item(row, 0).text()
			self.editMail 	= self.tbl_mem.item(row, 1).text()
			self.editName 	= self.tbl_mem.item(row, 2).text()
			self.editTelno	= self.tbl_mem.item(row, 3).text()
			self.editAddr 	= self.tbl_mem.item(row, 4).text()
			self.editSns 	= self.tbl_mem.item(row, 5).text()
		except Exception as e:
			print(e)

	def btn_search_clicked(self):
		# 데이터 조회 결과 처리
		datas = MemDbList(self.le_search.text())
		print('데이터 크기 : ', len(datas))
		self.tbl_mem.setRowCount(len(datas)) # 변수를 다른 곳에 사용하지 않으므로 변수 선언 X

		# 데이터 출력
		for idx, data in enumerate(datas): # 인덱스 값이 필요하므로 enumerate
			self.tbl_mem.setItem(idx, 0, QTableWidgetItem(str(data[0]))) # 0, 0 --> row, column
			self.tbl_mem.setItem(idx, 1, QTableWidgetItem(data[1])) # 0, 0 --> row, column
			self.tbl_mem.setItem(idx, 2, QTableWidgetItem(data[2]))
			self.tbl_mem.setItem(idx, 3, QTableWidgetItem(data[3]))
			self.tbl_mem.setItem(idx, 4, QTableWidgetItem(data[4]))
			self.tbl_mem.setItem(idx, 5, QTableWidgetItem(data[5]))
	
	def btn_add_clicked(self):
		memaddWin = MemAddWin()
		memaddWin.showModal()
		self.btn_search_clicked()
		
	def btn_edit_clicked(self):
		memeditWin = MemEditWin()
		# 데이터 전달 만들기
		memeditWin.loadData(
			self.editIdx,
			self.editMail,
			self.editName,
			self.editTelno,
			self.editAddr,
			self.editSns
		)
		memeditWin.showModal()
		self.btn_search_clicked()

	def btn_del_clicked(self):
		if self.delIdx == '':
			QMessageBox.about(self, "확인", "선택된 항목이 없습니다.")
			return

		# 삭제하기
		if MemDbDel(self.delIdx) == True:
			QMessageBox.about(self, "확인", "데이터를 삭제하였습니다.")
			self.btn_search_clicked()
		else:
			QMessageBox.about(self, "에러", "데이터 삭제에 실패하였습니다.")

		self.delIdx = ''

	def btn_close_clicked(self):
		exit()
			
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()