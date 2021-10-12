from flask import Flask , render_template

app = Flask(__name__)

@app.route("/uygulama")
def uygulama():
    return render_template ("uygulama.htm")
@app.route("/prewitt")
def prewitt():
    return render_template ("prewitt.htm")
@app.route("/sobel")
def sobel():
    return render_template ("sobel.htm")

@app.route("/robert")
def robert():
    return render_template ("robert.htm")

if __name__ =="__main__":

    app.run()
