# Canny Kenar Belirleme

Canny kenar belirleme algoritması; görüntüde keskin olarak belirlenmiş kenarları bulmak için John F. Canny tarafından geliştirilmiş ve aşamaları olan bir algoritmadır. Kenar bulmada son derece etkin olarak kullanılan bir algoritmadır. Aşamaları maddeleyecek olursak; Görüntünün gürültülerini azaltmak amacıyla Gaussian çekirdekle konvolüsyon alınarak azaltılır. Gaussian filtre dışında Mean ya da Medyan filtre de kullanılabilir. . Gradyan operatörü uygulanır. Bu şekilde görüntünün Gradyan büyüklüğü ve yönü hesaplanır. Bu işlem için Sobel filtresi en çok kullanılan yöntemdir. Bunun dışında Prewitt ve Robert kenar bulma metotları da mevcuttur. . Kenarlar Non Maxima baskılama kullanılarak incelemeye alınır. . İkili eşikleme uygulanır bu şekilde istenmeyen ayrıntılardan arındırılma işlemi gerçekleştirilir. . Güçlü-zayıf ayrımı yapıldıktan sonra baskılama uygulanır ve asıl kenarlarla görüntüye son hali verilir.

## Gaussian Filtresi

Kenar bulma işlemi için görüntüde yumuşatma yapılmalıdır. Gaussian filtresi görüntüleri bulanıklaştırmak/yumuşatmak ve görüntü üzerindeki gürültüyü arındırmak için kullanılır.
Gaussian fonksiyonu:




