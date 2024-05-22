'''
DS
1. AI-HUB
2. Google Dataset Search
3. Roboflow

'''

import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	

from search import SearchWin # search.py --> SearchWin Class Import
from word import WordWin

form_main = uic.loadUiType("ui/ui_main.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class MyWindow(QMainWindow, form_main): # 윈도우, ui파일 둘 다 가져옴
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.btn_close.clicked.connect(self.btn_close_clicked)
		self.btn_search.clicked.connect(self.btn_search_clicked)
		self.btn_wordcloud.clicked.connect(self.btn_wordcloud_clicked)

	def btn_search_clicked(self):
		searchWin = SearchWin()
		searchWin.showModal()

	def btn_wordcloud_clicked(self):
		wordWin = WordWin()
		wordWin.showModal()
	
	def btn_close_clicked(self):
		exit()
			
			
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()