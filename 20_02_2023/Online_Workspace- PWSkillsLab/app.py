from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/square", methods=['POST'])
def square():
    if(request.method=='POST'):
        num=request.form['num1']
        result = str(int(num)**2)
    return render_template('results.html', result=result)

@app.route("/postman_action", methods=['POST'])
def square1():
    if(request.method=='POST'):
        num=request.json['num1']
        result = str(int(num)**2)
    return jsonify(result)    

if __name__=="__main__":
    app.run(host="0.0.0.0")
