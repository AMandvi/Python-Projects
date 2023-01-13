from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def playground():
    return render_template('index.html', times=3, box_color='blue')  

@app.route('/play/<int:num>')    
def num_of_boxes(num):
    return render_template('index.html', times=num, box_color='blue')

@app.route('/play/<int:num>/<string:color>')   
def color_and_num_boxes(num,color):
    return render_template('index.html',times=num, box_color=color)

if __name__=="__main__":
    app.run(debug=True)                   

