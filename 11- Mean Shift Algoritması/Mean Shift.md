# Mean Shift 
Meanshift, noktaları noktaya doğru kaydırarak, veri noktalarını kümelere tekrarlayan bir küme algoritmasıdır. Mod, veri noktalarının en yüksek yoğunluğu (Meanshift bağlamında bölgede) olarak anlaşılabilir. Bu şekilde, mod arayan algoritma olarak da bilinir. Meanshift algoritması görüntü işleme ve bilgisayar görüşü alanında uygulamalara sahiptir.Bir dizi veri noktası  verildiğinde, algoritma her bir veri noktasını en yakın kümelenme merkezine doğru iteratif olarak atar. En yakın kümelenme merkezine olan yön, yakındaki noktaların çoğunun bulunduğu yere göre belirlenir. Böylece her bir iterasyon her veri noktası, en fazla noktanın bulunduğu yere yaklaşacak ve bu da kümelenme merkezine yönlendirecektir. Algoritma durduğunda, her nokta bir kümeye atanır.Popüler K-Means algoritmasının aksine, meanshift önceden kümelenme sayısını belirtmeyi gerektirmez. Kümelerin sayısı, veriye göre algoritma tarafından belirlenir.

İşte Meanshift'te adım adım ne olduğunu gösteren bir diyagram:

