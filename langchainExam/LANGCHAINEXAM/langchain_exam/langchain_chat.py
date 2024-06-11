import openai
from langchain.chat_models import ChatOpenAI
import apiKey


# 채팅 객체생성
llm = ChatOpenAI(
    temperature=1.2,
    max_tokens=2048,
    model_name='gpt-3.5-turbo',
)

# 질의내용
qus = '대한민국의 수도에 대해서 알려줘'
# 결과
print(f'[결과]: {llm.predict(qus)}')