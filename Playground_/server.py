from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
# def welcome_page():
#     return render_template("index.html", color="#9fc5f8",times=3)

@app.route('/play/<int:x>') 
# def number_of_boxes(x):
#     return render_template("index.html",color="#9fc5f8",times=x)

@app.route('/play/<int:x>/<string:color>')  
def  number_of_boxes_with_color(color="#9fc5f8",x=3):
    return render_template("index.html",color=color,times=x)

if __name__=="__main__":     
    app.run(debug=True, port=5001)     