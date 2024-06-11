# 라이브러리 불러오기
import apiKey
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# Chattong LLM 모델 생성
chat = ChatOpenAI()

##############################################################################################################################

# 실행
# rst = chat([HumanMessage(content="다음을 영어로 번역해줘 : 나는 파이썬을 존나게 혐오한다")])

# print(rst)

##############################################################################################################################

# # 메세지 교정
# messages = [
# 	# SystemMessage : 역할 부여
# 	SystemMessage(content="너는 10년된 대학병원의 내과전문의야. 내가 질문하는 의학에 관련된 질문에 대해서 최대한 자세하게 대답해줘."),
# 	# 문의
# 	HumanMessage(content="숨을 깊게 들이쉴 때 가슴통증이 더 커져요")
# ]

# rst = chat(messages)

# print(rst)

##############################################################################################################################

while True:
    msg = input('끝말을 입력하세요 : ')
    chatmsg = [
        # 문의
        SystemMessage(content="이제 나랑 끝말잇기 할거야. 처음 시작할때 단어를 먼저 말해줘."),
        HumanMessage(content=msg)
    ]

    rst = chat(chatmsg)
    print(rst)

