# 라이브러리 불러오기
import openai
from langchain.chat_models import ChatOpenAI
import apiKey


# 채팅 객체 생성
llm = ChatOpenAI(
	temperature = 0, # 창의성(0 ~ 2)
	max_tokens = 2048, # 최대 토큰 수
	model_name = 'gpt-3.5-turbo',
)

# 질의 내용
qus = '대한민국의 수도에 대해 알려줘'
# 결과
print(f'[결과] : {llm.predict(qus)}')