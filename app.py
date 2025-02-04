from flask import Flask 
from main import GabbyGemma 
llm_methods = GabbyGemma() 

app = Flask(__name__) 



@app.route("/") 
def get_response():
    res = llm_methods.get_gemma_response() 
    return res     

if __name__ == '__main__':  
   app.run() 