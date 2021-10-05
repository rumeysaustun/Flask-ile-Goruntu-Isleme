# YUV Renk Uzayı

PAL, NTSC, SECAM kompozit renkli video standartlarında kullanılır.

Y, **ışıklılık (luma)**; U ve V **renklilik (chrominance)** bileşenleridir. YUV bileşenleri RGB’den türetilir.

Y, ortalama parlaklığı veren ve R, G, B bileşenlerinin ağırlıklı ortalaması ile elde edilen ışıklılık bileşeni; U, mavi bileşeninden Y’nin; V, kırmızı bileşeninden Y nin çıkarılması ile elde edilen fark bileşenleridir.

![uv-grafik](https://user-images.githubusercontent.com/59111328/136016277-633e8d4d-088c-4a66-85b4-c5afeb08d1b5.png)

Formüller şöyledir:

**Y=(0.257*R)+(0.504*G)+(0.098*B)+16**

**U =-(0.148*R)-(0.291*G)+(0.439*B)+128**

**V =(0.439*R)-(0.368*G)-(0.071*B)+128**
