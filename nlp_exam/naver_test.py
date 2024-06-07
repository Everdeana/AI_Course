# 라이브러리 설치
from datasets import load_dataset
from konlpy.tag import Okt
from pykospacing import Spacing

spacing = Spacing()
okt = Okt()

# 네이버 영화리뷰 다운로드
dataset = load_dataset('nsmc')

print(dataset)

# 실제 데이터 확인
for i in range(20):
	print(dataset['train'][i])

# Okt 형태소 분석기 이용해서 token 분리(단어로 분리)
print('*'*20, '형태소 단위로 분리', '*'*20)

# dataset_num = 150_000
dataset_num = 1000

# 변수로 처리
nsmc_sents = [dataset['train'][idx]['document'] for idx in range(dataset_num)]

# 실제 데이터 확인
for i in range(20):
	print(nsmc_sents[i])
'''
# 텍스트 파일로 document 저장
filePath = "document_list.txt"
with open(filePath, 'w', encoding='utf-8') as file:
	for idx, sentence in enumerate(nsmc_sents):
		file.write(f"{idx + 1}: {sentence}\n")  # 문장 앞에 번호 추가하고 줄바꿈 문자 추가
'''

# 형태소 분석기로 분리 작업
print('*'*20, '형태소 분석기 분리', '*'*20)

for sent in nsmc_sents:
	words = [w for w, p in okt.pos(sent)]

for i in range(20):
	print("sent = ", sent)
	print("words = ", words)

# 맞춤법 보정과 띄어쓰기 보정하기
tokenized_nsmc_corpus = []

print('*'*20, '한글 전처리', '*'*20)

# pykospacing 전처리
for sent in nsmc_sents:
	new_sent = spacing(sent)
	words = [w for w, p in okt.pos(new_sent)]
	
	# 단어 추가
	tokenized_nsmc_corpus.append(words)

	print("전처리 전 : ", sent)
	print("전처리 후 : ", new_sent)
	print(words)

