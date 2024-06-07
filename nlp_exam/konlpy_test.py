# 라이브러리
import konlpy
from konlpy.tag import Okt
from konlpy.tag import Kkma

# 클래스를 변수로 받아서 사용
okt = Okt()
kkma = Kkma()

text = """레알 마드리드는 4일(한국시간) 홈페이지에 "음바페와 계약에 합의했다. 음바페는 앞으로 5년 동안 레알 마드리드의 선수가 된다"고 알렸다. 이어 "지난 시즌 파리 생제르맹(PSG·프랑스)에서 자신의 한 시즌 최다 골(44골)을 기록하는 등 6차례나 득점왕을 차지한 음바페를 영입해 팀 스쿼드를 강화했다"고 덧붙였다. 이로써 음바페는 자유계약(FA) 신분으로 이적료 없이 PSG를 떠나 레알 마드리드에서 2028-2029시즌까지 활약하게 됐다. 음바페는 계약 발표와 함께 자신의 사회관계망서비스(SNS)에 "꿈이 이뤄졌다. 나의 '꿈의 팀' 레알 마드리드에 합류해 기쁘고 자랑스럽다"라며 "내가 지금 얼마나 흥분되는지 아무도 모를 것이다. 레알 마드리드 팬들을 빨리 만나고 싶다"고 소감을 남겼다."""

# Okt 형태소 분석
print("-"*140)
print("형태소 분석(Okt)")
print(okt.morphs(text))
print("-"*140)
print("품사 태깅(Okt)")
print(okt.pos(text))
print("-"*140)
print("명사 태깅(Okt)")
print(okt.nouns(text))

# Kkma 형태소 분석
print("#"*140)
print("형태소 분석(Kkma)")
print(kkma.morphs(text))
print("-"*140)
print("품사 태깅(Okt)")
print(kkma.pos(text))
print("-"*140)
print("명사 태깅(Okt)")
print(kkma.nouns(text))

print("-"*140)
