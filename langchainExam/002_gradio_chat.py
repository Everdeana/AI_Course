import time
import gradio as gr
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import apiKey


# ------------------------------------------------------------------------------------
# 학습결과 불러오기
# ------------------------------------------------------------------------------------
persist_directory = 'db'
embedding = OpenAIEmbeddings()

vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)

print(vectordb)

# ------------------------------------------------------------------------------------
# Make a retriever : 결과를 만들기
# ------------------------------------------------------------------------------------
# 응답처리하기
retriever = vectordb.as_retriever(search_kwargs={'k':3})

def openai_chat(message, history):
    docs =  retriever.get_relevant_documents(message)
    
    msg = '<참고서류>' + '\n'
    
    for doc in docs:
        msg = msg + doc.metadata['source'] + '\n'
        
    return msg

# ------------------------------------------------------------------------------------
# ChatGPT 모델 수정
# ------------------------------------------------------------------------------------
# ChatGPT 모델 지정
llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0
)

# ------------------------------------------------------------------------------------
# Make a chain : 체인으로 연결하기
# ------------------------------------------------------------------------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=retriever,
    return_source_documents=True
)

def process_llm_response(llm_response):
    msg = '<AI 응답>\n'
    
    print(llm_response['result'])
    msg = msg + llm_response['result'] + '\n'
        
    print('\n\nSource:')
    msg = msg + '\n\n<참고문서>\n'
    for source in llm_response['source_documents']:
        print(source.metadata['source'])
        msg = msg + source.metadata['source'] + '\n'
        msg = msg + '<참고내용>\n'
        msg = msg + source.page_content + '\n\n'
        
    return msg

def openai_chat_ai(message, history):
    llm_response = qa_chain(message)
    print(llm_response)
    msg = process_llm_response(llm_response)
    
    return msg

gr.ChatInterface(
    openai_chat_ai,
    # chatbot=gr.Chatbot(height=200),
    title='LangChain ChatBot',
    description='자세히 물어보시면 좀 더 정확한 답변을 얻으실 수 있습니다.',
    examples=[
        "질문1", 
        "질문2", 
        "질문3"
    ],
    retry_btn="retry",
    undo_btn="undo",
    clear_btn="채팅내용 초기화"
    ).launch(
    share=False,
    server_name='0.0.0.0',
    server_port=9000
)
