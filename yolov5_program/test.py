# 라이브러리 설치
import torch

# 모델 불러오기
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# 파라미터 미세조정
model.conf = 0.6

# 이미지 검증(Predict)
img = "https://www.sporf.com/wp-content/uploads/2023/04/afab2c7c-gettyimages-74058407.jpg"

# 검증
results = model(img)

results.print()

# 프로그램에서 사용할 수 있도록 정보 받기(화면에 이미지 출력)
results.show()

# 데이터 구조 형태로 보기
print(results.pandas().xyxy[0])

# 저장
results.save('./savedata/milan_result.jpg')

# crop
results.crop()

