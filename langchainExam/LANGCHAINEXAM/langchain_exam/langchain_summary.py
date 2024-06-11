# 라이브러리
from langchain.memory import ConversationSummaryBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
import apiKey


# 시스템역활 설정
system_template = SystemMessagePromptTemplate.from_template(
    "내용을 확인하고 요약해줘.\n{trans}"
)

system_message = system_template.format(trans="""
"인공지능, 의사도 대체 가능...사회적 능력 계발 정책 변화 시급"

지난 10여년동안 의사소통 능력 등이 중요시되는 사회적 기술 일자리 비중이 증가하고, 이와 관련한 임금도 상승한 것으로 조사됐다. 또 인공지능(AI) 기술이 발달하면서 직업훈련과 교육 측면에서 사회적 능력을 계발할 수 있는 정책 변화가 시급하다는 의견도 나왔다. 
10일 한국은행은 오삼일 한은 조사국 고용분석팀장 등이 작성한 'BOK 이슈노트 : 노동시장에서 사회적 능력의 중요성 증가'를 발간하고, 이 같은 내용을 공개했다. 
보고서를 보면, 지난 2008~2022년 중 사회적 기술 집중 일자리 비중은 49%에서 56%로 7%포인트 상승했다. 반면 수학적(인지적) 기술 집중 일자리 비중은 50%에서 55%로 5%포인트 오르는데 그쳤다. 
오 팀장은 "전반적으로 우리나라 노동시장이 고숙련·고기술 일자리 중심으로 변화하는 가운데, 사회적 기술이 필요한 업무가 많은 일자리가 크게 늘었다"며 "지난 14년간 노동시장에서 수학적 기술보다는 사회적 기술의 중요성이 상대적으로 더 높아진 것"이라고 말했다.
사회적 능력에 대한 임금 보상도 늘었다. 개인의 사회적 능력이 1단위 높을 때 임금이 2007~2015년 중에는 4.4% 높고, 2016~2020년 중에는 5.9% 높은 것으로 추정됐다. 반면,인지적 능력이 1단위 높을 때는 임금이 2007~2015년 중 10.9% 높았지만, 2016~2020년 중에는 9.3% 높은 것으로 나타났다. 
의사도 인공지능 대체 가능성 높아져..."교육·직업훈련 정책 변화 시급"
오 팀장은 "최근 들어 사회적 능력에 대한 임금 보상은 과거보다 더 유의하게 높아진 반면 인지적 능력에 대한 임금 보상은 과거에 비해 낮아진 것"이라고 설명했다. 
사회적 능력의 중요성이 높아진 배경에는 인공지능의 발전이 있었다. 연구팀은 관련 문헌을 소개하면서 "병원에서 질병을 진단하고, 치료 계획을 세우는 등 기존에 고숙련 노동자가 수행하던 업무 또한 대체될 가능성이 높아졌다"며 "또한 고차원적 사고를 요구하는 고기술 업무 또한 정형화한 논리 구조를 가지기 때문에 컴퓨터에 의해 대체될 수 있다"고 밝혔다. 
이어 "직관, 판단력, 창의력, 유연성 등 인간의 암묵적인 지식은 명확하게 규칙화하기 어렵기 때문에 자동화 기술로 대체하기 어렵다"고 덧붙였다. 
연구팀은 앞으로 사회적 능력을 계발하는 것이 교육·직업훈련 측면에서 더욱 중요질 것으로 봤다. 오 팀장은 "자동화 기술의 대체 효과가 특정 직무나, 특정 일자리에 집중한다는 측면에서 개인의 자기계발에 대한 변화, 관련 정책의 변화가 시급하다고 판단한다"고 말했다. 
그러면서 "그렇지만 인지적 능력의 중요성을 간과하는 것은 아니다"라며 "최근 들어 전문 지식을 바탕으로 설득 능력이 있고, 매니지를 할 수 있는 사람과 관련 일자리가 가장 많이 늘어났기 때문에 인지 능력은 여전히 중요하다"고 했다. 
""")

# 템플릿 정의
prompt = ChatPromptTemplate.from_messages([
    system_message, # 가장 중요한 꼭 처리해야하는 내용
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{human_input}"),
])

# llm 모델 선언
llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.5,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# 메모리
memory = ConversationSummaryBufferMemory(
    llm=llm,
    memory_key="chat_history",
    max_token_limit=10,
    return_messages=True
)

# 결과 처리
convchat = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

# 실행
rst = convchat({'human_input':'기사내용을 초등학생도 이해할수 있는 정도로 쉽게 설명해줘.'})
print(rst)