from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'no secret on github' # set a secret key for security purposes

@app.route('/') #DISPLAY ROUTE
def display_form():
    return render_template("form.html")

@app.route('/process',methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def display_results():
    if not 'name' in session:
        session['name'] = " Name Not provided"  
    if not 'location' in session:
        session['location'] = " Location Not provided" 
    if not 'language' in session:
        session['language'] = " Language Not provided" 
    if not 'comment' in session:
        session['comment'] = " Comment Not provided"
    return render_template("display.html")

    






if __name__=="__main__":    
    app.run(debug=True, port=5001)