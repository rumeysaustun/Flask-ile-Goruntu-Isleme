# Canny Kenar Belirleme

Canny kenar belirleme algoritması; görüntüde keskin olarak belirlenmiş kenarları bulmak için John F. Canny tarafından geliştirilmiş ve aşamaları olan bir algoritmadır. Kenar bulmada son derece etkin olarak kullanılan bir algoritmadır. Aşamaları maddeleyecek olursak; Görüntünün gürültülerini azaltmak amacıyla Gaussian çekirdekle konvolüsyon alınarak azaltılır. Gaussian filtre dışında Mean ya da Medyan filtre de kullanılabilir. Gradyan operatörü uygulanır. Bu şekilde görüntünün Gradyan büyüklüğü ve yönü hesaplanır. Bu işlem için Sobel filtresi en çok kullanılan yöntemdir. Bunun dışında Prewitt ve Robert kenar bulma metotları da mevcuttur. Kenarlar Non Maxima baskılama kullanılarak incelemeye alınır. İkili eşikleme uygulanır bu şekilde istenmeyen ayrıntılardan arındırılma işlemi gerçekleştirilir. Güçlü-zayıf ayrımı yapıldıktan sonra baskılama uygulanır ve asıl kenarlarla görüntüye son hali verilir.

## Gaussian Filtresi

Kenar bulma işlemi için görüntüde yumuşatma yapılmalıdır. Gaussian filtresi görüntüleri bulanıklaştırmak/yumuşatmak ve görüntü üzerindeki gürültüyü arındırmak için kullanılır.
Gaussian fonksiyonu:

