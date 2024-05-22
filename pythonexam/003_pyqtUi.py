import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	


form_main = uic.loadUiType("main.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class MyWindow(QMainWindow, form_main): # 윈도우, ui파일 둘 다 가져옴
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn1.clicked.connect(self.btn1_clicked)
		self.btn2.clicked.connect(self.btn2_clicked)
		self.btn3.clicked.connect(self.btn3_clicked)
		self.btn4.clicked.connect(self.btn4_clicked)
		self.btn5.clicked.connect(self.btn5_ok)
		self.btnSearch.clicked.connect(self.btnSearch_clicked) 
		
	def btnSearch_clicked(self):
		self.searchText = self.lbSearch.text()
		QMessageBox.about(self, "검색창 검색어", f"'{self.searchText}'이/가 입력되었습니다.")
		print(self.lbSearch.text())
		
	def btn1_clicked(self):
		print("버튼 1이 눌렸습니다.")
		QMessageBox.about(self, "message", "버튼 1이 눌렸습니다.")
	def btn2_clicked(self):
		print("버튼 2가 눌렸습니다.")
		QMessageBox.about(self, "message", "버튼 2가 눌렸습니다.")
	def btn3_clicked(self):
		print("버튼 3이 눌렸습니다.")
		QMessageBox.about(self, "message", "버튼 3이 눌렸습니다.")
	def btn4_clicked(self):
		print("버튼 4가 눌렸습니다.")
		QMessageBox.about(self, "message", "버튼 4가 눌렸습니다.")

	def btn5_ok(self):
		print("버튼 1이 눌렸습니다.")
		btnQa = QMessageBox.information(
			self,
			"삭제",
			"자료를 삭제하시겠습니까 ?",
			QMessageBox.Yes | QMessageBox.Cancel
		)

		if btnQa == QMessageBox.Yes:
			QMessageBox.about(self, "삭제 완료", "자료를 삭제하였습니다.")
		if btnQa == QMessageBox.Cancel:
			QMessageBox.about(self, "삭제 취소", "취소하였습니다.")
	
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()