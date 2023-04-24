import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from sklearn import preprocessing

def rewrite_id(id, link, group, step, n):
    i = int(link[step,0])
    j = int(link[step,1])
    if i<n:
        group[i] = id
    else:
        rewrite_id(id, link, group, i-n, n)

    if j<n:
        group[j] = id
    else:
        rewrite_id(id, link, group, j-n, n)

df = np.loadtxt('iris.csv', delimiter=',')

sc = preprocessing.StandardScaler()
sc.fit(df)
df_norm = sc.transform(df)

# クラスタリング

linked = linkage(df_norm,'ward')

n = df_norm.shape[0]
threshold=40
group=np.empty(n,dtype='int32')
step=0
while True:
    if step>= n-2:
        break
    dist = linked[step,2]   
    if dist>threshold:
        break
    rewrite_id(step+n, linked, group, step, n)
    step=step+1

# 結果のプロット

cmap = plt.get_cmap("tab10")
cids = list(set(group))

print('cluster ids:',cids)

for i in range(df_norm.shape[0]):
    ell = cids.index(group[i]) % 10
    plt.scatter(df_norm[i,0], df_norm[i,1], color=cmap(ell))
plt.grid(True)

plt.savefig('result_ward.png')