# 라이브러리 불러오기
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import apiKey

# huggingface 모델 불러오기
modelId = "mistralai/Mistral-7B-v0.1"


# 질의 응답
q = "Who is Son Heung Min?"

# template
template = """Question : {question}

Answer:"""


# 템플릿 설정
prompt = PromptTemplate(template=template, input_variables=['question'])

# llm 모델을 허깅페이스 모델로 교체
llm = HuggingFaceHub(
    repo_id = modelId,
	model_kwargs = {
		"temperature" : 0.2,
		"max_length" : 128
	}
)

# 모델 객체를 생성 
llmChain = LLMChain(prompt = prompt, llm = llm)

# 실행
rst = llmChain.run(question=q)
print(rst)



