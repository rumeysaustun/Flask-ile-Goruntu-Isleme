# Flask ile Ağırlık Toplama Yöntemi

Uygulamada renkli bir resmi gri tonlarına dönüştüreceğiz. Python dilinde resim dosyaları üzerinde işlem yapabilmek için **“Image”** kütüphanesini projeye dahil edilmelidir. Python dili için bu tür grafik kütüphanelerini içine bulunduran **“PIL”** paketini indirebilir. Bunun için terminalden ```pip3 install pillow``` komutunu yazarak ‘PIL’ paketini indirmiştik. PyCharmda Python Projesi açarak  kodlar yazılabilir.

Bu uygulamada ekranda görüntü alabilmek için ```resim.show()``` metodu kullanılır. Bu metodun çalışabilmesi için bir görüntüleme programına ihtiyaç vardır.
Griye dönüştürülecek resim PyCharmda Python projelerinin olduğu dosyanın içindeki venv klasöründe bulunmalıdır.Örneğin;
/home/gorountuisleme/PycharmProjects/deneme/venv

Bu sayede resmin adı kullanılarak resim çağrılabilir.Fakat resim ile dosya aynı klasörde değilse resmin olduğu yerin adresi kod parçasının ilgili kısmına yazılır. **agirliktoplama.jpg** olarak resmimizi kaydediyoruz.

agirliktoplama.jpg dosyanın orjinal hali:

![pexels-james-wheeler-417074](https://user-images.githubusercontent.com/59111328/135749363-3be06750-ab4c-4ccb-91f2-73d9a2aba7f5.jpg)

Oluşacak agirliktoplama_yeni.jpg dosyası:

![agirliktoplama](https://user-images.githubusercontent.com/59111328/135749371-bba8afcc-0abc-4bc2-8e8c-12bede1803fe.jpg)

