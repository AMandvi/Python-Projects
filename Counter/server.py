from flask import Flask, render_template,redirect, session, request
app = Flask(__name__) 
app.secret_key = "its a secret to everybody!" 

@app.route('/')
def counter():
    if "visit" in session:
        print(session["visit"])
        session["visit"]+=1
    else:
        session["visit"]=1
    return render_template("index.html")

@app.route("/count/post", methods=["post"])
def count_submit():
    session["visit"]+=1
    return redirect("/count")

@app.route("/count")    
def count():
    return render_template("index.html")

@app.route("/reset/post", methods=["post"])
def reset():
    session.clear()
    return redirect("/")
@app.route("/destroy_session")    
def destroy_session():
    session.clear()
    return redirect("/")
    
if __name__== "__main__":
    app.run(debug=True, port=5001)