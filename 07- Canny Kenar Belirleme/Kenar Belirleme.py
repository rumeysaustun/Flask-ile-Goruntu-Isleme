from PIL import Image
#PIL modülünden Image kütüphanesi eklenmiştir.
import math
#Yapılacak matematik işlemleri için math kütüphanesi eklenmiştir.
import numpy
#numpy kütüphanesi eklenmiştir.

image=Image.open("static\img\canny.jpg")

#image değişkeninin içerisine proje klasörümüzde bulunan 'image' adlı resim dosyasını atıyoruz.

newmat = image.load()

#newmat adlı yeni bir matris oluşturup bunun içerisine resim dosyamızı yüklüyoruz.

wdh=image.size[0]

#wgh değişkenine resim dosyasının genişlik boyutunu atıyoruz. Dosyamızın genişliği 640 piksel.

hgh=image.size[1]

#hgh değişkenine resim dosyasının yükseklik boyutunu atıyoruz. Dosyamızın yüksekliği 360 piksel

graylist=[[0]*hgh for x in range(wdh)]

#graylist adında tanımladığımız matrisin boyutunu yukarıda aldığımız resim dosyamızın genişlik ve yükseklik değerlerine göre belirliyoruz.

for k in range(wdh):

#Resim dosyamızı gri tonlarına çevirmek için iç içe döngü ile matrise çekiyoruz. Böylece her bir piksel birer matris elemanı olacaktır.

   for l in range(hgh):
       r, g, b = image.getpixel((k, l))

       #Her pikselde birer r(kırmızı),g(yeşil),b(mavi) değeri bulunmaktadır. Bunlar o piksele renk veren kodlardır. Öncelikle 'getpixel' fonksiyonu ile bu değerleri r,g,b değişkenlerine atıyoruz.

       gray=(int)((r*0.2126)+(g*0.7152)+(b*0.0722))
       #Resimizi gri yapacak olan sayısal değeri elde etmek için, insan gözünün gama ışınlarını algılama oranlarına göre oluşturulan formül ile aldığımız katsayıları r,g,b değişkenleriyle çarpıp topluyoruz. Böylece resimdeki her piksel için ayrı bir gri renk tonu elde etmiş oluyoruz.
       graylist[k][l]=gray

       #graylist matrisinin her elemanına ağırlık toplama yöntemi ile bulduğumuz gri değerini kaydediyoruz.

       newmat[k,l]=(gray,gray,gray)
       #Resim dosyasını yüklediğimiz matrisin tüm elemanlarına(piksellerine) ağırlık toplama yöntemine göre bulduğumuz gri renk kodunu atıyoruz. Böylece resmin her pikseli renk tonuna göre gri rengini almış olacaktır.Burada kırmızı, yeşil, mavi renk tonlarının hepsine aynı değeri atıyoruz. Bu yöntem gri rengini elde etmemizi sağlıyor.

image.save("static\img\gray.bmp")

#Artık gri tonlarında olan resmi proje dosyasının içine .bmp uzantılı olarak kaydediyoruz.

grayimage = Image.open("static/img/gray.bmp")

#Kaydettiğimiz resim dosyasını tekrar açıyoruz.

mean_im = grayimage.load()

#Açtığımız resim dosyasını mean_im adlı değişkene yüklüyoruz.

meanArray=[[0]*hgh for x in range(wdh)]

#Resim dosyasının boyutu kadar bir boş matris oluşturuyoruz. Bu matris ile Mean filtresini resme uygulayaccağız.

for i in range (1,hgh-1):

