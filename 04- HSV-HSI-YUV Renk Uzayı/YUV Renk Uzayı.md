# YUV Renk Uzayı

PAL, NTSC, SECAM kompozit renkli video standartlarında kullanılır.

Y, **ışıklılık (luma)**; U ve V **renklilik (chrominance)** bileşenleridir. YUV bileşenleri RGB’den türetilir.

Y, ortalama parlaklığı veren ve R, G, B bileşenlerinin ağırlıklı ortalaması ile elde edilen ışıklılık bileşeni; U, mavi bileşeninden Y’nin; V, kırmızı bileşeninden Y nin çıkarılması ile elde edilen fark bileşenleridir.

![uv-grafik](https://user-images.githubusercontent.com/59111328/136016277-633e8d4d-088c-4a66-85b4-c5afeb08d1b5.png)

Formüller şöyledir:

**Y=(0.257*R)+(0.504*G)+(0.098*B)+16**

**U =-(0.148*R)-(0.291*G)+(0.439*B)+128**

**V =(0.439*R)-(0.368*G)-(0.071*B)+128**
 
 ## YUV Uygulaması
 
 **Resmin orijinal hali:**

 <img src="https://user-images.githubusercontent.com/59111328/136017276-82e1725f-fee0-47f9-9ba8-0a55076af3cf.jpg" width = "300">
 
 **[Buradaki](https://github.com/rumeysaustun/Flask-ile-Goruntu-Isleme/blob/main/04-%20HSV-HSI-YUV%20Renk%20Uzayı/YUV.py) kod ile son hali:**
 
  <img src="https://user-images.githubusercontent.com/59111328/136017351-45d6e686-660a-4624-8e68-eb3c762cbd1f.jpg" width = "300">

