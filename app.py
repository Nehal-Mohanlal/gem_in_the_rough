from flask import Flask, render_template, request, redirect, url_for, session
from main import GabbyGemma 
llm_methods = GabbyGemma() 

app = Flask(__name__) 
app.secret_key ="655321"

@app.route("/") 
def get_response():   
    return render_template("index.html")

@app.route("/submit", methods=["POST", "GET"]) 
def input_prompt(): 
     res = ""
     if "chat" not in session: 
         session["chat"] = [] 
    
     if request.method =="POST": 
         user_text = request.form.get("input", "").strip() 
         
         if user_text: 
             session["chat"].append({"sender":"user", "message":user_text})
             res = llm_methods.get_gemma_response(user_text) 
             
             session["chat"].append({"sender":"bot", "message":res}) 
             session.modified = True 
         return redirect(url_for('input_prompt')) 
     
     return render_template("form.html", chat = session["chat"])   


@app.route("/clear", methods=["GET"])
def clear_chat(): 
    session.pop("chat", None) 
    return redirect(url_for('input_prompt')) 

if __name__ == '__main__':  
   app.run() 