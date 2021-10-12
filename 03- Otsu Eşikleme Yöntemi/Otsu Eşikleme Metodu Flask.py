#Aşağıdaki kod diğer .htm kodları ile birlikte kullanılmaktadır.
from flask import Flask, render_template
from PIL import Image

from flask import Flask, render_template
from PIL import Image

resim = Image.open("static\img\otsu.jpg")
newmat = resim.load()
h = resim.size[1]
w = resim.size[0]
graylist = [[0]*h for x in range (w)]
for x in range (w):
     for y in range (h) :
          r,g,b = resim.getpixel((x,y))
          gray=(int)((r*0.2126)+(g*0.7152)+(b*0.0722))
          graylist[x][y] = gray
          newmat[x,y]= (gray,gray,gray)
resim.save("static\img\otsu_gri.jpg")
def histogram(resim):
     width = resim.size[0]
     height = resim.size[1]
     histogram = [0]*256
     for x  in range(height):
          for y in range(width):
               a,b,c = resim.getpixel((y,x))
               histogram[a] = histogram[a]+1
     return histogram
def Otsu (resim):
     hist = histogram(resim)
     sum_all = 0
     for t in range(256):
          sum_all+=t*hist[t]
     sum_back = 0
     w_back = 0
     w_fore =0
     mean_back = 0
     mean_fore = 0
     var_max = 0
     var_between = 0
     threshold = 0
     total =resim.size[0]*resim.size[1]
     for t in range(256):
          w_back +=hist[t]
          if(w_back == 0):
             continue
          w_fore = total-w_back
          if(w_fore == 0):
              continue
          sum_back += t*hist[t]
          mean_back = sum_back/w_back
          mean_fore=(sum_all-sum_back)/w_fore
          var_between = w_back * w_fore * (mean_back-mean_fore)**2
          if(var_between>var_max):
             var_max=var_between
             threshold = t
     return threshold
res = Image.open("static\img\otsu_gri.jpg")
otsu_th = Otsu(res)
otsu_im = res.load()
print (otsu_th)
for x in range(w):
    for y in range(h):
        if graylist[x][y]<otsu_th:
            otsu_im[x,y] =(0,0,0)
            if graylist[x][y]>otsu_th:
                otsu_im[x,y]=(255,255,255)
res.save("static\img\otsu_yeni.jpg")
res.show() 

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
    app.run()


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
