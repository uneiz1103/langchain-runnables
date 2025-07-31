from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda

def word_count(text):
    return len(text.split())


runnable_word_counter = RunnableLambda(word_count)

result = runnable_word_counter.invoke("Hii there how are you , whats going !!")

print(result)

