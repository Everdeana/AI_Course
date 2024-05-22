import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)

app = QApplication(sys.argv) #윈도우를 만드는 명령(Q는 PyQT형 의미)

btn = QPushButton("푸시버튼입니다.")

btn.show() # 화면
app.exec_() # 사용자가 종료버튼(X) 누르기 전까지 프로그램 동작
