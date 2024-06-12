# Anaconda : p310_medease

import json
import pandas as pd

# 파일 경로 설정
input_file_path = r'./combined_disease_prediction_symptom.json'
csv_output_path = r'./disease_symptoms_unique.csv'
json_output_path = r'./disease_symptoms_unique.json'

# JSON 데이터 로드
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 질병 이름과 증상 추출
disease_symptoms = []

for entry in data:
    instruction = entry.get('instruction', '')
    output = entry.get('output', '')
    
    if "What are the symptoms of" in instruction:
        disease = instruction.split("What are the symptoms of ")[1].strip('?')
        symptoms = output.split("The following are the symptoms of ")[1].split(': ')[1]
        disease_symptoms.append({'Disease': disease, 'Symptoms': symptoms})
    elif "What could be the disease" in instruction:
        symptoms = instruction.split("I am having the following symptoms: ")[1].split('. What could be the disease ?')[0]
        disease = output.split("The symptoms listed indicates that the patient is dealing with ")[1].strip('.')
        disease_symptoms.append({'Disease': disease, 'Symptoms': symptoms})

# DataFrame으로 변환
df = pd.DataFrame(disease_symptoms)

# 중복 제거
df_unique = df.drop_duplicates()

# CSV와 JSON 파일로 저장
df_unique.to_csv(csv_output_path, index=False, encoding='utf-8')
df_unique.to_json(json_output_path, orient='records', lines=True, force_ascii=False)

print("전처리가 완료되었습니다.")
