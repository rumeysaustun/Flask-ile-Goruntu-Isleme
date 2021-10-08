# Miniconda'ya Flask Kurulumu

- İlk olarak **Anaconda Prompt (miniconda3)** komut ekranı açılır.
- Flask'ı indirmek için ekrana 
```
python -m pip install Flask
```
komutu girilir.
- Deneme amacıyla 
```
python
>>> import flask
```
komutu girilir. Hata yok ise kurulum başarılıdır. ```exit()``` ile çıkış yapılabilir.
- Geliştiricimizi açmak için
```
jupyter-lab
```
komutu girilir. 
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
