from sklearn.decomposition import PCA
import numpy as np
from matplotlib import pyplot as plt


# ランダムにデータを作成
#teachers = np.random.rand(1000, 3)
teachers = np.zeros((1000,3)) #全部黒
#teachers[:,0] = 1 #赤
teachers[:,1] = 1 #緑
#eachers[:,2] = 1 #青

# PCAを実行
pca = PCA()
pca.fit(teachers)

# 主成分得点を求める
feature = pca.transform(teachers)

# 累積寄与率を求める
pca_contribution = pca.explained_variance_ratio_

# 固有値を求める
pca_lambda = pca.explained_variance_

# 固有ベクトルを求める
pca_vector = pca.components_

print (pca_contribution)

# プロット（結構時間がかかる）
for i in range (1000):
    plt.scatter(feature[i,0],feature[i,1],color=teachers[i,:])
plt.savefig("2.png")      