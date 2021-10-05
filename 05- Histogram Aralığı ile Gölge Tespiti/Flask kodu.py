from flask import Flask , render_template
#Gerekli kütüphaneler uygulamaya dahil edilir.
app = Flask(__name__)

@app.route("/histogram")
def histogram():
    return render_template ("histogram.htm")

@app.route("/histogram_yeni")
def histogram_yeni():
    return render_template ("histogram_yeni.htm")

if __name__ =="__main__":

    app.run(debug=True)