![image](https://user-images.githubusercontent.com/59111328/136805469-4adbdc34-cc56-418c-b007-3971bb574c0a.png)
![image](https://user-images.githubusercontent.com/59111328/136805489-f1aad315-dd5f-43b0-8ca7-b12bcc134f40.png)

Mavi veri noktaları ilk veri noktalarıdır ve kırmızı her bir iterasyonda bu veri noktalarının konumlarıdır. Her adım için açıklama:

1- Başlangıç hali. Kırmızı ve mavi veri noktaları, Meanshift algoritması başlamadan önce ilk iterasyonda tamamen üst üste gelir.

2-Yinelemenin sonu 1. Tüm kırmızı veri noktaları kümelere daha da yaklaşır. 4 küme olacak gibi görünüyor.

3-Yinelemenin sonu 2. Üst sağ ve sol alt kümeleri sadece iki yineleme kullanılarak yakınsamaya ulaşmış gibi görünmektedir. Orta ve alt sağ kümeler, birleşme gibi görünüyorlar, çünkü iki merkez çok yakın.

4-Yinelemenin sonu 3. Sağ üst ve alt sol merkezlerde değişiklik yok. Veri noktaları her bir kümeyi etkilediğinden, diğer iki merkezci bir araya geldiler. Bu, Meanshift imzasıdır, kümelerin sayısı önceden belirlenmemiştir.

5-Yinelemenin sonu 4. Tüm kümeler yakınsadı olmalıdır.

6-Yinelemenin sonu 5. Tüm kümelerin aslında hareketi yoktur. Tüm kırmızı veri noktaları için herhangi bir değişiklik tespit edilmediğinden algoritma burada durur.

![image](https://user-images.githubusercontent.com/59111328/136805534-60ec0ac2-be59-42e4-b7d4-7caf74d0aff3.png)

Meanshift, yukarıda daire içine aldığım 3 kümeyi buldu. Orijinal veriler aslında 4 veri kümesinden elde edilir, ancak Meanshift'in 3 veri kümesini daha iyi temsil edebileceğini düşündüğü ve çok da kötü olmadığı için kullandı. Scikit-Learn’in make_blobs veri kümelerini kullandım:

![image](https://user-images.githubusercontent.com/59111328/136805585-64e26005-626a-4a19-89a7-1f3ce0eda1ed.png)

Şimdi Meanshift'in genel olarak nasıl çalıştığına dair büyük bir resmimiz var. Tek bir veri noktasının ne olduğuna bakalım ve bunu tüm noktalara genelleştirelim.

Aşağıda Meanshift üzerinden yeni bir veri noktaları kümesinde tek bir veri noktası çalıştırıyoruz. Tek veri noktası siyah okla işaret edilir.

![image](https://user-images.githubusercontent.com/59111328/136805642-7639195a-b01a-49fe-ab57-70847e633c6a.png)

En yakın nokta kümeleri ilk veri noktasının güneyi veya kuzeyi olabilir. Meanshift algoritmasını çalıştıran verilerin, veri noktasını ya güney ya da kuzeydeki veri noktalarına yaklaştırması gereken verileri inceleyerek söyleyebiliriz.

![image](https://user-images.githubusercontent.com/59111328/136805686-26da815d-ce5e-46f0-a310-26c83f3fb674.png)

Kırmızı yol, noktanın her bir iterasyondan sonra güney küme merkezine yaklaştığını göstermektedir. Her iterasyondan sonra hareketin kademeli olarak azaldığını fark edebilir ve bunun nedeni veri noktasının merkeze daha yakın olmasından ötürü, kaymanın daha az şiddetli olmasıdır. 10 tekrardan sonra, nokta gerçekten merkeze yakın. Araç kayması bunu K iterasyonları için tüm veri noktaları için yapar. Çoğu durumda, 5 yineleme yakınsama için yeterli olmalıdır. Bundan, algoritmanın çalışma zamanı karmaşıklığının O (KN2) olduğunu, N'nin veri noktası sayısı olduğunu ve K'nin Meanshift'in yineleme sayısı olduğunu söyleyebiliriz.

Tek bir nokta hareketini göstermek için bu uygulamanın tüm veri noktalarının hareket ettiği yerden biraz farklı olduğuna dikkat edin, ancak fikir temelde aynıdır. Merak için, tüm veri noktaları hareket ederse, her bir komşu veri noktasını daha büyük ölçüde etkileyecektir. Sonuç, algoritmanın daha hızlı bir şekilde birleşmesidir: bu versiyonda ~ 10 tekrarlamaya karşı ~ 3 tekrarlama.

## Mean Shift Algoritması

Meanshift'i bir takım veri noktaları X üzerinde çalıştırmaya başlamadan önce birkaç şeye ihtiyacınız olacak:

1-Bir x (X) noktasının komşularını belirlemek için N (x) fonksiyonu kullanılır. Komşu noktalar belli bir mesafe içindeki noktalardır. Mesafe metriği genellikle Öklid Mesafesidir.

2-Meanshift'te kullanılacak bir çekirdek K (d). K genellikle bir Gauss Çekirdeğidir ve d iki veri noktası arasındaki mesafedir.

Şimdi, yukarıdaki ile, bu bir dizi veri noktası X için Ortalama Shift algoritmasıdır:

1.	Her bir x ∈ X veri noktası için x'in komşu noktalarını (N (x)) bulun.
2.	Her bir x ∈ X veri noktası için, bu denklemden m (x) ortalama kaymasını hesaplayın:

![image](https://user-images.githubusercontent.com/59111328/136805781-61eaaf70-37ae-4944-8560-f573dc2ddb89.png)

3.  Her bir x ∈ X veri noktası için x ← m (x) dosyasını güncelleyin.
  4. N_iteations için veya noktalar neredeyse hareket etmeden veya hareket            etmedikçe tekrarlayın.
      
En önemli parça m (x) ortalama kayması hesaplamaktır. 2. adımdaki formül, göz korkutucu görünüyor, ancak onu bozalım. Kırmızı kırmızılı bölümlerin aslında aynı olduğuna dikkat edin:

![image](https://user-images.githubusercontent.com/59111328/136805807-53cc862c-38d8-411a-8ac4-fa06e0b1d44f.png)

Bunu Wi ile değiştirelim, böylece formül şöyle olur:

![image](https://user-images.githubusercontent.com/59111328/136805880-4fc0377a-2b0f-4892-b272-410b38b4e22b.png)

Wikipedia'da ağırlıklı ortalama genel formülüne bakın bize şunu verir:

![image](https://user-images.githubusercontent.com/59111328/136805843-02c0f742-5ed5-4ceb-8edc-dd55df5e790d.png)

**Özetlemek gerekirse:** Algoritma, bir veri noktasını etkileyen bir dizi yakın nokta bulup daha sonra noktaların çoğunun bulunduğu yere doğru kaydırır ve en yakın noktaların diğer noktalardan daha fazla etkisi vardır. Hiçbir şey değişmeyene kadar tüm veri noktaları için bunu tekrarlayın.

**Uygulaması:**

