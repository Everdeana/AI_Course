import json
import pandas as pd

# 파일 경로 설정
doctor_versus_disease_path = r'totData/Doctor_Versus_Disease.csv'
original_dataset_path = r'totData/Original_Dataset.csv'
specialist_path = r'totData/Specialist.xlsx'
symptom_weights_path = r'totData/Symptom_Weights.csv'
disease_description_path = r'totData/Disease_Description.csv'
doctor_specialist_path = r'totData/Doctor_Specialist.csv'

# 데이터 로드
doctor_versus_disease = pd.read_csv(doctor_versus_disease_path, encoding='ISO-8859-1')
original_dataset = pd.read_csv(original_dataset_path, encoding='ISO-8859-1')
specialist = pd.read_excel(specialist_path)
symptom_weights = pd.read_csv(symptom_weights_path, encoding='ISO-8859-1')
disease_description = pd.read_csv(disease_description_path, encoding='ISO-8859-1')
doctor_specialist = pd.read_csv(doctor_specialist_path, encoding='ISO-8859-1')

# 컬럼 이름 수정
doctor_versus_disease.columns = ['Disease', 'Specialist']
doctor_specialist.columns = ['Specialist']

# 병명과 증상, 전문의, 설명 추출
disease_symptoms_specialist = original_dataset.copy()
disease_symptoms_specialist['Symptoms'] = disease_symptoms_specialist.apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
disease_symptoms_specialist = disease_symptoms_specialist[['Disease', 'Symptoms']]

disease_specialist = doctor_versus_disease[['Disease', 'Specialist']]
disease_description = disease_description[['Disease', 'Description']]

# 데이터 병합
merged_data = pd.merge(disease_symptoms_specialist, disease_specialist, on='Disease', how='left')
merged_data = pd.merge(merged_data, disease_description, on='Disease', how='left')

# 증상들을 각각 다른 컬럼으로 분리
symptoms_split = merged_data['Symptoms'].str.split(',', expand=True)
merged_data = merged_data.drop(columns=['Symptoms']).join(symptoms_split)

# Description 컬럼을 맨 뒤로 이동
description_column = merged_data.pop('Description')
merged_data['Description'] = description_column

# 중복 제거
merged_data = merged_data.drop_duplicates()

# 저장 경로 설정
csv_output_path = r'result/disease_symptoms_specialist_unique.csv'
json_output_path = r'result/disease_symptoms_specialist_unique.json'
merged_data.to_csv(csv_output_path, index=False, encoding='utf-8')
merged_data.to_json(json_output_path, orient='records', lines=True, force_ascii=False)

print("전처리가 완료되었습니다.")
