import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("static\img\mean.jpg")

image = np.array(image)

original_shape = image.shape

X = np.reshape(image, [-1, 3])

plt.imshow(image)

bandwidth = estimate_bandwidth(X, quantile=0.1, n_samples=100)

print(bandwidth)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)

ms.fit(X)

labels = ms.labels_

print(labels.shape)

cluster_centers = ms.cluster_centers_

print(cluster_centers.shape)

labels_unique = np.unique(labels)

n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" %n_clusters_)

segmented_image = np.reshape(labels, original_shape[:2])  

plt.figure(2)

plt.subplot(1, 2, 1)

plt.imshow(image)

plt.axis('off')

plt.imsave("static\img\mean_1.jpg",image)

plt.subplot(1, 2, 2)

plt.imshow(segmented_image)

plt.axis('off')

plt.imsave("static\img\mean_yeni.jpg",segmented_image)
