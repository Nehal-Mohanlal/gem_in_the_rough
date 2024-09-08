from langchain_ollama import OllamaLLM 

model = OllamaLLM(model="gemma2:2b")

result = model.invoke(input = "Can you give me some fantasy book recommendations, around 10?") 
print(result) 

