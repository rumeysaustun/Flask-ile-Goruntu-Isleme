from flask import Flask , render_template

app = Flask(__name__)

@app.route("/yara")
def yara():
    return render_template ("/yara.htm")

if __name__ =="__main__":

    app.run()
