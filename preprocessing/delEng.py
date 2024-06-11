import pandas as pd
import re
import json

# 파일 경로 설정
file_path = r'./combined_disease_prediction_symptom_translated.json'

# JSON 파일을 읽어옵니다.
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 데이터프레임으로 변환합니다.
df = pd.DataFrame(data)

# 영어 문장을 포함하는 레코드를 찾기 위한 정규식 패턴을 정의합니다.
english_pattern = re.compile(r'[A-Za-z]')

# 영어 문장이 있는 레코드를 삭제합니다.
filtered_df = df[~df['instruction'].apply(lambda x: bool(english_pattern.search(x))) & ~df['output'].apply(lambda x: bool(english_pattern.search(x)))]

# 필터링된 데이터를 다시 JSON 형태로 변환합니다.
filtered_data = filtered_df.to_dict(orient='records')

# 필터링된 데이터를 새로운 JSON 파일로 저장합니다.
filtered_file_path = r'D:\ai_exam\AI_Course\preprocessing\filtered_combined_disease_prediction_symptom_translated.json'
with open(filtered_file_path, 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)

print("영어 문장이 포함된 레코드는 삭제되었습니다.")
