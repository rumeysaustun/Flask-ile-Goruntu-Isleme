# Makine Öğrenmesi

## Makine Öğrenmesi Analiz Yöntemleri

Sınıflandırma algoritmalarını kullanarak yapılan çalışmalarda en büyük yanılgılardan biri başarı kriteri olarak sadece doğruluk oranına bakmaktır. Özellikle dengesiz veri setlerinde (imbalanced data sets) doğruluk oranı bize pek bilgi vermez. Dengesiz veri seti sınıflar arasındaki dağılımın yakın olmadığı veri setlerini tanımlarken kullanılır.
Düşünün ki 10.000 kişiden alınan çeşitli özniteliklere bakarak bu kişilerin kanser olup olmadığını tahmin etmek istiyorsunuz ve içlerinde 10 kişi gerçekten kanser. Biz herkese sağlıklı dersek

**Accuracy (Doğruluk) = (9.990/10.000) * 100= %99.9**

Kanserli hastaları tespit etmeden yapılan rastgele bir tahminin doğruluk oranı bile muazzam. Benzer problem telekom ve kredi kartı dolandırıcılıkları tespitinde de görülmektedir. Anomali ve dolandırıcılık vakalarının bütün veri setine oranı oldukça düşüktür. Bu gibi durumlarda doğruluğa ek olarak iki metriğe daha bakmakta fayda var: recall (duyarlılık) ve precision (kesinlik). TP, FP, TN, FN metriklerinin ne olduğundan ve confusion matrixten bahsedeyim.

**TP (True positive — Doğru Pozitif):** Hastaya hasta demek.
**FP (False positive — Yanlış Pozitif):** Hasta olmayana hasta demek.
**TN (True negative — Doğru Negatif):** Hasta olmayana hasta değil demek.
**FN (False negative — Yanlış Negatif):** Hasta olana hasta değil demek.

### Confusion Matrix

Genel çerçeveyi gördüğümüze göre yukarıda bahsettiğim iki metriğin ne olduğuna bi bakalım.

