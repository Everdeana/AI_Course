import easyocr

# 기본 구현
reader = easyocr.Reader(['en', 'ko'])

# rst = reader.readtext('./test_data/news3.jpg') # 뉴스 글자 읽기
rst = reader.readtext('./test_data/car_bin.jpg') # 자동차 번호판 읽기
rst1 = reader.readtext('./test_data/car_bin1.jpg') # 자동차 번호판 읽기

# print(rst)

for msg in rst:
	print(msg[1])

for msg1 in rst1:
	print(msg1[1])
