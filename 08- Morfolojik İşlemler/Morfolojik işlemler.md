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

