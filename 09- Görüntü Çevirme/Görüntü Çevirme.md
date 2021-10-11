# Görüntü Çevirme

Rotasyon operatörü, bir giriş görüntüsündeki bir resim elemanının konumunu (x1, y1), bir kullanıcı tarafından belirlenen Q açısı boyunca döndürerek çıktı görüntüsündeki bir pozisyona (x2, y2) yerleştiren bir geometrik dönüşüm gerçekleştirir. Görüntünün sınırı dışında olan çıkış yerleri (x2, y2) dikkate alınmaz. Rotasyon en yaygın olarak bir görüntünün görsel görünümünü iyileştirmek için kullanılır, ancak yönlendirici operatörlerin dahil olduğu uygulamalarda bir önişlemci olarak yararlı olabilir. Döndürme özel bir affine dönüşümü olgusudur.
Rotasyon operatörünün dönüşüm formülü :

![image](https://user-images.githubusercontent.com/59111328/136799005-d761b258-665d-4625-91a6-67f7b150b7e8.png)
 
Burada (x0, y0) dönme merkezinin koordinatları (giriş görüntüsünde) ve Q, pozitif açılara sahip saat yönündeki dönüşleri olan  dönme açısıdır. (Burada, görüntü koordinatlarında çalıştığımıza dikkat edin, böylece y ekseni gider.) Y ekseninin yukarı doğru gelmesi için de benzer rotasyon formülü tanımlanabilir.) Çevirme operatöründen daha da fazlası, döndürme işlemi, görüntünün sınırlarına uymayan çıkış konumlarını (x2, y2) üretir. Orijinal giriş görüntüsünün boyutları. Bu gibi durumlarda, çoğu uygulama tarafından görüntünün dışında haritalanan hedef öğeler göz ardı edilir. Bir görüntünün döndürüldüğü piksel konumları genellikle siyah piksellerle doldurulur.

![image](https://user-images.githubusercontent.com/59111328/136799085-fcc278bc-95f9-4b9c-876c-c724bca8d7d5.png)
 
Döndürme algoritması, çeviri tarafından kullanılanın aksine, tam sayı olmayan koordinatlar (x2, y2) üretebilir. Her bir tamsayı konumunda piksellerin yoğunluğunun üretilmesi için, farklı buluşsal yöntemler (veya yeniden örnekleme teknikleri) kullanılabilir Örneğin, iki yaygın yöntem şunları içerir:
-	Her bir tamsayı piksel konumundaki yoğunluk seviyesinin, en yakın tam sayı olmayan komşunun (x2, y2) değerini almasına izin verin.
-	Her tamsayı piksel konumundaki yoğunluk düzeyini, n en yakın tam sayı olmayan değerlerin ağırlıklı ortalamasını temel alarak hesaplayın. Ağırlık, yakındaki projeksiyonların uzaklık veya piksel çakışmasıyla orantılıdır.
Sonuncu yöntem daha iyi sonuç verir, ancak algoritmanın hesaplama süresini artırır.

**Uygulaması:**

