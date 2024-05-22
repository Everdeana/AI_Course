#########################################################################################################################
# 2024-05-10
# openAi chat API
#########################################################################################################################

# 1. 라이브러리 등록
import openai

# 2. 환경 설정
# openai 키 등록
# 원래는 리눅스 환경변수에 KEY를 넣음 --> 해킹 방지

# OPENAI_KEY = os.environment.get(OPENAI_KEY)

OPENAI_KEY = "##########################################" # 나중에 바뀔 수 있으므로 절대키

# export OPENAI_KEY = "##########################################" # 리눅스에 KEY 저장
openai.api_key = OPENAI_KEY # 키 입력

# 3. 인공지능 모델 선택
MODEL = "gpt-3.5-turbo"

#########################################################################################################################
# chatGPT 함수
#########################################################################################################################

def ChatMessage(msg):
	response = openai.ChatCompletion.create(
		model = MODEL,
		messages = [
			# {"role":"system", "content":"대답을 자세히 해주세요."}, # 시스템에서 역할 부여
			# {"role":"system", "content":"너는 축구선수야 축구에 관련된 대답만 해줘."}, # 시스템에서 역할 부여
			{"role":"system", "content":"대답을 부산 사투리로 해줘"}, # 시스템에서 역할 부여
			{"role":"user", "content":msg},
			{"role":"assistant", "content":""}
			# {"role":"assistant", "content":"축구에 관련된 내용만 대답해줘"}
		],
		temperature = 0,
	)

	# print(response) # 정보 출력
	# print(response['choices'][0]['message']['content'])
	return response['choices'][0]['message']['content']


