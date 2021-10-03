
import PIL
from PIL import Image

resim = Image.open("static\img\medyanfiltreleme.png").convert("RGB")

pix = resim.load()

w = resim.size[0]

h = resim.size[1]

graylist = [[0]*h for x in range (w)]

temparray = [[0]*(h+2) for x in range (w+2)]

print(resim.getpixel((3,5)))

for i in range (w):

    for j in range (h):

        r,g,b = resim.getpixel((i,j))

        print (r,g,b)

        gray = (int)((r*0.2126)+(g*0.7152)+(b*0.0722))

        graylist[i][j] = gray

        pix [i,j] = (gray,gray,gray)

for ni in range (1,w+1):

    for nj in range (1,h+1):
        temparray [ni] [nj]  =  graylist [ni-1] [nj-1]

med = [0]*9

gecici = 0
for m in range(1,w+1):

    for n in range (1,h+1):

        med[0] = temparray[m-1][n-1]

        med[1] = temparray[m-1][n]

        med[2] = temparray[m-1][n+1]

        med[3] = temparray[m][n-1]

        med[4] = temparray[m][n]

        med[5] = temparray[m][n+1]

        med[6] = temparray[m+1][n-1]

        med[7] = temparray[m+1][n]

        med[8] = temparray[m+1][n+1]

        med = sorted(med)

        value = med[4]
        pix[m-1,n-1] = (value,value,value)

resim.save("static\img\medyanfiltreleme.png")
resim.show()
