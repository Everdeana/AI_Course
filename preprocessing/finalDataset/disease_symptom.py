import json
import pandas as pd

# 경로 설정
input_json_path = r'./combined_disease_prediction_symptom_processed.json'
input_csv_path = r'./MedEaseSeparate.csv'
intermediate_csv_path = r'./diseases_symptoms.csv'
intermediate_json_path = r'./diseases_symptoms.json'
unique_csv_output_path = r'./MedEaseSeparate_unique.csv'
unique_json_output_path = r'./MedEaseSeparate_unique.json'

# 1. JSON 파일을 CSV 및 JSON 파일로 변환
with open(input_json_path, 'r') as file:
    data = json.load(file)

diseases = []
symptoms = []

for entry in data:
    if "symptoms of" in entry["instruction"].lower():
        disease = entry["instruction"].lower().replace("what are the symptoms of ", "").replace("?", "").strip()
        symptom_list = entry["output"].lower().replace("the following are the symptoms of ", "").strip()
        diseases.append(disease)
        symptoms.append(symptom_list)

df = pd.DataFrame({
    "Disease": diseases,
    "Symptoms": symptoms
})

# 중간 CSV 및 JSON 파일로 저장
df.to_csv(intermediate_csv_path, index=False)
df.to_json(intermediate_json_path, orient='records', lines=True)

# 2. CSV 파일 중복값 제거
df_csv = pd.read_csv(input_csv_path)

# 모든 증상 열을 하나의 문자열로 결합
df_csv['Combined_Symptoms'] = df_csv[['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4', 'Symptom_5', 'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9', 'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14', 'Symptom_15', 'Symptom_16', 'Symptom_17']].fillna('').agg(', '.join, axis=1)

# 'Disease'와 'Combined_Symptoms' 열을 기준으로 중복값 제거
df_unique = df_csv.drop_duplicates(subset=['Disease', 'Combined_Symptoms'])

# 고유 값을 새로운 CSV 및 JSON 파일로 저장
df_unique.to_csv(unique_csv_output_path, index=False)
df_unique[['Disease', 'Combined_Symptoms']].to_json(unique_json_output_path, orient='records', lines=True)
