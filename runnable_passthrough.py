from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

passthrough = RunnablePassthrough()

print(passthrough.invoke({'name': 'uneiz'}))
