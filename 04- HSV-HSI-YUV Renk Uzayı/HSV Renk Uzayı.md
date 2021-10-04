# HSV Renk Uzayı

RGB renk uzayı genel olarak kullanılan renk uzayıdır. Bu renk uzayında üç ana bileşen kullanılır.Görüntü **R**(red), **G**(green), **B**(Blue) yani kırmızı, yeşil, mavi renk kodları üzerine tanımlanır. Her piksel bu renk kodlarına göre ara değerler alır. Böylece renkli bir resim elde edilir.

HSV renk uzayı ise **Hue(Renk), Saturation(Doygunluk) ve Value(Parlaklık)** terimleri ile rengi tanımlar.RGB de renklerin karışımı kullanılmasına karşın HSV de renk, doygunluk ve parlaklık değerleri kullanılır. Doygunluk rengin canlılığını belirlerken parlaklık rengin aydınlığını ifade eder. Örneğin; HSV uzayında siyah renk için renk ve doygunluk değerleri 0 ile 255 arasında herhangi bir değer alabilirken  parlaklık değeri sıfırdır. Beyaz renkte ise parlaklık değeri 255’tir. Buna göre herhangi bir bilgisayarlı görme/görüntü işleme uygulamasında belirli renkteki bir nesneyi ayırt etmek istenirse HSV renk uzayını kullanmak daha elverişlidir. Çünkü RGB renk uzayında eşik değeri için kullanılan filtreler yerine burada sadece Hue bileşeni ile eşik değeri belirlenebilir. Böylelikle daha net renkler elde edilebilir.

![hsv renk uzayo](https://user-images.githubusercontent.com/59111328/135860411-0c63b62e-d4ae-4c2a-bc94-5a55ac38d593.gif)

## HSV Modelleme

RGB renk uzayından HSV renk uzayına geçiş yapmak için belirli formüller kullanılır. Burada dikkat edilmesi gereken nokta RGB değerlerini 0-1 arasına indirilmesi gerekliliğidir.

Her pikselin değeri 255 ile bölünerek normalize edildikten sonra aşağıdaki formüller ile HSV değerleri bulunabilir.

İlk olarak görüntünün piksel değerlerinde bulunan renk kodları alınır .
**R' = R/255
G' = G/255
B' = B/255
Cmax = max (R', G', B')
Cmin = min (R', G', B')
Δ = Cmax - Cmin**



