from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate 


# template for prompt, needs more research on my part
template = """
Answer the question below.

Here is the conversation history {context}. 

Question: {question} 

Answer
"""
#Which world destroying AI shall we use? 
#Gemma is really cool + the 2b can run on my PC XD 
model_name = "gemma2:2b"

#initialize the model
model = OllamaLLM(model=model_name,streaming=True)

#Structure the prompt. 
prompt = ChatPromptTemplate.from_template(template) 

#Chain (Connect) the model to the prompt. 
chain = prompt | model 

## How we handle the conversation 
def handle_convo(): 
    context = "" 
    print("Hi, welcome! Type 'exit' to exit") 
    
    while(True): 
        user_input = input("you: ") 
        if user_input.lower() =="exit":
            break 
        result = chain.invoke({"context":context, "question":user_input})
         
        print("Gemma: ", result) 
        
        ## store the conversation history
        context += f"\n User:{user_input} \n AI: {result}" 
        
        
#Call main function
handle_convo() 
