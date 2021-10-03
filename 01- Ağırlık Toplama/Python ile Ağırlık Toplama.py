#Aşağıdaki kod ile hedefteki resmi gri tonlarına dönüştürecek.
import PIL
from PIL import Image

resim = Image.open("static\img\\agirliktoplama.jpg").convert("RGB")

yuklenen = resim.load()

genislik = resim.size[0]

yukseklik = resim.size[1]

for i in range(genislik):

    for j in range(yukseklik):
        r, g, b = resim.getpixel((i, j))
        gray = (int)((r * 0.2126) + (g * 0.7152) + (b * 0.0722))
        yuklenen[i, j] = (gray, gray, gray)

resim.save("static\img\\agirliktoplama_yeni.jpg")
resim.show()
