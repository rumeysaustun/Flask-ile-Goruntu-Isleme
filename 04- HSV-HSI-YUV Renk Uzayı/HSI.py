from PIL import Image
import math

def  rgbtohsi (R, G, B):

  r = R / 255
  g = G / 255  #Değerler normalize hale getirilir.
  b = B / 255

  num=0.5*((r-g)+(r-b))
  den=((r-g)*(r-g)+(r-b)*(g-b))**(0.5) #Formül uygulanır.

  if(b<=g):
     if den != 0:
         h = math.acos(num / (den))
     else:
         h = 0

  elif(b>g):
      if den!=0:
          h=(2*math.pi)-math.acos(num/den)
      else:
          h=0

  s=0
  i=0
  if (r+g+b) != 0:
    s=1-(3*min(r,g,b)/(r+g+b))
    i=(r+g+b)/3

  return int(h*180/math.pi), int(s*100), int(i*255)





resim=Image.open("static\img\HSI.jpg").convert("RGB")
resim_pix = resim.load()
w=resim.size[0]
hg=resim.size[1]
for i in range(w):
  for j in range(hg):
      r, g, b = resim.getpixel((i, j))
      h, s, v = rgbtohsi(r, g, b)
      resim_pix[i,j] = (h, s, v)
resim.save("hsi_new.jpg")
resim.show()
