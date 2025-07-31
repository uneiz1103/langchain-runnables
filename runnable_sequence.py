from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv


load_dotenv()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain me this {text}',
    input_variables=['text']
)

parser = StrOutputParser()


chain = RunnableSequence(prompt1 , model, parser, prompt2, model, parser)

# Recommended (Better Style)
# chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'AI'})

print(result)