![t1](https://user-images.githubusercontent.com/59111328/136939338-a806efc2-80df-4897-a48a-9c4da116ab8a.PNG)

**Recall (Duyarlılık):** Hasta olanları doğru tespit etme oranı?

![t2](https://user-images.githubusercontent.com/59111328/136939456-cf8db9ea-9f0e-420d-b19c-101566f32807.PNG)

**Artısı:** Bazı anomali vakalarını doğru tespit etmek yanlış alarm üretmekten daha önemli. Diğer bir deyişle false negative false positiveden daha kritik. Kanserli birini tespit edemeyip ölümüne neden olmaktansa kanser olmayan biri için yanlış tahmin yapıp onu hastaneye çağırmak daha kabul edilebilir.
**Eksisi:** Herkesi hastaneye çağırdık (recall = 1) bütün kanserli vakaları bulduk ama alarmların çoğu yanlış (FP yüksek)
**Precision (Kesinlik):** Hasta dediklerimizin gerçekten kaçı hasta? 

![t3](https://user-images.githubusercontent.com/59111328/136939521-f0d1e2bd-899a-4454-b4fd-bf67222562aa.PNG)

**Artısı:** Birine hasta demeden önce iyice düşünüp taşınmamızı sağlıyor. Herkes hasta dersek precision = 10/10.000 = 0.001
**Eksisi:** Eğer bir kişiye hasta dedik ve o kişi gerçekten hasta (precision = 1) ama kalan 9 kişiyi tespit etmedik. (FN yüksek)
Gördüğünüz gibi recall ve precision iki önemli metrik ve aralarında bir trade-off var. Bununla baş edebilmek için F1-skoru kullanılıyor. F1-skoru ekstrem durumları cezalandırmak için aritmetik ortalama yerine harmonik ortalamayı kullanıyor. 

![t4](https://user-images.githubusercontent.com/59111328/136939595-d56f6a1d-1b65-4f59-a63a-3bed047a6d5a.PNG)

Hatırlarsanız ilk tahminimizde herkese sağlıklı demiştik ve accuracy (doğruluk) oranımız %99.9'du ama tahminin recall ve precision oranları 0.

### ROC Curve (Receiver Operating Characteristic Curve - Alıcı İşletim Karakteristik Eğrisi)

Sınıflandırma modellerinin başarı hesaplarında ROC Curve sık sık karşımıza çıkmaktadır. İlk başta karışık gelebilir temelde iki basit metriğe bakıyor.
 
**TPR:** Kanser olan insanlara hangi olasılıkla doğru diye alarm veriyorum. (Recall aslında)
 
**FPR:** Kanser olmayan insanlara hangi olasılıkla yanlış alarm veriyorum. (Bu metrik yeni daha önce görmedik.)
Bu iki metriği x ve y eksenlerine yerleştirerek çizginin altında kalan alanı hesaplıyoruz (AUC — Area Under Curve).
Aşağıdaki görselde her eğri bir modeli temsil ediyor. Eğri boyunca düşen threshold (sınır) değerlerine karşı TPR ve FPR oranları tespit ediliyor (o noktalar eğriyi oluşturuyor aslında.)
Her threshold için precision, recall değerlerini hesaplayıp F1 skorunu maksimum yapan thresholdu seçiyoruz.
Rastgele bir sınıflandırma (Random Classification) yapıldığında çizginin altında kalan alan 0.5 olmakta. Çizginin altında kalan alan ne kadar büyükse modelin başarı oranı o kadar yüksek demektir. Aslında bir modelin F1 skoru ne kadar yüksekse çizginin altında kalan alan da o kadar yüksek deyip işin içinden kolayca sıyrılabiliriz.
 

Şimdiye kadar bahsettiğim metriklerdeki problem FP ve FN durumlarına eşit yaklaşmasıdır. Halbuki kredi kartı dolandırıcılığını tespit edememek (FN) yanlış tespit yapıp müşteriyi aramaktan (FP) daha büyük maliyet içerir. Bununla başa çıkmak için çeşitli yöntemler var:
**FN = k * FP** (örneğin k = 3). Böylece FN durumunun FP durumundan 3 kat daha problemli olduğunu modele ekleyebiliriz.
Buradaki yeni problemimiz ise her FN durumunu aynı görmektir. Halbuki 5.000 TL değerinde bir dolandırıcılıkla 50 TL değerindeki dolandırıcılık veya standart bir müşteriyle premium müşterinin kartında gerçekleşen dolandırıcılığın maliyeti banka açısından aynı değildir.
Başarı oranlarını büyük gösteren ama gerçekte hem istatistiksel hem de ekonomik olarak anlamsız çalışmalar yerine problemi ve alanı doğru anlayıp ona göre modeller kurmalıyız.
Veri bilimi alanında başarılı olmanın yolu literatürdeki bütün modelleri üstünkörü bilmekten değil bir probleme hangi modelin uygulanacağını ve hangi metriklere bakılacağını bilmekten geçiyor.

![t5](https://user-images.githubusercontent.com/59111328/136939716-17f31df1-5937-42eb-81e5-54c2f6a227d6.PNG)

## Başarı Kriterlerinin Farklı Makine Öğrenmesi Yöntemleri ile Test Edilmesi

Basit bir dataset ile makine öğrenmesi test yöntemlerini analiz edelim. Bu uygulamada fisheriris dataset ile **MATLAB** kullanarak Lineer **SVM, KNN, K-means, Desicion Tree makine öğrenemsi** yöntemleri ile train ve test yapılıp sonuçlar değerlendirilecektir. Fisheriris dataset 3 farklı balık türünün çeşitli özelliklerini bize veren basit bir datasettir ve makine öğrenmesi için başlangıç uygulamalarında sıkça kullanılır. Aşağıda dataset  görselleştirilmiştir.

![t6](https://user-images.githubusercontent.com/59111328/136939980-8335085d-395d-4b52-8f5d-bbb821944ea0.PNG)

### Lineer SVM

SVM iki veya daha fazla sınıfı birbirinden ayıracak en uygun sınırları bulmayı hedefleyen bir makine öğrenmesi yöntemidir. Lineer SVM uygulamada lineer kernel kullanılması anlamına gelmektedir ve sınıfların arasının düz çizgiler ile ayrılması hedeflenmektedir. Uygulamada dataset %80 Train, %20 Test için ayrıldı ve Lineer SVM ile Train ve Test Datası görüntülendi.

![t7](https://user-images.githubusercontent.com/59111328/136940075-e671cd97-0c04-45fb-960c-b1bfb9f5118e.PNG

Lineer SVM için train ve test işlemleri yapılıp confusion matrix ve yukarıda anlatılan diğer parametreler aşağıda verilmiştir

![t8](https://user-images.githubusercontent.com/59111328/136940220-c3387dba-5c6a-4919-bace-d43fac483a94.PNG)

### KNN
En yakın komşu algoritması olarak da bilinir.  Seçtiğimiz k değeri komşu sayısını belirler.  Karar verme aşamasında belirlenen sayıdaki en yakın komşular bulunur ve bunların hangi sınıflara ait olduklarına bakılarak bir hesaplama yapılır. Ağırlıklı olarak hangi sınıfa aitlerse test için gelen eleman o sınıfa aittir denilir.
Dataset %80 Train, %20 Test için ayrıldı ve KNN metodu ile train işlemi yapıldıktan sonra aşağıdaki gibi test ve train datası çizdirildi.

![t9](https://user-images.githubusercontent.com/59111328/136940311-ecd83a47-a8bd-449e-be76-a7eadcb5f54b.PNG)

KNN için test işlemi yapılıp confusion matrix ve yukarıda anlatılan diğer parametreler aşağıda verilmiştir.
 
![t10](https://user-images.githubusercontent.com/59111328/136940395-c26ffd0d-2859-411e-bc47-e529c1ace07a.PNG)

### Desicion Tree

Desicion Tree ile karar vermek için uygun eşik değerleri belirlenir ve bu değerlere göre yeni gelen data test edilir. 
Dataset %80 Train, %20 Test için ayrıldı ve Desicion Tree ile Train işlemi gerçekleştirilip sonucu aşağıdaki gibi görüntülendi.

![t11](https://user-images.githubusercontent.com/59111328/136940498-5ef06442-6edc-4dd9-aa11-b1d349079f1f.PNG)

Desicion Tree için test işlemi yapılıp confusion matrix ve yukarıda anlatılan diğer parametreler aşağıda verilmiştir.

![t12](https://user-images.githubusercontent.com/59111328/136940632-fac740db-d312-42a6-8ab5-50fae651fadf.PNG)

![t13](https://user-images.githubusercontent.com/59111328/136940637-9acd4d9c-94f6-41bc-baa3-3a85abcd7fe2.PNG)

## K-MEANS
K-means algoritmasında k değeri kaç adet merkez noktası belirleyeceğimizi belirler. Train buna göre yapılır.Dataset %80 Train, %20 Test için ayrıldı ve Kmeans algoritması kullanılarak test ve train işlemi gerçekleştirildi ve görselleştirildi. Kmeans algoritmasında k değeri sınıf sayısına göre belirlenmelidir.  Bu nedenle datasetimizde 3 sınıf olduğu için K değeri 3 olarak seçildi. Train ve test datası aşağıdaki gibi görselleştirilmiştir. x ile gösterilen noktalar merkez noktalarını ifade etmektedir.

![t14](https://user-images.githubusercontent.com/59111328/136940760-98feb6fb-35d2-45f7-9afe-d7be3e1ef16e.PNG)

Aşağıda k-means için yukarıda anlatılan ölçütler verilmiştir.

![t15](https://user-images.githubusercontent.com/59111328/136940816-67a2ca0c-9ad5-438e-b033-542ab281d8ef.PNG)

## Sonuçlar

Yukarıda anlatılan makine öğrenmesi algoritmalarının farklı değerlendirme kriterlerine göre sonuçları aşağıdaki tabloda verilmiştir.

![t16](https://user-images.githubusercontent.com/59111328/136940916-728bb08e-7d32-453f-9ecd-ed859cabf7c0.PNG)

SVM	KNN	K-MEANS	Desicion-Tree

F1-skore	0,93	0.89	0.90	0.96

Training Time	0.941	0.051	1.304	0.965

Test Time	0.047	0.014	0.085	0.014

Yukarıdaki sonuçlara bakılarak bu uygulamada fisheriris dataset için F1 skoru en yüksek olan Desicion Tree daha iyi bir yöntem gibi gözükmektedir. Bu uygulamada test ve train datası her seferinde random olarak atandığı için F1 skorlarda değişebilir burda önemli olan nasıl karşılaştırma yapılması gerektiğinin anlanmasıdır. Ayrıca kullanılacak yöntemi seçmeden önce kullanacağımız dataseti iyi tanımak gerekir. Datasetin karakteristiği göz önünde bulundurularak yöntem seçilmelidir. 





