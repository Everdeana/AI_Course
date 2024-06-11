# 라이브러리 불러오기
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import apiKey

# 채팅 객체생성
llm = ChatOpenAI(
    temperature=1.2,
    max_tokens=2048,
    model_name='gpt-3.5-turbo',
)

# 받침 유무 확인 함수
def has_final_consonant(word):
    if not word:
        return False
    last_char = word[-1]
    return (ord(last_char) - 44032) % 28 != 0

# 템플릿 멀티 변수를 받도록 변경
def generate_template(city1, city2):
    if has_final_consonant(city1):
        template = f"{city1}과 {city2}의 거리는 얼마나 되지?"
        print(template)
    else:
        template = f"{city1}와 {city2}의 거리는 얼마나 되지?"
        print(template)
    return template

# 템플릿 설정 및 실행
def run_chain(city1, city2):
    template = generate_template(city1, city2)
    prompt = PromptTemplate(template=template, input_variables=['city1', 'city2'])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(city1=city1, city2=city2)

# 사용자 입력받기
def get_city_names():
    print("***************거리 확인***************")
    city1 = input("첫 번째 도시 이름을 입력하세요: ")
    city2 = input("두 번째 도시 이름을 입력하세요: ")
    return city1, city2

# 실제 처리하는 과정
city1, city2 = get_city_names()
rst = run_chain(city1, city2)

print(rst)
