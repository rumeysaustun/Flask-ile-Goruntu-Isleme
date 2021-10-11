# Morfolojik İşlemler
Biyolojinin canlıların şekil ve yapıları ile ilgilenen dalına **morfoloji (biçim bilim)** adı verilmektedir. Matematiksel morfoloji ise temel küme işlemlerine dayanan, imgedeki **sınırlar (borders), iskelet (skeleton)** gibi yapıların tanımlanması ve çıkartılması, gürültü giderimi, bölütleme gibi uygulamalar için gerekli bir araçtır. İmge işlemede genellikle, **morfolojik süzgeçleme, inceltme (thinning), budama (pruning)** gibi ön/son işlem olarak da sıkça kullanılırlar. Gri tonlu imgeler üzerinde de yapılabileceği gibi, genellikle ikili imgeler üzerinde yapılan işlemlerdir.Uygulama alanları : 
-	Görüntülerin ön işlenmesinde ya da son işlenmesi adımlarında
-	Sınır, kenar gibi görüntü bileşenlerinin ayrıştırılmasında

## İkili Morfolojik İşlemler
İkili görüntülerde her pikselin (x,y) değeri 0 veya 1 olabilir. İkili görüntü genellikle siyah ve beyaz olarak görülür.Temel ikili morfolojik işlemler :
-	Genleşme İşlemi
-	Aşınma İşlemi
-	Açma İşlemi
-	Kapama İşlemi
 Temel ikili morfolojik işlemlerin matematiksel ifadeleri aşağıdaki denklemlerle tanımlanmaktadır :
