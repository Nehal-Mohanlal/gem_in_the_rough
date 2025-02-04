import ollama 

class GabbyGemma: 
  def __init__(self):
    pass
  
  def init_response(self, prompt): 
        ollama_response = ollama.chat(
                          model="gemma2:2b", stream=True,
                          messages=[
                          {
                            'role': 'user',
                            'content': prompt,
                          }
                        ])
        
        for x in ollama_response: 
              print(x['message']['content'], end='', flush=True)
    
    
  def handle_convo(self): 
    print("hello! Please enter a propmpt") 

    while(True): 
        prompt = input("you: ")
        if prompt.lower() == "exit":
           self.init_response("I am done with the conversation")
           break
        self.init_response(prompt)  
        

GabbyGemma().handle_convo()    