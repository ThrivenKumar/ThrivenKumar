import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from sklearn.mixture import GaussianMixture
df=pd.read_csv("/Users/thrivenkumar/Downloads/9e5938fc2ce611eb/train.csv",sep=",")
arr=df[['customer_visit_score','customer_order_score']].to_numpy(dtype=np.float32)
#X = np.array([[1, 2], [1, 4], [1, 0],[10, 2], [10, 4], [10, 0]])
for i in range(len(arr)):
    if math.isnan(arr[i,1]):
        arr[i,1]=0
#kmeans = KMeans(n_clusters=2, random_state=0).fit(arr)
#print(kmeans.cluster_centers_)

model = GaussianMixture(n_components=2)
# fit the model
model.fit(arr)
# assign a cluster to each example
yhat = model.predict(arr)
# retrieve unique clusters
clusters = np.unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = np.where(yhat == cluster)
	# create scatter of these samples
	plt.scatter(arr[row_ix, 0], arr[row_ix, 1])


"""fig,ax=plt.subplots()
ax.scatter(arr[:,0], arr[:,1], color= "red",marker= ".", s=5)
ax.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="black",marker=".",s=20)"""
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()
