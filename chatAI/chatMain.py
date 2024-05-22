#########################################################################################################################
# 2024-05-10
# openAi chat API
#########################################################################################################################

# openAI 채팅 함수 불러오기
from chat import ChatMessage
from dbAdd import ChatGPTadd

while True:
	msg = input("질문 : ")
	rst = ChatMessage(msg) # result

	# DB에 저장
	ChatGPTadd(msg, rst)
	print("답변 : ", rst)