#Matris elemanlarına erişmek için iç içe döngüler kullanıyoruz.
   for j in range (1,wdh-1):

   #Mean filtresi resmin her pikseli yani oluşturduğumuz matrisin her elemanına gri olan resmin sırasıyla tüm piksellerini toplayıp bölerek orta bir değer atar.
       meanArray[j][ i] = (graylist[j][i - 1]
           + graylist[j][i + 1]
           + graylist[j][i]
           + graylist[j - 1][ i - 1]
           + graylist[j - 1][i + 1]
           + graylist[j - 1][ i]
           + graylist[j + 1][i - 1]
           + graylist[j + 1][i + 1]
           + graylist[j + 1][ i] ) / 9;
       mean_value=(int)(round(meanArray[j][i]))

       #Bulunan değer yuvarlanır ve yüklenen resme işlenir.

       mean_im[j,i] = (mean_value,mean_value,mean_value)
grayimage.save("static/img/mean.bmp")

#Mean filtresinden geçen resim proje dosyasına kaydedilir.

meanimage=Image.open("static/img/mean.bmp")

#Kaydettiğimiz resmi tekrar açıp bir matrise yüklüyoruz.

robert_im=meanimage.load()
robertArray=[[0]*hgh for x in range(wdh)]
robert_x=[[2,1,0],

#Kenar bulma işleçlerinden olan Robert işleci ile kenarları diagonal olarak taramak için iki matris oluşturuyoruz.

        [1,0,-1],
        [0,-1,-2]]
robert_y=[[0,-1,-2],
        [1,0,-1],
        [2,1,0]]
for m in range (1,hgh-1):

#İç içe döngüler ile matrisin her elemanına raporda belirtilen Robert kenar bulma formülünü uyguluyoruz.

   for n in range (1,wdh-1):
       robertArray[n][m]=(int)(math.fabs(graylist[n][m] - graylist[n - 1][m - 1])) + (int)(math.fabs(graylist[n][m - 1] - graylist[n - 1][m]))
       rbrt_value=int(round(robertArray[n][m]))
       #Bulunan değer yuvarlanır ve bir değişkene atılır.

       robert_im[n,m] = (rbrt_value,rbrt_value,rbrt_value)

       #Son olarak bulunan değer resim matrisine işlenir.

meanimage.save("static/img/robert.bmp")

#Robert kenar bulma işleminden geçen resim proje dosyasına kaydedilir.

robertimage=Image.open("static/img/robert.bmp")

#Kaydettiğimiz resim doyasını non maxima işleminden geçirmek için açıyoruz. Bu işlem ile kenarlar arasında baskılama yapacağız.

image_non=robertimage.load()
newangle=[[0]*hgh for x in range(wdh)]

#Kenar ve açı işlemlerimiz için iki adet resim boyutunda matris oluşturulmuştur.

newedge=[[0]*hgh for x in range(wdh)]
for x in range (1,wdh-1,1):

#Raporda belirtilen Gx ve Gy değerleri için konvolüsyon işlemi yapılmaktadır. Bu işlem ile görüntünün her piksel değeri oluşturduğumuz Robert işleç matrisi ile çarpılıp toplanacaktır. Böylece Gx ve Gy değerini elde ediyoruz.

   for y in range (1,hgh-1,1):
       Gx = (robert_x[0][0] * graylist[x-1][y-1]
           + robert_x[0][1] * graylist[x-1][y]
           + robert_x[0][2] * graylist[x-1][y+1]
           + robert_x[1][0] * graylist[x][y-1]
           + robert_x[1][1] * graylist[x][y]
           + robert_x[1][2] * graylist[x][y+1]
           + robert_x[2][0] * graylist[x+1][y-1]
           + robert_x[2][1] * graylist[x+1][y]
           + robert_x[2][2] * graylist[x+1][y+1])

       Gy = (robert_y[0][0] * graylist[x-1][y-1]
           + robert_y[0][1] * graylist[x-1][y]
           + robert_y[0][2] * graylist[x-1][y+1]
           + robert_y[1][0] * graylist[x][y-1]
           + robert_y[1][1] * graylist[x][y]
           + robert_y[1][2] * graylist[x][y+1]
           + robert_y[2][0] * graylist[x+1][y-1]
           + robert_y[2][1] * graylist[x+1][y]
           + robert_y[2][2] * graylist[x+1][y+1])

       edge=round(math.sqrt((Gx*Gx)+(Gy*Gy)))

       #Elde edilen Gx ve Gy değeri kullanılarak kenar formülünü uyguluyoruz.

       thisAngle=math.degrees(math.atan2(Gx, Gy))

       #Non maxima işlemi için kullanılan renk açıları bulunmaktadır. 0,45,90,135 açı değerlerini renk tablosunda belirtildiği üzere açı aralığını kontrol ederek açı listesinin değerlerini buluyoruz.


       if ( ( (thisAngle < 22.5) and (thisAngle > -22.5) ) or (thisAngle > 157.5) or (thisAngle < -157.5) ):
               newangle[x][y] = 0
       if ( ( (thisAngle > 22.5) and (thisAngle < 67.5) ) or ( (thisAngle < -112.5) or (thisAngle > -157.5) ) ):
               newangle[x][y] = 45
       if ( ( (thisAngle > 67.5) and (thisAngle < 112.5) ) or ( (thisAngle < -67.5) or (thisAngle > -112.5) ) ):
               newangle[x][y] = 90
       if ( ( (thisAngle > 112.5) and (thisAngle < 157.5) ) or ( (thisAngle < -22.5) and (thisAngle > -67.5) ) ):
               newangle[x][y] = 135
       edge=int(edge)
       newedge[x][y]=edge

       #Sonuç olarak bulunan tüm değerleri integer dönüşümüne tabi tutarak edgelist matrisine topluyoruz.


