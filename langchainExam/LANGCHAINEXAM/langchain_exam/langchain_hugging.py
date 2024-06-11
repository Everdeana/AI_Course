# 라이브러리 불러오기
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import apiKey



# 허깅페이스 모델불러오기
model_id = "mistralai/Mistral-7B-v0.1"

# 질의 응답
q = "Who is Son Heung Min ?"

# 템플릿
template = """Question : {question}

Answer:"""

# 템플릿 설정
prompt = PromptTemplate(template=template, input_variables=['question'])

# llm 모델을 허깅페이스 모델로 교체
llm = HuggingFaceHub(
    repo_id=model_id,
    model_kwargs={
        "temperature" : 0.2,
        "max_length" : 128
    }
)

# 모델 객체를 생성
llm_chain = LLMChain(prompt=prompt, llm=llm)

# 실행
rst = llm_chain.run(question=q)
print(rst)