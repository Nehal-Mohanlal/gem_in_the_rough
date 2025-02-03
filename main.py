import ollama 

def handle_convo(): 
    print("hello! Please enter a propmpt") 

    while(True): 
        prompt = input("you: ")
        if prompt.lower() == "exit": 
          break 
        ollama_response = ollama.chat(
                          model="gemma2:2b", stream=True,
                          messages=[
                          {
                            'role': 'user',
                            'content': prompt,
                          }
                        ])
        print("\n")
        for x in ollama_response: 
            print(x['message']['content'], end='', flush=True) 
        
        
handle_convo()