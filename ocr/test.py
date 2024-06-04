from PIL import Image
import pytesseract

# 명령어 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' # r : 경로를 입력할 때 \\ 중복 입력 방지

# 성능을 올리기 위한 옵션
# config = '-l kor + eng --oem 3 --psm 11'
# config = '-l kor + eng --oem 2 --psm 6'
# 성능 1
# config = '-l kor + eng --oem 1 --psm 6'
# 성능 2
# config = '-l kor + eng --oem 1 --psm 6'
config = '-l eng --oem 1 --psm 6'


# 한국어 + 영어를 같이 인식하도록 설정
rst = pytesseract.image_to_string(Image.open('./test_data/news4.jpg'), config = config)# lang='kor+eng')

print(rst)