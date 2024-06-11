import json
import pandas as pd

# 경로 설정
input_json_path = r'./combined_disease_prediction_symptom_processed.json'
input_csv_path = r'./MedEaseSeparate.csv'
unique_csv_output_path = r'./MedEaseSeparate_unique.csv'
unique_json_output_path = r'./MedEaseSeparate_unique.json'
final_combined_csv_path = r'./final_combined_diseases_symptoms.csv'
final_combined_json_path = r'./final_combined_diseases_symptoms.json'

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

df_diseases_symptoms = pd.DataFrame({
    "Disease": diseases,
    "Combined_Symptoms": symptoms,
    "Specialist": "General Practitioner"  # 추가된 열
})

# 중간 CSV 및 JSON 파일로 저장
df_diseases_symptoms.to_csv(unique_csv_output_path, index=False)
df_diseases_symptoms.to_json(unique_json_output_path, orient='records', lines=True)

# 2. CSV 파일 중복값 제거
df_csv = pd.read_csv(input_csv_path)

# 모든 증상 열을 하나의 문자열로 결합
df_csv['Combined_Symptoms'] = df_csv[['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4', 'Symptom_5', 'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9', 'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14', 'Symptom_15', 'Symptom_16', 'Symptom_17']].fillna('').agg(', '.join, axis=1)

# 'Disease'와 'Combined_Symptoms' 열을 기준으로 중복값 제거
df_csv.drop_duplicates(subset=['Disease', 'Combined_Symptoms'], inplace=True)

# Remove 'unknown' text from the dataframe
df_csv.replace('unknown', '', inplace=True)

# Fill missing specialist data
df_csv['Allergist'].fillna('General Practitioner', inplace=True)

# Combine both dataframes
combined_df = pd.concat([df_csv.rename(columns={'Allergist': 'Specialist'}), df_diseases_symptoms], ignore_index=True)

# Remove duplicates based on 'Disease' and 'Combined_Symptoms' columns
combined_df.drop_duplicates(subset=['Disease', 'Combined_Symptoms'], inplace=True)

# Create a list of unique symptoms
all_symptoms = combined_df['Combined_Symptoms'].str.split(', ', expand=True).stack().unique()

# Count the occurrences of each symptom in the combined dataset
symptom_counts = {symptom: combined_df['Combined_Symptoms'].str.contains(symptom).sum() for symptom in all_symptoms}

# Save the combined data to a new CSV file
combined_df.to_csv(final_combined_csv_path, index=False)

# Save the combined data to a new JSON file
combined_df.to_json(final_combined_json_path, orient='records', lines=True)

# 증상 종류 리스트 및 증상 개수 출력
print(f"Unique symptoms: {all_symptoms}")
print(f"Symptom counts: {symptom_counts}")
