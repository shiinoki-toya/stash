import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage

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


# クラスタリング
x = np.loadtxt('iris.csv', delimiter=',')
linked = linkage(x,'ward') # ワード法なので wardを指定している。

# 描画のためのラベルの付けなおし
n = x.shape[0]
group=np.empty(n,dtype='int32')
step=0

# 終了条件（ここではクラスタ数で終了条件を決めている。）
num_cluster = 3
while True:
    if step>= n-num_cluster:
        break
    dist = linked[step,2]   
    rewrite_id(step+n, linked, group, step, n)
    step=step+1



# 結果のプロット
cmap = plt.get_cmap("tab10")
cids = list(set(group))


for i in range(x.shape[0]):
    ell = cids.index(group[i]) % 10
    plt.scatter(x[i,0], x[i,1], color=cmap(ell))
plt.grid(True)
plt.savefig("result_ward2.png")