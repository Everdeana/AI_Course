# 표제어 추출, 어간 추출
import nltk
from nltk.stem import WordNetLemmatizer # 표제어 추출
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords


# 필요한 라이브러리
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

words = ['policy','doing','organization','have','going','love','lives','fly','dies','watched','has','starting']

# 표제어 추출
print("-"*140)
print("단어 : ", words)
print("표제어 : ", [lemmatizer.lemmatize(word) for word in words]) # 람다함수
print("-"*140)

# 100% 완벽하지 않기 때문에 품사 정보 추출 -> ex) 'dies' : 'dy'

# 품사 정보 추출
print("품사 정보 추가(doing) : ", lemmatizer.lemmatize('doing', 'v'))
print("품사 정보 추가(dies) : ", lemmatizer.lemmatize('dies', 'v'))
print("품사 정보 추가(watched) : ", lemmatizer.lemmatize('watched', 'v'))
print("품사 정보 추가(has) : ", lemmatizer.lemmatize('has', 'v'))
print("-"*140)

# 어간 추출 함수 설정
porterStemmer = PorterStemmer()
lancasterStemmer = LancasterStemmer()

text = """Mbappé has long been connected with a move to Madrid, even before he signed a two-year contract extension with a player option for a third year with PSG in 2022. He played more than 300 games for the club, scoring his 250th goal in March and winning the Ligue 1 title a month later. Despite his considerable success in domestic competitions Mbappé has won six league titles with PSG and one with his previous club, AS Monaco the forward is yet to add a Champions League title to his list of career achievements, which also includes winning the World Cup with France in 2018."""

tokenized_sentence = word_tokenize(text)

# 어간 추출
print("어간(Porter):", [porterStemmer.stem(word) for word in tokenized_sentence])
print("-"*140)
print("어간(Lancaster):", [lancasterStemmer.stem(word) for word in tokenized_sentence])
print("-"*140)

# 불용어 리스트
stopwordsList = stopwords.words("english")
print("불용어 리스트")
print(stopwordsList)