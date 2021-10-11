from flask import Flask , render_template

app = Flask(__name__)

@app.route("/goruntucevirme")
def goruntucevirme():
    return render_template ("goruntucevirme.htm")

if __name__ =="__main__":

    app.run()
