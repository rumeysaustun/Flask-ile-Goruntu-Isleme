# Otsu Eşikleme Metodu

Adını geliştiricisi Nobuyuki Otsu’dan alan yöntem gri tonlamalı bir görüntüyü monokroma dönüştürmek için kullanılan yaygın bir görüntü işleme görevidir. Yöntem sadece renklerin görüntü üzerinde kaçar defa bulunduğuna bakar.Gri seviyedeki bir görüntüyü ikili seviyeye dönüştürülerek kullanılabilecek en uygun eşik değerinin tespitini sağlar.Bu yöntemde, renklerin görüntü üzerinde var olma sayısına bakıldığı için uygulamaların eşik belirleme adımına geçmeden önce renk histogramı hesaplanır ve tüm hesaplamalar bu histogram üzerinden yapılır. Otsu algoritması histogramda eşikleme yapılabilecek en uygun konumun bulunması için kullanılır.

Otsu algoritmasında histogramın her bir elemanını eşik gibi düşünerek her biri için **“weight”**,**"mean”** ve **”variance”** diye tabir edilen veriler hem eşikten önce *(background)* hem de eşikten sonrası *(foreground)* için hesaplanır.

Her bir eleman eşik kabul edilerek her bir eleman için hesaplamalar yapılacağı için belirlenen elemandan öncesi eşik öncesi(background),belirlenen elemandan sonrası eşik sonrası(foreground) olarak adlandırılır.

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/03-%20Otsu%20Eşikleme%20Yöntemi/Otsu%20Eşikleme%20Metodu%20Flask.py) kodlar uygulandığında aşağıdaki çıktılar elde edilir.<br>

Resmin orijinal hali:

![orijinall](https://user-images.githubusercontent.com/59111328/135831971-faad6dfc-0085-42c7-89c7-537c0d6d5b52.PNG)

Resmin gri hali:

![grii](https://user-images.githubusercontent.com/59111328/135831979-5ca29bbb-3092-41a5-903d-25f2a6c86aac.PNG)

Resmin otsu eşikleme ile son hali:

![yenii](https://user-images.githubusercontent.com/59111328/135831978-d430ecf3-0179-4add-9a9b-1dded4a00939.PNG)




