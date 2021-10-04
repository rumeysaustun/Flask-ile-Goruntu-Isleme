#Aşağıdaki kod diğer .htm kodları ile birlikte kullanılmaktadır.
from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)

@app.route("/otsu")
def otsu():
    return render_template("otsu.htm")

@app.route("/otsu_gri")
def otsu_gri():
    return  render_template("otsu_gri.htm")

@app.route("/otsu_yeni")
def otsuyeni():
    return render_template("otsu_yeni.htm")

if __name__ == "__main__":
    app.run(debug=True)
