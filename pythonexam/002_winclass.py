import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow): # QMainWindow 에서 상속받음
	def __init__(self):
		super().__init__() # QMainWindow에 있는 모든 기능 수행
		self.setWindowTitle("PyQt Test")		
		self.setGeometry(100, 200, 600, 400) # 창 크기 조정
		self.setMaximumWidth(800)
		self.setMinimumWidth(100)
		self.setWindowIcon(QIcon('testIcon1.png'))

		btn = QPushButton('버튼1', self)
		btn.move(5, 30)
		btn.clicked.connect(self.btn_click)

		menubar = self.menuBar()
        
		menu1 = menubar.addMenu("파일") 
		menu2 = menubar.addMenu("설정")
		menu3 = menubar.addMenu("Help")
        
		loadfile = QAction('load File', self)
		savefile = QAction('save File', self)	
		property = QAction('property', self)

		help =    QAction('help', self)
		version = QAction('version 보기', self)


		menu1.addAction(loadfile)
		menu1.addAction(savefile)

		menu2.addAction(property)		

		menu3.addAction(help)
		menu3.addAction(version)

	def btn_click(self):
		print("버튼을 눌렀습니다.")

app = QApplication(sys.argv)
windowMain = MyWindow()
windowMain.show()
app.exec_()
