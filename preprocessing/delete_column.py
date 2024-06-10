import pandas as pd

# 파일 불러오기
file_path = './data/MedEase.csv'
data = pd.read_csv(file_path)

# 컬럼에서 중복값 제거
data['Symptom'] = data['Symptom'].apply(lambda x: ' '.join(sorted(set(x.split()))))

data_deduplicated = data.drop_duplicates(subset='Symptom')

# 컬럼 분리
symptoms_split = data_deduplicated['Symptom'].str.split(expand=True)
symptoms_split.columns = [f'Symptom_{i+1}' for i in range(symptoms_split.shape[1])]

data_final = pd.concat([data_deduplicated.drop(columns=['Symptom']), symptoms_split], axis=1)

final_file_path = './data/Final_MedEase.csv'
data_final.to_csv(final_file_path, index=False)


