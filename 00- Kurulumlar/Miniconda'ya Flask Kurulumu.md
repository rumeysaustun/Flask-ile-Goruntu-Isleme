# Miniconda'ya Flask Kurulumu

- İlk olarak **Anaconda Prompt (miniconda3)** komut ekranı açılır.
- Flask'ı indirmek için ekrana 
```
pip install Flask
```
komutu girilir.<br>

![flask indir](https://user-images.githubusercontent.com/59111328/136689349-a3beef94-85a7-459a-a9c5-c472bb34ea77.PNG)


- Deneme amacıyla 
```
python
>>> import flask
```
komutu girilir. Hata yok ise kurulum başarılıdır. ```exit()``` ile çıkış yapılabilir.

![python](https://user-images.githubusercontent.com/59111328/136689357-9a335818-a737-41e4-8202-580860332594.PNG)


- Geliştiricimizi açmak için
```
jupyter-lab
```
komutu girilir. 

![lab](https://user-images.githubusercontent.com/59111328/136689362-3802a37a-14db-47c2-8648-759a2c0731fe.PNG)


- Açılan geliştirme ortamında ilk FLask projemizi denemek amacıyla aşağıdaki kodlar yazılır ve çalıştırılır.

```
from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello():

    return "Hello World!"
if __name__ == '__main__':

   app.run()
```
![run](https://user-images.githubusercontent.com/59111328/136689366-0df9adf6-d7fe-488c-9887-3c383a2e9c38.PNG)

- Alt kısımda çıkan **http://127.0.0.1:5000/** yönlendiriciye tıklanır.

![helloworld](https://user-images.githubusercontent.com/59111328/136689370-3fff9125-9d8f-41e5-a377-33d11fa85172.PNG)

