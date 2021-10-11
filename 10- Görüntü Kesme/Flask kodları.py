from flask import Flask , render_template

app = Flask(__name__)

@app.route("/kesme")
def kesme():
    return render_template ("kesme.htm")

if __name__ =="__main__":

    app.run()
