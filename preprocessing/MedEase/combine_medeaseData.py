import pandas as pd

# 파일 경로 설정
file1_path = r'./result/disease_symptoms_specialist_unique.csv'
file2_path = r'./result/disease_symptoms_unique.csv'
combined_csv_output_path = r'./final/combined_disease_symptoms.csv'
combined_excel_output_path = r'./final/combined_disease_symptoms.xlsx'

# CSV 파일 로드
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# 데이터 결합
combined_df = pd.concat([df1, df2], ignore_index=True)

# CSV 파일로 저장
combined_df.to_csv(combined_csv_output_path, index=False, encoding='utf-8')

# 엑셀 파일로 저장
combined_df.to_excel(combined_excel_output_path, index=False)

print("데이터 결합 및 저장이 완료되었습니다.")
