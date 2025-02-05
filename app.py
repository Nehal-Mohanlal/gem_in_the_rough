from flask import Flask, render_template, request
from main import GabbyGemma 
llm_methods = GabbyGemma() 

app = Flask(__name__) 


@app.route("/") 
def get_response():
    # res = llm_methods.get_gemma_response()      
    return render_template("index.html")

@app.route("/submit", methods=["POST", "GET"]) 
def input_prompt(): 
    user_text=""
    if request.method=="POST": 
        user_text = request.form['input'] 
        res = llm_methods.get_gemma_response(user_text)
        return render_template("form.html", prompt = res)
    
    return render_template("form.html")

if __name__ == '__main__':  
   app.run() 