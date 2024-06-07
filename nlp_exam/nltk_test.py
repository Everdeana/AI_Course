# 라이브러리 설치
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# 필요한 라이브러리 온라인에서 다운로드
# 텍스트에서 단어 숫자, 단어 빈도, 어휘 다양도 같은 통계적
nltk.download('punkt')

# 토크나이저(Tokenization) 토큰화
text = """Mbappé has long been connected with a move to Madrid, even before he signed a two-year contract extension with a player option for a third year with PSG in 2022. He played more than 300 games for the club, scoring his 250th goal in March and winning the Ligue 1 title a month later. Despite his considerable success in domestic competitions Mbappé has won six league titles with PSG and one with his previous club, AS Monaco the forward is yet to add a Champions League title to his list of career achievements, which also includes winning the World Cup with France in 2018."""

# 문단을 문장으로 분리
for idx, sent in enumerate( sent_tokenize(text)):
	i = idx + 1
	print("-"*140)
	print(f'{i} 번째 문장 : {sent}')

	# 문장을 단어로 분리
	print("")
	print("단어 : ", word_tokenize(sent))

print("-"*140)