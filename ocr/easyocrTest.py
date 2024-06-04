import easyocr

# 기본 구현
reader = easyocr.Reader(['en', 'ko'])

rst = reader.readtext('./test_data/news3.jpg')

# print(rst)

for msg in rst:
	print(msg[1])
