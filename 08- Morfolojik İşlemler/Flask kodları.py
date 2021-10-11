# Bu Flask kodları diğer .htm dosyaları ile birlikte kullanılmaktadır.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/asinma")
def asinma():
    return render_template("asinma.htm")

@app.route("/genlesme")
def genlesme():
    return render_template ("genlesme.htm")

@app.route("/gri_asinma_genlesme")
def gri_asinma_genlesme():
    return render_template ("gri_asinma_genlesme.htm")

@app.route("/acilma")
def acilma():
    return render_template ("acilma.htm")    

@app.route("/kapama")
def kapama():
    return render_template ("kapama.htm")

if __name__ =="__main__":

    app.run()
