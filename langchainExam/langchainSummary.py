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

# 시스템역할 설정
system_template = SystemMessagePromptTemplate.from_template(
	"내용을 확인하고 한글 5줄로 요약해줘.\n{trans}"
)
system_message = system_template.format(trans = """
	A penalty shootout was all that stood between England and European Championship glory in 2021.
	Having endured a painful defeat by Italy in the final at Wembley Stadium, it was hard not to wonder if the Three Lions had just thrown away their best opportunity of major tournament success.
	Perhaps not though.
	According to Opta's pre-tournament projections for Euro 2024, the window of victory remains very much open for Gareth Southgate's side this summer…
	It's rare for England to head to a major international tournament as outright favourites, but that is precisely the situation this time according to Opta's prediction model.
	Southgate's side sit top of the pack of projected winners, with a 19.9% chance of going on to lift the trophy in Germany.
	While the news will no doubt be warmly welcomed by many, you're probably now wondering how exactly we've arrived at that outcome… and it's a fair question.
	To achieve a more well-rounded picture of who will go on to win the tournament, Opta's prediction model estimates the probability of each match outcome - win, draw or loss - by using betting market odds and our own team rankings.
	The odds and rankings are based on historical and recent team performances, while the model then considers opponent strength and the difficulty of their path to the final by using match outcome probabilities, taking into account the composition of the groups and seedings into the knockout stages.
	While the Opta predictor puts England in first position, it is France - the team who knocked them out of the 2022 World Cup - who are hot on their heels at the top end of the charts.
	With a 19.1% chance for Didier Deschamps' side to win Euro 2024, there’s a legitimate feel of a 'big two' meeting in the final.
	In fact, the model estimates that both teams have almost a one-in-two chance of making the semi-finals, with England at 48.2% and France at 48.1% respectively, to be among the final four.
	Beyond them, hosts Germany are the team who round out the top three in terms of projected champions.
	Julian Nagelsmann's side have a 12.4% chance of being victorious on home soil, and are the last of the three sides with a better than 10% likelihood of lifting the trophy.
	As for those who look the surest bets to make some noise in the knockout stages, England, France, Germany, Spain, and Portugal are the five teams given a 50% or better chance of reaching at least the quarter-finals.
	Elsewhere from a British perspective, the outlook for Scotland isn't quite as optimistic.
	Steve Clarke's men will have it all to do to secure qualification in Group A, which looks primed to be one of most evenly-matched groups in the tournament overall.
	According to the predictor, Scotland have a 58.9% chance of reaching the last 16, whether that's finishing in the top two or as one of the best third-placed sides.
	The big problem for them is that, along with Group A favourites Germany, both Switzerland (61%) and Hungary (59.3%) are very similarly placed to make it to the knockout stages too.
	The competition will be fierce for the Tartan Army, and things will be tricky from the off as their tie with hosts Germany gets the competition under way on 14 June.
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