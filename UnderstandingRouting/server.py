from flask import Flask
app = Flask(__name__)    

@app.route('/')         
def hello_world():
    return 'Hello World!'

@app.route('/dojo')         
def dojo():
    return 'Dojo'    

@app.route('/say/<name>')    
def hi_name(name):
    return f"Hi, {name}!"

@app.route('/repeat/<int:times>/<string:word>')
def word_times(word,times):
    return f"<p>{word}<p>"* times


if __name__=="__main__":    
    app.run(debug=True, port=5001)    