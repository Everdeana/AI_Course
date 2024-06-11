from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
import apiKey

# Chatting LLM 모델 생성
chat = ChatOpenAI()

# 실행
# rst = chat(
#     [HumanMessage(content="다음을 영어로 번역해줘: 나는 파이썬을 좋아한다.")]
# )

# print(rst)

# 메시지 교정
while True:
    msg = input('끝말을 입력하세요 : ')
    chatmsg = [
        # 문의
        SystemMessage(content="이제 나랑 끝말잇기 할거야. 처음 시작할때 단어를 먼저 말해줘."),
        HumanMessage(content=msg)
    ]

    rst = chat(chatmsg)
    print(rst)
