# 라이브러리 불러오기
import cv2
import yolov5
import time
import torch
import pandas as pd
import yaml

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# yolov5 Custom Model 불러오기
model = torch.hub.load('ultralytics/yolov5', 'custom', path = './train/best.pt', force_reload=False)

# yaml에 있는 데이터셋(labels) 불러오기
data_yaml = './train/data.yaml'

with open(data_yaml) as f:
	data = yaml.load(f, Loader=yaml.FullLoader)

# print(data)
# print("#"*140)
# print(data['names'])

# 레발(정답) cjfl
labels = data['names']
print(labels)

# 영상 불러오기
cap = cv2.VideoCapture(0) 
'''
cap1 = cv2.VideoCapture(1) # 카메라 1개 -> 0 / 카메라 2개 -> 1 / ...
cap2 = cv2.VideoCapture(2) 
cap3 = cv2.VideoCapture(3) 
'''

# 카메라 크기 조x정
# width : 3, height : 4
cap.set(3, 1280)
cap.set(4, 720)

# 실시간으로 계속 영상 받기

while True:
    
    _, frame = cap.read()  # 비디오 프레임 읽기
    
    frame = cv2.flip(frame, 1)
    
	# yolov5 처리 후
    results = model(frame)
    
    df_hand = results.pandas().xyxy[0]
    hands = df_hand.values.tolist()
    
	
    for hand in hands:
        print("손인식: ", hand[6])
    # print(df_hand) 
    # print(hands)
    
    label = results.xyxy[0][:, -1].cpu().numpy()
    bbox = results.xyxy[0][:, :-2].cpu().numpy()
    score = results.xyxy[0][:, -2].cpu().numpy()

    print("labels = ", label)
    print("bbox = ", bbox)
    print("score = ", score)

    # 스코어 글씨 변경
    if len(score) > 0:
        conf_score = round(score[0] * 100, 2)
        print_score = f'{conf_score} %'

    # 바운딩 박스 처리
    if len(label) > 0:
        # 네모 박스 int 처리
        x1 = int(bbox[0][0])
        y1 = int(bbox[0][1])
        x2 = int(bbox[0][2])
        y2 = int(bbox[0][3])
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2) # BGR, Line
        cv2.rectangle(frame, (x1, y1 - 30), (x1 + 200, y1), (0, 0, 255), -1) # BGR, Line

        text = f'{labels[int(label[0])]} : {print_score}'

        cv2.putText(frame, text, (x1 + 15, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # 카메라 객체 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기