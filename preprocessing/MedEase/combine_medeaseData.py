import pandas as pd

# 파일 경로 설정
file1_path = 'result//disease_symptoms_specialist_unique.csv'
file2_path = 'result/disease_symptoms_unique.csv'
combined_csv_output_path = 'final/combined_disease_symptoms_final.csv'
combined_json_output_path = 'final/combined_disease_symptoms_final.json'

# CSV 파일 로드
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# df2의 컬럼들을 df1의 끝에 추가
combined_df = pd.concat([df1, df2], ignore_index=True)

# 중복 제거
combined_df_unique = combined_df.drop_duplicates()

# CSV와 JSON 파일로 저장
combined_df_unique.to_csv(combined_csv_output_path, index=False, encoding='utf-8')
combined_df_unique.to_json(combined_json_output_path, orient='records', lines=True, force_ascii=False)

print("데이터 결합 및 저장이 완료되었습니다.")
