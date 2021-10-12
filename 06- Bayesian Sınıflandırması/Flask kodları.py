from flask import Flask
from flask import render_template 


app = Flask(__name__)

@app.route("/bayesian")
def bayesian():
    return  render_template ("bayesian.htm")

@app.route("/bayesian_yeni")
def bayesian_yeni():
    return render_template ("bayesian_yeni.htm")

if __name__ =="__main__":
    app.run()
