# HSI Renk Uzayı

RGB, CMY gibi renk uzayları insan gözünün renk alma yapısındadır. İnsan beyninde renkler tanınırken ya da birbiri ile karşılaştırılırken bu modellerin kullanımı zordur.
Bu nedenle bu tür çalışmalarda renk **özü (hue-H), doygunluk (saturation-S) ve şiddet (intensity-I)** tanımlamaları kullanılır. Bu bileşenlerden oluşan modele de **HSI (hue, saturation, intensity)** renk modeli adı verilir.

Sonuçta söyleyebiliriz ki, RGB renk modeli renk oluşturma için idealdir (örn;monitör) fakat betimlemede kötüdür. HSI renk modeli ise renge bağlı tanımlamada çok iyidir.

## HSI Modelleme

**Renk Özü (Hue-H) :** Baskın renk dalga boyunu gösterir ve açısal olarak [0°,360°] aralığında ifade edilir.

**Doygunluk (Saturation-S) :** Saf rengin beyaz ışık
ile hangi oranda karıştığını gösterir. Yarıçapa 
karşılık gelir ve [0,1] aralığında değer alır.

**Şiddet (Intensity-I) :** Işık miktarını gösterir.

**RGB → HSI geçiş:**

![image](https://user-images.githubusercontent.com/59111328/135862273-77134d7b-810c-41de-ad00-ccf26beaf183.png)

Formüller:

![for](https://user-images.githubusercontent.com/59111328/135862631-3266b1c4-d035-4082-88a1-f9000f2435ed.PNG)

## Uygulama

**Resmin orijinal hali:**

![HSI](https://user-images.githubusercontent.com/59111328/136016533-eb107695-426c-478c-8dd3-7377d906b92c.jpg)

**[Buradaki]() kod yardımıyla oluşan yeni resim:**

![HSI_new](https://user-images.githubusercontent.com/59111328/136016552-e0059d68-a053-4857-abe2-cc4236fb72d4.jpg)