![gauss](https://user-images.githubusercontent.com/59111328/136355830-bb35ebbe-13e3-4823-b11a-4f544ac79bb7.PNG)

Denklemde kullanılan σ değeri dağılımın standart sapmadır. Dağılımın ortalama 0 değere sahip olduğu varsayılmaktadır.

<img src = "https://user-images.githubusercontent.com/59111328/136355986-3c462e8f-bb0d-4a3e-8b78-3b83709766c5.jpg" width="400">

Gaussian fonksiyonu için önemli olabilecek bazı değerler tabloda gösterilmiştir.

![image](https://user-images.githubusercontent.com/59111328/136356061-9ba907f3-9897-4e46-b31b-88ac67e69411.png)

Gaussian fonksiyonu birçok araştırma alanında kullanılmaktadır: 

- Gürültü veya bir veri için olasılık dağılımı tanımlar. 
- Yumuşatma için kullanılan bir operatördür.
- Matematikte kullanılır.
- Gaussian görüntü işlemede çalışılırken 2 boyutlu Gaussian fonksiyonuna ihtiyaç duyulmaktadır.

## Mean Filtresi

Mean filtresi alçak geçiren filtre olarak çalışmaktadır. Alçak geçiren filtre belirli bir frekansın üzerinde kalan sinyallerin işlenmesini sağlayan filtredir. Mean filtrenin çalışma mantığı; pencerede bulunan piksel değerinin diğer tüm piksel değerlerinin ortalaması ile değiştirerek çalışır. Pencere genellikle karedir yani matris olarak düşünülürse nxn boyutunda kare matristir. Filtrenin çalışma mantığı bir örnekle gösterilecek olursa:

![image](https://user-images.githubusercontent.com/59111328/136356330-446395cf-64ed-44d3-b056-3fc6a55f5b5f.png)

![image](https://user-images.githubusercontent.com/59111328/136356372-fb7319f2-f09c-41a0-aa4c-4741706b7a56.png)

![image](https://user-images.githubusercontent.com/59111328/136356389-2677570f-8763-46e0-8ba9-43baa656304b.png)

## Gradyan Operatörünün Bulunması

Kenarların belirlenmesinde 3 adet işleç kullanılmaktadır. Sobel işleci, Prewitt işleci ve Robert işleçleridir.

### Sobel İşleci 

Sayısal bir görüntü, bir fonksiyon olarak değerlendirildiğinde, bir nokta üzerindeki gradyan değerinin, 3×3 komşulukta mümkün olan dört merkezi yönde elde edilebilir. Gradyan değerlerinin vektör toplamları şeklinde oluşturulması düşüncesine dayanmaktadır.

Bu gradyan değerlerinin vektör toplamları; gradyan ölçümleri üzerinde ortalama değer bulunmasını sağlamaktadır. 3×3’lük komşuluk için merkez noktanın gradyan değeri, dik vektör çiftlerinin vektör toplamları olarak bulunmaktadır.
Sobel işlecinde iki adet konvolüsyon çekirdeği yer alır. Bunlar görüntü içerisindeki ani ışık yoğunluk değişimi olan yerlerin belirlenmesini sağlar.

### Prewitt İşleci 

Sobel işleci gibi düşey ve yatay keskinlik sağlamaktadır. Sobel işlece göre daha basittir ama sonucunu değerlendirecek olursak biraz daha gürültü içermektedir.

### Robert İşleci

Görüntü işlemede kullanılan en eski işleçtir. Bu işleçle sadece yatay ya da sadece düşey olarak kenarlar elde edilmektedir. Hızlı ve basit bir uygulamaya sahip olduğundan gerçek zamanlı uygulamalarda çokça tercih edilmektedir.

## Kenar İnceltme

İşleçler ile elde edilen görüntülerde kenarlar kalındır. Kenarların bir piksel gibi ince gösterilmesi için çeşitli metotlar geliştirilmiştir. Bu yöntemlerden en başarılısı maksimum olmayan piksel değerlerinin bastırılması yöntemidir.

Çalışma mantığına bakılacak olursa; görüntü, görüntünün gradyanı yönünde taranır ve pikseller yerel maksimumun parçası değillerse sıfıra ayarlanır.
Gradyan Yönü: arctan(Gy /Gx) ile tayin edilmektedir.

Her bir piksel için gradyan yönü hesaplandıktan sonra, elde edilen açı değeri istikametindeki iki ilave komşu piksel seçilerek, ortanca pikselin bunlardan yüksek değerde olması istenir. Bu şart sağlanmaz ise, ortanca piksel sıfıra çekilerek kenar resminden elenir. Bu şekilde, kenar resminde sadece kenarlara dik yönde maksimum gradyan değerlerine sahip olan pikseller bırakılır.

Bulunan Gradyan operatörünün komşuluğunun incelenmesi için öncelikle, açı değerlerinin belirlenmesi gereklidir. Bunun için de kenar ayrımlarını saptayacağımız renk açılarını kullanmalıyız. Her renk değeri belirli aralıklar içerisinde kalır. Bunları şöyle bir formül ile hesaplayacağız.Sarı aralıktaki herhangi bir kenar yönü 0 derece olarak ayarlanır. Yeşil yönde düşen herhangi bir kenar yönü 45 dereceye ayarlanır. Mavi aralıktaki herhangi bir kenar yönü 90 dereceye ayarlanır. Son olarak, kırmızı yönde kalan herhangi bir kenar yönü 135 dereceye ayarlanır.

## İkili Eşikleme Ve Kenar Ayrımı

Gradyan genlik resminin belirli bir aralığa normalize edilmesi ve kenarların diki boyunca maksimum olmayanların bastırılması sonrasında elde edilen kenar resmi, piksel sürekliliği aşamasına girer. Kenar resmindeki piksel sürekliliğinin test edilmesi amacıyla yüksek ve düşük seviyede iki eşik değeri
kullanılır. Süreklilik testi için şu adımlar uygulanır:
Yüksek ve düşük seviye olmak üzere iki adet eşik seviyesi belirlenir.
Her bir nokta için Eğer kenara dik maksimum gradyan genliği (piksel değeri) yüksek eşikten yüksek ise, kenar olarak bırakılır.
Eğer kenara dik maksimum gradyan genliği düşük eşikten düşük ise, sıfıra çekilir.
Eğer, piksel değeri, yüksek ve düşük eşik arasında ise, bu pikselin yüksek eşiği aşan bir komşusu var ise kenar olarak kalmasına izin verilir.
Eğer ki eşiği aşan bir komşusu yok ise sıfıra çekilerek kenar resminden elenir.


## Uygulaması

**Orijinal:**

<img src = "https://user-images.githubusercontent.com/59111328/136357938-b757ed3e-331c-4693-adfb-c13e2b7c6305.jpg" width="400">

**Gri tonlarına dönüşmüş hali:**

<img src = "https://user-images.githubusercontent.com/59111328/136358566-650b2b5a-5e52-4e65-ba5d-bcc64e2486e6.jpg" width="400">

**Mean filtresinden geçmiş hali:**

<img src = "https://user-images.githubusercontent.com/59111328/136358730-8f2d4352-5e47-45c0-8847-75f19f9c6542.jpg" width="400">

**Robert kenar belirleme işleminden geçmiş hali:**

<img src = "https://user-images.githubusercontent.com/59111328/136358815-11dec9d8-f9ef-4382-8986-fc0fac7adee9.jpg" width="400">

**Non makima işleminden geçmiş hali:**

<img src = "https://user-images.githubusercontent.com/59111328/136358921-52800174-904d-4f33-a5f0-9cd1183d75c3.jpg" width="400">

**İkili eşikleme işleminden geçmiş hali:**

<img src = "https://user-images.githubusercontent.com/59111328/136359002-613383e1-bfa0-43eb-b2ff-233f5e2bbb9d.jpg" width="400">








