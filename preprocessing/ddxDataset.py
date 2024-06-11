import pandas as pd
import json

# 파일 경로 설정
validate_cut_path = 'path_to_your_file/validate_cut.csv'
release_evidences_path = 'path_to_your_file/release_evidences.json'

# 데이터 파일 로드
validate_cut_df = pd.read_csv(validate_cut_path)

# JSON 파일 로드
with open(release_evidences_path, 'r') as f:
    release_evidences = json.load(f)

# 증상 코드와 설명 매핑 생성
symptom_code_to_description = {k: v['question_en'] for k, v in release_evidences.items()}
symptom_code_to_value_meaning = {k: v['value_meaning'] for k, v in release_evidences.items()}

# 증상 코드와 값을 설명으로 변환하는 함수
def replace_codes_with_descriptions_and_values(codes, mapping, value_mapping):
    if isinstance(codes, str):
        codes = eval(codes)
    replaced = []
    for code in codes:
        if '_@_' in code:
            code_part, value_part = code.split('_@_')
            code_desc = mapping.get(code_part, code_part)
            value_desc = value_mapping.get(code_part, {}).get(value_part, value_part)
            replaced.append(f"{code_desc} {value_desc}")
        else:
            replaced.append(mapping.get(code, code))
    return replaced

# 단일 값을 변환하는 함수
def replace_single_code_with_description_and_value(code, mapping, value_mapping):
    if '_@_' in code:
        code_part, value_part = code.split('_@_')
        code_desc = mapping.get(code_part, code_part)
        value_desc = value_mapping.get(code_part, {}).get(value_part, value_part)
        return f"{code_desc} {value_desc}"
    else:
        return mapping.get(code, code)

# 함수 적용
validate_cut_df['EVIDENCES'] = validate_cut_df['EVIDENCES'].apply(lambda x: replace_codes_with_descriptions_and_values(x, symptom_code_to_description, symptom_code_to_value_meaning))
validate_cut_df['INITIAL_EVIDENCE'] = validate_cut_df['INITIAL_EVIDENCE'].map(lambda x: replace_single_code_with_description_and_value(x, symptom_code_to_description, symptom_code_to_value_meaning) if isinstance(x, str) else x)

# NaN 값을 빈 문자열로 대체
validate_cut_df['INITIAL_EVIDENCE'] = validate_cut_df['INITIAL_EVIDENCE'].fillna('')

# 변환된 데이터 확인
print(validate_cut_df.head())

# 변환된 데이터 저장
output_file_path = 'path_to_your_file/updated_validate_cut_with_descriptions.csv'
validate_cut_df.to_csv(output_file_path, index=False)
