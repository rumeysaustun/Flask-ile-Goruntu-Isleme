from PIL import Image

image = Image.open("static\img\\bayesian.jpg")
newmat = image.load()

wdh = image.size[0]
hgh = image.size[1]


shapelist = [ [0]*hgh for x in range(wdh)]
r_list = [  [0]*hgh for x in range(wdh)]
g_list = [  [0]*hgh for x in range(wdh)]

b_list = [  [0]*hgh for x in range(wdh)]
for i in range(wdh):
    for j in range(hgh):
        r,g,b = image.getpixel((i,j))
        r_list[i][j] = r
        g_list[i][j] = g
        b_list[i][j] = b
hist_r = [0] * 256

hist_g = [0] * 256
hist_b = [0] * 256
for m in range(wdh):
     for n in range(hgh):
        a=r_list[m][n]
        b=g_list[m][n]
        c=b_list[m][n]
        hist_r[a]=hist_r[a]+1
        hist_g[b]=hist_g[b]+1
        hist_b[c]=hist_b[c]+1
sum_r,sum_g,sum_b = 0,0,0

for p in range (len(hist_r)-1):
   sum_r=(hist_r[p]*p)+sum_r
for p in range(len(hist_g)-1):
  sum_g=(hist_g[p]*p)+sum_g

for p in range(len(hist_b)-1):

   sum_b=(hist_b[p]*p)+sum_b

mean_r=int(sum_r/(wdh*hgh))

mean_g=int(sum_g/(wdh*hgh))

mean_b=int(sum_b/(wdh*hgh))
poseb2=(float(hist_r[mean_r])/(hist_r[mean_r]+hist_g[mean_g]+hist_b[mean_b]))*(float(hist_g[mean_g])/(hist_r[mean_r]+hist_g[mean_g]+hist_b[mean_b]))*(float(hist_b[mean_b])/(hist_r[mean_r]+hist_g[mean_g]+hist_b[mean_b]))
for x in range(wdh):
   for y in range(hgh):
       poseb1=(hist_r[r_list[x][y]]/(hist_r[r_list[x][y]]+hist_b[b_list[x][y]]+hist_g[g_list[x][y]]+0.01))*(hist_g[g_list[x][y]]/(hist_r[r_list[x][y]]+hist_b[b_list[x][y]]+hist_g[g_list[x][y]]+0.01))*(hist_b[b_list[x][y]]/(hist_r[r_list[x][y]]+hist_b[b_list[x][y]]+hist_g[g_list[x][y]]+0.01))
       if(poseb1>poseb2):
           shapelist[x][y]=1
           newmat[x,y]=(255,255,255)
       else:
             shapelist[x][y]=0
             newmat[x,y]=(0,0,0)
image.save("static\img\\bayesian_yeni.jpg")
image.show()
