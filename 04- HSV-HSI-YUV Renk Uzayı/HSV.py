from PIL import Image

def  rgbtohsv (r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    Cmax = max (r, g, b)
    Cmin = min (r, g, b)
    delta = Cmax - Cmin
    if delta == 0:
        h = 0
    elif Cmax == r:
        h = (60 * ((g-b)/delta)) % 360
    elif Cmax == g:
        h = (60 * ((b-r)/delta) + 2) % 360
    elif Cmax == b:
        h = (60 * ((r-g)/delta) + 4) % 360
    if Cmax == 0:
        s = 0
    else:
        s = delta/Cmax
    v = Cmax
    h=int(h)
    s=int(s)
    v=int(v)
    return h, s, v
resim=Image.open("static\img\HSV.jpg")
resim_pix = resim.load()
w=resim.size[0]
hg=resim.size[1]
for i in range(w):
    for j in range(hg):
        r, g, b = resim.getpixel((i, j))
        h, s, v = rgbtohsv(r, g, b)
        resim_pix[i,j] = (h, s, v)
resim.save("static\img\HSV_yeni.jpg")
resim.show()
