from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	
from PyQt5.QtGui import *
from memdbAdd import MemDbAdd


memAddMain = uic.loadUiType("ui/mem_add.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class MemAddWin(QDialog, memAddMain): # 윈도우, ui파일 둘 다 가져옴 (DIalog로 생성된 ui파일)

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn_add.clicked.connect(self.btn_add_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)

	

	def btn_add_clicked(self):
		if self.le_mail.text() == '':
			QMessageBox.about(self, "입력에러", "메일을 입력해주세요!!!.")
			return
		if self.le_name.text() == '':
			QMessageBox.about(self, "입력에러", "이름을 입력해주세요!!!.")
			return
		if self.le_telno.text() == '':
			QMessageBox.about(self, "입력에러", "전화번호를 입력해주세요!!!.")
			return
		if self.le_addr.text() == '':
			QMessageBox.about(self, "입력에러", "주소를 입력해주세요!!!.")
			return
		# 간결함을 위해 else를 쓰지 않고 return 후 바로 나감 --> 한 루틴에선 한 가지만 수행
		try:
			# 변수가 필요하지 않을 땐 변수 사용 X
			MemDbAdd(self.le_mail.text(), 
				self.le_name.text(), 
				self.le_telno.text(), 
				self.le_addr.text(), 
				self.le_sns.text()
			)
			'''
		print(self.memMail)
		print(self.memName)
		print(self.memTelno)
		print(self.memAddr)
		print(self.memSns)
		'''
			QMessageBox.about(self, "입력", "데이터베이스에 기록되었습니다.")
		except:
			QMessageBox.about(self, "입력에러", "데이터베이스 입력 실패하였습니다!!!.")
	def btn_close_clicked(self):
		self.close() # 자기 자신만 종료
	
	def showModal(self):
		return super().exec_() # 화면 출력
