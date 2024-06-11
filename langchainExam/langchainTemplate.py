# 라이브러리 불러오기
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import apiKey


# 질문을 템플릿으로 구성
template = '{country}의 수도는 어디야 ?'

# 채팅 객체생성
llm = ChatOpenAI(
    temperature=1.2,
    max_tokens=2048,
    model_name='gpt-3.5-turbo',
)

# 템플릿 설정
prompt = PromptTemplate(template=template, input_variables=['country'])

llm_chain = LLMChain(prompt=prompt, llm=llm)

# 실제 처리하는 과정
# rst = llm_chain.run(country='미국')

# print(rst)

# 원하는 결과를 동시에 처리하는 과정
inputs = [
	{'country' : '미국'},
	{'country' : '대한민국'},
	{'country' : '일본'},
	{'country' : '스페인'},
]

# 한꺼번에 결과를 배열로 처리
# rst = llm_chain.apply(inputs)
# for i, result in enumerate(rst):
#     print(f"Input: {inputs[i]['country']}, Output: {result['text']}")
    
# generate()를 이용하여 상세정보를 추출하는 방법
gen_rst = llm_chain.generate(inputs)
print(gen_rst)
# 토큰 금액
print(gen_rst.llm_output)