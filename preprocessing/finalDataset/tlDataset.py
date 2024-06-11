# 라이브러리 설치
# pip install googletrans==4.0.0-rc1

# 라이브러리 불러오기
import json
import re
import time
from googletrans import Translator

# 파일 경로
input_file_path = r'finalDataset/diseases_symptoms.json'
output_file_path = r'finalDataset/diseases_symptoms_processed.json'
translated_file_path = r'finalDataset/diseases_symptoms_processed_translated.json'

# 데이터 전처리 함수
def preprocess_data(data):
    # 'input' 및 'reference' 값이 비어있으면 해당 컬럼을 제거
    for key in ["input", "reference"]:
        if data.get(key) == "":
            del data[key]
    
    # 모든 값에서 괄호와 괄호 안의 텍스트를 제거 및 ':'를 공백으로 변경
    for key in data:
        data[key] = re.sub(r'\s*\(.*?\)\s*', '', data[key])  # 괄호 및 괄호 안의 텍스트 제거
        data[key] = data[key].replace(':', ' ')  # ':'를 공백으로 변경
    
    return data

# 파일에서 JSON 데이터 불러오기
with open(input_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 각 항목에 대해 데이터 전처리 적용
processed_data = [preprocess_data(item) for item in json_data]

# 전처리된 데이터 파일에 저장
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(processed_data, file, indent=4, ensure_ascii=False)

print(f"전처리가 완료되었습니다. 전처리된 파일이 {output_file_path}에 저장되었습니다.")

# 번역기 초기화
translator = Translator()

# 데이터 번역 함수
def translate_data(data, src='en', dest='ko'):
    translated_data = {}
    for key, value in data.items():
        try:
            translated = translator.translate(value, src=src, dest=dest).text
            translated_data[key] = translated
        except Exception as e:
            print(f"Error translating key '{key}' with value '{value}': {e}")
            translated_data[key] = value  # 번역 실패 시 원본 값을 유지
    return translated_data

# 전처리된 데이터 불러오기
with open(output_file_path, 'r', encoding='utf-8') as file:
    processed_data = json.load(file)

# 전체 데이터 수
total_items = len(processed_data)

# 각 항목에 대해 데이터 번역 적용 및 확인
translated_data = []
failed_items = []

# 번역 시도 및 예외 처리
for index, item in enumerate(processed_data):
    try:
        translated_item = translate_data(item)
        translated_data.append(translated_item)
    except Exception as e:
        print(f"Error translating item at index {index}: {e}")
        failed_items.append(item)
    print(f"전체 데이터 수: {total_items}, 번역 중인 데이터 인덱스: {index + 1}")
    print("-" * 50)

# 할당량 초과 오류가 발생한 데이터 청크 단위로 번역
chunk_size = 100  # 한 번에 처리할 데이터 수
for start_idx in range(0, len(failed_items), chunk_size):
    end_idx = min(start_idx + chunk_size, len(failed_items))
    chunk = failed_items[start_idx:end_idx]
    for index, item in enumerate(chunk, start=start_idx):
        try:
            translated_item = translate_data(item)
            translated_data.append(translated_item)
        except Exception as e:
            print(f"Error translating chunk item at index {index}: {e}")
            translated_data.append(item)  # 번역 실패 시 원본 데이터를 저장
        print(f"할당량 초과 데이터 수: {len(failed_items)}, 번역 중인 데이터 인덱스: {index + 1}")
        print("-" * 50)
    time.sleep(2)  # 각 청크 사이에 지연 시간 추가

# 번역된 데이터 파일에 저장
with open(translated_file_path, 'w', encoding='utf-8') as file:
    json.dump(translated_data, file, indent=4, ensure_ascii=False)

print(f"번역이 완료되었습니다. 번역된 파일이 {translated_file_path}에 저장되었습니다.")
