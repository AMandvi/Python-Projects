from flask import Flask, render_template,redirect, session, request
app = Flask(__name__)  
app.secret_key = "its a secret to everybody!"  # key can be any string, we need this for session to work            
    
@app.route('/')                           
def landing_page():
    return render_template('index.html') 
@app.route('/submit_answer', methods=["post"])    
def submit_answer():
    print(request.form["answer"])
    #session works as a dictionary but is not a dictionay. you can access it as a dictionary
    #key:"answer"=value
    #print(request.form["answer"])
    session["answer"] = request.form["answer"]
    session["incorrect"] = ""

    progress = ""
    for letter in request.form["answer"]:
        if letter == " ":
            progress += " "
        else:
            progress += "_"  
    session["progress"] = progress 
    return redirect("/game")

@app.route("/game")    
def game(): 
    if"answer" not in session:
        return redirect('/')

    print(session["answer"])
    return render_template("game.html")

@app.route("/reset")    
def reset():
    del session["answer"]
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True, port=5002)                   
