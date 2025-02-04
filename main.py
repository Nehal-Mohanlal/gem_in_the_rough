import ollama 

class GabbyGemma: 
  def __init__(self):
    pass
  
  def init_response(self, prompt):
        final_response_list = []
        ollama_response = ollama.chat(
                          model="gemma2:2b", stream=True,
                          messages=[
                          {
                            'role': 'user',
                            'content': prompt,
                          }
                        ])
        
        for x in ollama_response: 
             #print(x['message']['content'], end='', flush=True)
             final_response_list.append(x['message']['content'])
        
        cleaned_response = "".join(final_response_list).strip()
        return cleaned_response
  
  # def handle_convo(self): 
  #   print("hello! Please enter a propmpt") 

  #   while(True): 
  #       prompt = input("you: ")
  #       if prompt.lower() == "exit":
  #          response = self.init_response("I am done with the conversation")
  #          break
  #       response = self.init_response(prompt)  
        
  #   return response

  def get_gemma_response(self): 
    prompt = "hello" 
    
    response = self.init_response(prompt) 
    return response 
  
