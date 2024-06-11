# 라이브러리 불러오기
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import apiKey


# 채팅 객체생성
llm = ChatOpenAI(
    temperature=0,
    max_tokens=2048,
    model_name='gpt-3.5-turbo',
)

# 템플릿 멀티변수를 받도록 변경
template = "{city1}과 {city2}의 거리는 얼마나 되지 ?"

# 템플릿 설정
prompt = PromptTemplate(template=template, input_variables=['city1','city2'])

llm_chain = LLMChain(prompt=prompt, llm=llm)

rst = llm_chain.run(city1='서울', city2='목포')
print(rst)