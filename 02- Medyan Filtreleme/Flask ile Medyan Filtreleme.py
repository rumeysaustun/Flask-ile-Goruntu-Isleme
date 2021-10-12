#Aşağıdaki kod klasördeki diğer .htm kodlarıyla beraber çalıştırılacaktır.
from flask import Flask, render_template
import PIL
from PIL import Image,ImageFilter

im1 = Image.open("static\img\medyanfiltreleme.png")
im1 = im1.filter(ImageFilter.MedianFilter(size=3))
im1.save("static\img\medyanfiltrelemeyeni.png")
for i in range(9):
    im1 = im1.filter(ImageFilter.MedianFilter(size=3))
    im1.save("static\img\medyanfiltreleme10.png")
    if i == 2:
        im1.save("static\img\medyanfiltreleme3.png")


im1.show()
app = Flask(__name__)

@app.route("/agirliktoplama")
def agirliktoplama():
    return render_template("agirliktoplama.htm")

@app.route("/medyan")
def medyan():
    return render_template("medyan.htm")

@app.route("/medyanyeni")
def medyanyeni():
    return render_template("medyanyeni.htm")

@app.route("/medyan10")
def medyan10():
    return render_template("medyan10.htm")

@app.route("/medyan3")
def medyan3():
    return render_template("medyan3.htm")

if __name__ == "__main__":
    app.run()
