from matplotlib.pyplot import savefig
import numpy as np
import matplotlib.image as mpimg
import pylab as plt
def imhist (im):
    m,n=im.shape
    h=[0.0]*256
    for i in range(m):
          for j in range(n):
             h[im[i,j]] += 1
    return np.array(h) / (m*n)
def cumsum(h):
     return [sum(h[:i+1]) for i in range(len(h))]
def histeq(im):
     h=imhist(im)
     cdf=np.array(cumsum(h))

     sk=np.uint8(255*cdf)
     s1,s2=im.shape
     new_im=np.zeros_like(im)
     for i in range(0,s1):
         for j in range(0,s2):
               new_im[i,j]=sk[im[i,j]]
     return new_im
img=np.uint(mpimg.imread("static\img\cicek.jpg")*255.0)

img = np.uint8(0.2126 * img[:,:,0]) +\
          np.uint8(0.7152 * img[:,:,1]) +\
          np.uint8(0.0722 * img[:,:,2])
new_img = histeq(img)
plt.subplot(121)
plt.imshow(img)
plt.title("Orjinal Resim")
plt.set_cmap("gray")
savefig("static\img\cicek_yeni.jpg")

plt.subplot(122)
plt.imshow(new_img)
plt.title("Histogram Esikleme Yapılan Resim")
plt.set_cmap("gray")
savefig("static\img\cicek_eskileme.jpg")
plt.show()