![image](https://user-images.githubusercontent.com/59111328/136694801-78cedf37-8dfa-43d0-9dfd-1a4745288065.png) <br>
![image](https://user-images.githubusercontent.com/59111328/136694812-25f6bdb7-72b9-4b9c-85c1-7e6e3cb6288e.png)


### Genleşme İşlemi
İkili imgedeki nesneyi büyütmeye ya da kalınlaştırmaya yarayan morfolojik işlemdir. Sayısal bir imgeyi genişletmek imgeyi yapısal elemanla kesiştiği bölümler kadar büyütmektir. İşlenecek imgenin her bir pikseli, yapısal elemanın merkez noktasına oturtularak genleşme işlemi yapılmaktadır. Kalınlaştırma işleminin nasıl yapılacağını yapısal eleman belirler. Genleşme işlemi uygulanmış bir imgede, imge içerisindeki deliklerin ve boşlukların doldurulması ve köşe noktasının yumuşaması gözlenir.

![image](https://user-images.githubusercontent.com/59111328/136694877-e0670b11-4fcb-4911-9068-5158b9bfd27f.png)<br>

![genleşme](https://user-images.githubusercontent.com/59111328/136694873-5088815a-d85a-4f74-a838-9175cb11b81e.png)

**Genleşme İşlemi Uygulaması**

Orijinal Hali:

![morfolojik](https://user-images.githubusercontent.com/59111328/136787524-b602f6f6-b1ed-4e45-9571-ca79979738ed.png)

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/genlesme.py) kod ile genleşmiş hali:

![morfolojik_genlesme](https://user-images.githubusercontent.com/59111328/136787629-76fb5038-8717-435c-b4ee-738ff97f61d3.jpg)

### Aşınma İşlemi

İkili imgedeki nesneyi küçültmeye ya da inceltmeye yarayan morfolojik işlemdir. Aşınma işlemi tam anlamıyla olmasa da bir bakıma genleşme işleminin tersi gibidir. İmge içerisindeki nesneler ufalır, delik varsa genişler, bağlı nesneler ayrılma eğilimi gösterir.

![image](https://user-images.githubusercontent.com/59111328/136782229-d3084360-c537-4c27-8516-f9ca172c0b1d.png) <br>

![image](https://user-images.githubusercontent.com/59111328/136790189-2ce9d1c3-0338-4bbf-a3be-fd3a6c29be05.png)

**Aşınma İşlemi Uygulaması**

Orijinal Hali:

![morfolojik](https://user-images.githubusercontent.com/59111328/136789305-6277afe3-304e-4a88-bae8-775eef653551.png)

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/asinma.py) kod ile aşınmış hali:

![morfolojik_asinma](https://user-images.githubusercontent.com/59111328/136789325-de8cc84f-43ac-419e-8092-0aace9c0b34f.jpg)

### Açma İşlemi

İmge üzerinde aşınma işleminin hemen ardından genleşme işlenmesi uygulanması sonucu açma işlemi elde edilir. İmge içerisindeki nesneler ve nesneler arasındaki boşluklar yapısal elemanın büyüklüğüne göre temizlenir. İmge üzerinde kalan nesneler orijinal imgedeki şekillerinden biraz daha küçük hale gelir. Açma işlemi ile birbirine yakın iki nesne imgede fazla değişime sebebiyet vermeden ayrılmış olurlar.

![image](https://user-images.githubusercontent.com/59111328/136790308-1a4f008d-ac7a-4847-a01d-617013855f8d.png)
<br>
![image](https://user-images.githubusercontent.com/59111328/136790130-1b67b319-4d46-4611-b60a-60fd9cf908e9.png)

**Açma İşlemi Uygulaması**

Orijinal Hali:

![morfolojik](https://user-images.githubusercontent.com/59111328/136790866-fad179ef-2062-45bd-a3b6-23282b99d922.png)

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/acma.py) kodla açılmış hali:

![morfolojik_acma](https://user-images.githubusercontent.com/59111328/136790883-875be952-fa51-4440-a5b1-2a5e191f88c0.jpg)

### Kapama İşlemi

İmge üzerinde genleşme işleminin hemen ardından aşınma işleminin uygulanması sonucu kapama işlemi elde edilir. Dolayısıyla birbirine yakın iki nesne imgede fazla değişiklik yapılmadan birbirine bağlanmış olur. Kapama işlemi sonunda imge içerisindeki noktalar birbirlerini kapatırlar, imgedeki ana hatlar daha da dolgunlaşır. Genleşme işlemine benzer bir şekilde kapama işleminde de birbirine yakın olan noktalar arasındaki boşluklar dolar ve noktalar birleşir. İmge üzerinde kalan nesneler, orijinal imgedeki şekillerine bürünürler.

![image](https://user-images.githubusercontent.com/59111328/136790949-f78c622c-80a7-4ec4-b698-7cfd85a4681c.png)<br>

![image](https://user-images.githubusercontent.com/59111328/136790967-d42c7946-012e-44b2-bdd0-468c787f5184.png)

**Kapama İşlemi Uygulaması**
 
 Orijinal Hali:
 
 ![morfolojik](https://user-images.githubusercontent.com/59111328/136791096-faef6ec7-17d3-4aa4-b87c-e43251be2af6.png)

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/kapama.py) kod ile kapanmış hali:

![morfolojik_kapanma](https://user-images.githubusercontent.com/59111328/136791311-1509f43b-474e-4a8c-be7f-e9614714020d.jpg)

### Yapısal Eleman

Yapısal eleman olarak isimlendirilen yapı, imge üzerinde yapacağımız işleme ve yapmak istediğimiz uygulamaya göre istenilen boyutlarda ve istenilen şekilde hazırlanmış küçük ikilik bir imgedir. Yapısal eleman farklı geometrik şekillerden herhangi biri olabilir. En çok kullanılanları kare, dikdörtgen ve dairedir.

![image](https://user-images.githubusercontent.com/59111328/136791583-30a061f6-6e3a-4fe4-b1b4-858066a42546.png)

### Gri Seviyeli Morfolojik İşlemler

Gri seviyeli bir imgenin B yapısal elemanı ile genleşme işlemi denklem 11 ile tanımlanmaktadır. Şekil 1.14’de gri seviyeli imgeye 15x15 kare yapısal elamanı ile genleşme işlemi uygulanmış hali gösterilmektedir. 

![image](https://user-images.githubusercontent.com/59111328/136791874-6be428f1-459c-40a0-ac07-87b48be153f8.png)

Burada Df ve Db, sırasıyla f ve b’nin tanım bölgeleridir. Genleşme işleminden sonra imge daha parlaktır. Gri seviyeli aşınma işlemi denklemi aşağıda tanımlanmıştır. Aşağıdaki şekilde gri seviyeli imgeye 15x15 kare yapısal elemanı ile aşınma işlemi uygulanmış hali gösterilmektedir.

![image](https://user-images.githubusercontent.com/59111328/136791890-d1dd4430-4b32-46f2-a659-bd80619a3fc7.png)

Aşınma işleminden sonra imge daha koyudur. 

![image](https://user-images.githubusercontent.com/59111328/136791922-77618707-d797-4163-9b9a-88a9d4b44897.png)

Gri seviyeli imgelerde yapılan morfolojik işlemler sonucunda;  Gri seviyeli imgede uygulanan genleşme işlemi, imge daha parlak bir hal alır.  İmgede koyu tonlu bölgelerle çevrili olan parlak bölgeler genişlerken, parlak bölgelerle çevrili koyu tonlu bölgeler zayıflamakta, hatta yapısal elemanın ve koyu tonlu bölgenin boyutuna bağlı olarak kaybolabilmektedir. Gri seviyeli imgede uygulanan aşınma işlemi, imge daha koyu bir hal alır.  İmgede koyu tonlu bölgelerle çevrili olan parlak bölgeler daralırken, parlak bölgelerle çevrili koyu tonlu bölgeler genişlemektedir. 

**Gri Seviyeli Aşınma Ve Genleşme Uygulamaları:**

Orijinal resim:

<img src="https://user-images.githubusercontent.com/59111328/136792715-3e5f626b-8781-431e-9e08-7e0bb1d9e1f7.jpg" width="800">

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/griasinma.py) kod ile aşınmış hali:

<img src="https://user-images.githubusercontent.com/59111328/136792745-3a1effdb-bcf9-4dad-bb56-82b2e5811753.png" width="800">

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/gri_genlesme.py) kod ile genleşmiş hali:

<img src="https://user-images.githubusercontent.com/59111328/136793546-977ae3b5-509f-4d44-9152-fff39451b050.png" width="800">


### Ortalama Süzgeç

Ortalama süzgeç, imgedeki gürültüyü azaltmak için yaygın olarak kullanılan, basit bir süzgeç tipidir. Ortalama süzgeçleme, gürültülü imge üzerindeki her bir pikselin değeri o piksele komşu olan diğer piksellere ait değerlerin ortalaması ile değiştirilir. Bu çalışmada, aritmetik ortalama süzgeci kullanılmıştır. Ortalama süzgeci, katlama süzgeç olarak da düşünmek mümkündür. Gürültü çeşidine ve büyüklüğüne göre kullanılacak maske tipi seçilmelidir. Genellikle 3X3’lük maskeler kullanılmaktadır fakat daha büyük gürültü temizleme işlemleri için daha büyük boyutta maskeler kullanılmalıdır. Küçük maskelerin imgeye ardışıl bir şekilde uygulanması koşuluyla, büyük bir maskenin imge üzerinde yarattığı etkiye benzer bir etki oluşturması mümkündür. 

![image](https://user-images.githubusercontent.com/59111328/136793716-2975f0c2-1c2d-484a-8349-a523134646a9.png)

Ortalama süzgeçte, seçilen farklı boyutlarda ve değerlerde ortalama süzgeç maskesine göre oluşturulan yeni ortalama piksel değerleri ile imgedeki gürültülerin eliminasyonu sağlanır. Ortalama süzgecin dezavantajları: 
1) İmgede çok düşük değere sahip olan bir piksel, o piksele komşu olan bütün piksellerin ortalamasını büyük oranda etkiler ve dolayısıyla işlemlerde yanılsamaya neden olur. 
2) Süzgeç kerneli belirgin kenarlar üzerinde işlem yaptığında, gürültü pikseller için gösterdiği etkiyi kenarlarda da gösterebilecek ve böylece imgedeki belirgin detaylar ve kenarlar da bulanıklaşabilecektir. Eğer işlem sonundaki imgede belirgin kenarlar önem arz ediyorsa, bu durum problem yaratabilecektir.



