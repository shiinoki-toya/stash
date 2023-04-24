
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import numpy as np
 
df = np.loadtxt('iris.csv', delimiter=',')

sc = preprocessing.StandardScaler()
sc.fit(df)
df_norm = sc.transform(df)
 
# クラスタリング
cls = KMeans(n_clusters=3)
result = cls.fit(df_norm)
# 結果を出力
plt.scatter(df_norm[:,0],df_norm[:,1], c=result.labels_)
plt.scatter(result.cluster_centers_[:,0],result.cluster_centers_[:,1],s=250, marker='*',c='red')
plt.savefig('result_k-means.png')