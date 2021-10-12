# Flask ile Ağırlık Toplama Yöntemi

Uygulamada renkli bir resim gri tonlarına dönüştürülecektir. Python dilinde resim dosyaları üzerinde işlem yapabilmek için **“Image”** kütüphanesini projeye dahil edilmelidir. Python dili için bu tür grafik kütüphanelerini içine bulunduran **“PIL”** paketini indirebilir. Bunun için terminalden ```pip3 install pillow``` komutunu yazarak ‘PIL’ paketini indirmiştik. Anaconda için ise ```conda install -c anaconda pillow``` komutu ile indirmek mümkündür. **Anaconda Prompt (miniconda3)** komut isteminden ``` Jupyter-lab ``` yazarak çıkan geliştirme ortamında kodu yazabilirsiniz.

Bu uygulamada ekranda görüntü alabilmek için ```resim.show()``` metodu kullanılır. Bu metodun çalışabilmesi için bir görüntüleme programına ihtiyaç vardır. Bunun ile ilgili yazıya [buradan](https://github.com/rumeysaustun/Flask/blob/main/05-%20Flask%20Sayfaya%20Kaynak%20Dosyalar%C4%B1%20Ekleme%20(CSS,JS,IMG%20vs).md#flask-sayfaya-kaynak-dosyalar%C4%B1-ekleme-cssjsimg-vsmd) ulaşabilirsiniz.

Bu sayede resmin adı kullanılarak resim çağrılabilir. Fakat resim ile dosya aynı klasörde değilse resmin olduğu yerin adresi kod parçasının ilgili kısmına yazılır. **agirliktoplama.jpg** olarak resmimizi kaydediyoruz. Bir de orijinal resim kaybolmasın diye resmin kopyasını **agirliktoplamaorijinal.jpg** olarak kaydediyoruz.

agirliktoplama.jpg dosyanın orjinal hali:

![pexels-james-wheeler-417074](https://user-images.githubusercontent.com/59111328/135749363-3be06750-ab4c-4ccb-91f2-73d9a2aba7f5.jpg)

Oluşacak agirliktoplama_yeni.jpg dosyası:

![agirliktoplama](https://user-images.githubusercontent.com/59111328/135749371-bba8afcc-0abc-4bc2-8e8c-12bede1803fe.jpg)

[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/01-%20Ağırlık%20Toplama/Flask%20ile%20Ağırlık%20Toplama.py) kodları uyguladığımızda ise aşağıdaki görüntüler ortaya çıkmaktadır.

![orijinal](https://user-images.githubusercontent.com/59111328/135750717-6667a50e-58f3-49df-be1c-f5278f1c2f3f.PNG)
![gri](https://user-images.githubusercontent.com/59111328/135750719-b21ed629-fa2d-4e06-a836-04e42756d0f2.PNG)
