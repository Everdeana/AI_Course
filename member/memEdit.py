from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	
from PyQt5.QtGui import *
from memdbEdit import MemDbEdit


memEditMain = uic.loadUiType("ui/mem_edit.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class MemEditWin(QDialog, memEditMain): # 윈도우, ui파일 둘 다 가져옴 (DIalog로 생성된 ui파일)

	editIdx = ''

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn_edit.clicked.connect(self.btn_edit_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)

	def loadData(self, idx, mail, name, telno, addr, sns): # 클래스는 항상 맨 앞에 self 필요 --> 없으면 클래스가 객체 인식 불가
		self.editIdx = idx
		self.le_mail.setText(mail)
		self.le_name.setText(name)
		self.le_telno.setText(telno)
		self.le_addr.setText(addr)
		self.le_sns.setText(sns)
		

	def btn_edit_clicked(self):
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
			return # 간결함을 위해 else를 쓰지 않고 return 후 바로 나감 --> 한 루틴에선 한 가지만 수행
		try:
			# 변수가 필요하지 않을 땐 변수 사용 X
			MemDbEdit(
				self.editIdx,
				self.le_mail.text(), 
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
			QMessageBox.about(self, "수정 완료", "수정되었습니다.")
		except:
			QMessageBox.about(self, "수정 에러", "수정에 실패하였습니다!!!.")
	def btn_close_clicked(self):
		self.close() # 자기 자신만 종료
	
	def showModal(self):
		return super().exec_() # 화면 출력
