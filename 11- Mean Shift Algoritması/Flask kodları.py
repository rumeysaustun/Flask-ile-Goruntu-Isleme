from flask import Flask , render_template

app = Flask(__name__)

@app.route("/mean")
def anaSayfa():
    return render_template ("/mean.htm")

if __name__ =="__main__":

    app.run()

image = Image.open("static\img\mean.jpg")
