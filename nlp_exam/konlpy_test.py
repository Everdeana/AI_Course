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


# 한국어 불용어 처리
kor_word = """클린스만호가 요르단에 무너지며 64년 만의 아시안컵 우승 꿈을 이루지 못했죠. 해외 언론들도 "이변이 일어났다"며 일제히 주목했습니다. 로이터통신과 영국 가디언은 클린스만 감독에 대해 "요르단의 압박과 유연한 공격에 아무런 답을 찾지 못했다"고 한목소리로 지적했습니다. 미국 스포츠 전문 매체 디애슬레틱도 "전술적인 계획이 부족해 최악의 경기력을 만들었다"고 비판했습니다. 독일 슈피겔은 클린스만 감독의 잦은 외유 논란을 언급하며 "독일 감독을 맡았을 때와 비슷하다"고 평가했습니다. 영국 BBC와 중국 소후닷컴은 "김민재의 공백이 결정적이었다"며 수비 불안을 패인으로 꼽았습니다. 일본 언론들도 한국 4강 탈락 소식을 일제히 보도했습니다. 닛칸스포츠는 "요르단이 지난달 일본과의 친선 경기에서 6대1로 대패한 국가"라고 소개했고, 스포니치아넥스는 "한국은 네 경기 연속 후반 추가시간에 득점했지만, 이번엔 기적이 일어나지 않았다"고 전했습니다."""
stop_words = "의 과 가 를 악성 루머 최악 탈락 불안 논란 비판"

# 조사, 접속사 제거
stop_words = stop_words.split(' ')
word_tokens = okt.morphs(kor_word)
print("word_tokens")
print(word_tokens)
print("-"*140)

# 불용어에 해당하는 경우 제거
# word_tokens에 있는 단어를 word에 저장 -> 만약 stop_words에 있는 단어가 word에 존재하지 않는다면 -> 그 데이터를 result에 저장
result = [word for word in word_tokens if not word in stop_words] # 람다 함수 처리
print("불용어 제거 후 단어들")
print(result)
print("-"*140)