for p in range(1,wdh-1,1):

#Non Maxima işlemi için gereken komşuluklar kontrol edilir.

   for q in range(1,hgh-1,1):
       if newangle[p][q]==0:
           if(newedge[p][q] <= newedge[p+1][q]) or (newedge[p][q] <= newedge[p-1][q]):
               newedge[p][q] = 0
       elif newangle[p][q] == 45:
           if(newedge[p][q] <= newedge[p+1][q+1]) or (newedge[p][q] <= newedge[p-1][q-1]):
               newedge[p][q] = 0
       elif newangle[p][q] == 90:
           if(newedge[p][q] <= newedge[p][q+1]) or (newedge[p][q] <= newedge[p][q-1]):
               newedge[p][q] = 0
       else :
           if(newedge[p][q]<=newedge[p-1][q+1]) or (newedge[p][q] <= newedge[p+1][q-1]):
               newedge[p][q] = 0
       nonmax_value=newedge[p][q]

       #Komşuluk değerine göre elde edilen siyah noktalar matris elemanı olarak tutulur.

       image_non[p,q] = (nonmax_value,nonmax_value,nonmax_value)
robertimage.save("static/img/nonmax.bmp")

#Non maxima işleminden geçen resim dosyası proje klasörüne kaydedilir.

maxim=numpy.max(newedge)

#numpy kütüphanesi kullanılarak non maxima işleminde elde edilen değerlerden en yüksek değer seçilir.

thrd_hgh=maxim*0.1

#Seçilen değere göre iki ayrı threshold değeri hesaplanır ve değerlere göre resim dosyasına ikili eşikleme yapılır.

thrd_low=maxim*0.5
high_thres=int(round(thrd_hgh))
low_thres=int(round(thrd_low))
for a in range(1,wdh-1,1):

#Her eleman için kontrol yapılır.

   for b in range (1,hgh-1,1):
       if newedge[a][b] > high_thres:

       #Eşik değerinden yüksek olanlar aynen bırakılır.

           newedge[a][b] = newedge[a][b]
       elif (newedge[a][b] > low_thres) and (newedge[a][b] < high_thres):

       #İki eşik değerinin arasında olanlar tam bir değere yuvarlanır.

           newedge[a][b] = int(round(newedge[a][b]*0.1))
       else:
           newedge[a][b]=0
       thrd_value=newedge[a][b]
       image_non[a,b]=(thrd_value,thrd_value,thrd_value)
robertimage.save("static/img/thrd.bmp")

#Son olarak resim dosyası proje klasörüne kaydedilir.
