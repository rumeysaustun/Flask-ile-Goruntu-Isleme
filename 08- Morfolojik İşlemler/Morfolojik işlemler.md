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

![AŞINDIRMA](https://user-images.githubusercontent.com/59111328/136782315-27915e57-18c3-4a64-b5e9-a506a910a3cc.png)

**Aşınma İşlemi Uygulaması**

Orijinal Hali:

![morfolojik](https://user-images.githubusercontent.com/59111328/136789305-6277afe3-304e-4a88-bae8-775eef653551.png)

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/08-%20Morfolojik%20İşlemler/asinma.py) kod ile aşınmış hali:

![morfolojik_asinma](https://user-images.githubusercontent.com/59111328/136789325-de8cc84f-43ac-419e-8092-0aace9c0b34f.jpg)

