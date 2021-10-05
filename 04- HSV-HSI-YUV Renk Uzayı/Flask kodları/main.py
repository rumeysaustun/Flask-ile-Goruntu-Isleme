# Buradaki kodlar diğer .htm kodları ile birlikte kullanılmaktadır. 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/HSV")
def HSV():
    return render_template("HSV.htm")

@app.route("/HSV_yeni")
def HSV_yeni():
    return render_template("HSV_yeni.htm.")

@app.route("/HSI")
def HSI():
    return render_template("HSI.htm")

@app.route('/HSI_yeni')
def HSI_yeni():
   return render_template("HSI_yeni.htm")

@app.route("/YUV")
def YUV():
    return render_template ("YUV.htm")

@app.route('/YUV_yeni')
def YUV_yeni():
   return render_template ("YUV_yeni.htm")

if __name__ == "__main__":
    app.run(debug=True)
