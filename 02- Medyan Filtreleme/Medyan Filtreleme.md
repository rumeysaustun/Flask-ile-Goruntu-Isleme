# Medyan Filtreleme

Medyan filtresi görüntü işlemede çok sık kullanılan filtredir. Görüntülerde gürültü adı verilen, istenmeyen sinyaller bulunmaktadır. Gürültü, görüntüyü kirleten ve görüntü kalitesini düşüren harici kaynaklarda oluşan etkidir. Gürültü bir görüntü içerisinde bir çok farklı kaynaklardan meydana gelebilir. Filtreleme yöntemleri sayesinde görüntüler gürültüden arındırılarak istenilen hale getirilebilir.

Filtreleme yöntemi görsel üzerinde uygulanacaktır. Uygulama sırasında hangi işlemlerin yapıldığı, filtrenin seçimi ve aşamalar anlatılacaktır. Uygulamanın Python dilinde kodlanması da gerçekleştirilecektir.

## Medyan Filtreleme Yöntemi

Bahsedildiği üzere medyan filtresi en çok tercih edilen algoritmaların başında yer alır ve lineer bir işlem değildir.

Medyan filtreler **nonlineer uzaysal** filtrelerdir. Maskeyi oluşturan boyuttaki resim piksel değerlerinin küçükten büyüğe sıralanıp ortadaki değeri merkez piksele atama işlemidir.Medyan filtresi bir alçak geçiren filtredir.

Mean filtrelerinin genel çalışma mantığı ise; **NxN** boyutlu bir matris penceresi içerisinde bir ortalama değer bulmaya çalışarak işlenir. Bunu yaparken görüntü üzerinde gezen bir kayan pencere yöntemi kullanılır. Medyan filtresi mean filtreleri içerisinde en basit olanıdır. Pencere içerisindeki değerlerin aritmetik ortalamasını alır ve bu şekilde büyük atlamaları kaldırmış olur. Filtre uygulandıktan sonra; konumlarından ayrılmış olan pikseller tespit edilerek temizlenmiş olur. Görüntü içerisindeki yerel değişimleri yumuşatmış olur.

## Medyan Filtrelerinin Gerçekleştirdiği İşlemler

Medyan filtresi için örnek olarak alınan değerler sırasıyla şunlar olsun:
*996, 1718, 1002, 993, 1692, 1003*

Alınan bu sayıları 3’erli gruplayalım (*window size=3 alındı*):

***1.grup: [996 996 1718]***  → Burada 996 sayısının 2 kere kullanılmasının sebebi window size’ın 3 olarak belirlenmiş olmasıdır. 1.grup için medyan=996 O halde 1. Sayı 996’dır. 

***2.grup:[ 996, 1718, 1002]***  → Sıralanırsa: 996 1002 1718. Bu grup için medyan değeri=1002dir. 2.sayı da 1002 olmuş oldu. 

***3.grup:[ 1718, 1002, 993]*** → Sıralama işleminin ardından medyan değeri=1002. Üçüncü sayı 1002 olmuştur.  

***4.grup:[1002 993 1693]*** → 4.grubun medyanı=1002 bulundu. 4. Sayı=1002 

***5.grup:[ 993, 1692, 1003 ]*** →  Üç sayının medyanı 1003 dür. O halde beşinci sayının yeni değeri 1003 dür.

***6. grup: [1692 1003 1003]*** → 6.grubun medyan değeri. 1003 dür. O halde son sayının yeni değeri 1003 olmuştur. 

***7.*** Buna göre ilk başta verilmiş olan; 996 1718 1002 993 1692 1003 sayılarının yeni değerleri sırayla aşağıdaki gibi olmuştur.
*996 1002 1002 1002 1003 1003*

Yeni elde ettiğimiz değerlerden anlaşılacağı gürültüden kaynaklı **1718** ve **1692** sayıları kaybolmuştur. Yeni değerlerin ortalaması ise **1001,3** dür.
Değerler; ortanca filtre kullanılmadan önce ortalama 1234 idi. Ortanca filtresi kullanımından sonra **1001,3** olmuştur.

Tek bir pixelden örnek verecek olursak:
<br>
<img src="https://user-images.githubusercontent.com/59111328/135754045-ad052ce5-2c0a-4983-b696-49baa7010432.png" width="500">

Kenarda kalan alanların nasıl hesaplandığına bir bakalım.<br>
![ö1](https://user-images.githubusercontent.com/59111328/135754832-e826a044-999d-4376-b35c-3190682ff63d.PNG)

Alınması gereken alan 3x3 olmalı. Bu nedenle 4 rekemının ortada olduğunu varsayarak devam edersek hayali bir sağ taraf da olduğunu varsaymış oluruz. Bu sağ tarafı ise soldaki değerleri sağa aynalayarak doldurabiliriz. Yani yeni matrisimiz {{2,2,2} {2,4,2} {9,4,9}} olur. Buradan da aradığımız rakama ulaşabiliriz.

Bir görüntünün tamamen medyan filtresinden geçişini aşağıdaki giften rahatlıkla anlayabiliriz.

![lazım](https://user-images.githubusercontent.com/59111328/135754743-fd7557fd-4b21-47a8-a531-3f84f8a6ffa7.gif)

<br><br>
[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/02-%20Medyan%20Filtreleme/Python%20İle%20Medyan%20Filtre.py) python kodu ile aşağıdaki örnek istenilen hale getirilmiştir.

![medyanfiltrelemeorijinal](https://user-images.githubusercontent.com/59111328/135755773-5af3474c-6a55-455d-b4bd-55f061d518e6.png) ![medyanfiltreleme](https://user-images.githubusercontent.com/59111328/135755776-4477b3e4-b4d2-4186-b707-ab8435accfe6.png)


