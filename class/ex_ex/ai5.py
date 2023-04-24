import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance


# 期待値と分散共分散行列の準備
mean1 = np.array([3, 5])
cov1 = np.array([[3,-2], [-2, 2]])

mean2 = np.array([0,0])
cov2 = np.array([[0.1,0],[0,0.1]])

# numpy を用いた生成
data_1 = np.random.multivariate_normal(mean1, cov1, size=20)
data_2 = np.random.multivariate_normal(mean2, cov2, size=20)

fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.set_xlim([-4,8])
ax1.set_ylim([-4,8])
ax2.set_xlim([-4,8])
ax2.set_ylim([-4,8])

# 分散共分散行列と逆行列の計算
cov1 = np.cov(data_1.T)
cov2 = np.cov(data_2.T)
cov1_i = np.linalg.inv(cov1)
cov2_i = np.linalg.inv(cov2)

Sw = cov1+cov2
Sw_i = np.linalg.inv(Sw)

# クラス1の平均値
average1_x = np.average(data_1[:,0])
average1_y = np.average(data_1[:,1])
center1 = np.array([average1_x, average1_y])

# クラス2の平均値
average2_x = np.average(data_2[:,0])
average2_y = np.average(data_2[:,1])
center2 = np.array([average2_x, average2_y])
diff = center1-center2

# クラス1とクラス2との中点
mid = (center1+center2)/2

# Fisher の線形判別
# 傾き
w = np.matmul(Sw_i,center1-center2)

# クラスの中点を求める（傾きwで、aを通るのが判別式）
a = w[0]*mid[0]+w[1]*mid[1]

# 格子点を生成
dx = np.linspace(-4,8,50)
dy = np.linspace(-4,8,50)

#カウンターを作成
count1_red=0
count2_red=0

# Fisher
for y in range (50):
    for x in range(50):
        p = -w[1]/w[0]*dx[x]+a/w[1]-dy[y]
                
        # 近い方のクラスに判定する
        if(p<0):
            ax1.scatter(dx[x],dy[y],c="green",marker=".")
        else:
            ax1.scatter(dx[x],dy[y],c="red",marker=".")
            count1_red = count1_red+1 #カウントする

# Mahalanobis            
for y in range (50):
    for x in range(50):

        p = [dx[x],dy[y]]
        
        # クラス1とクラス2の平均からの距離を求める
        d1 = distance.mahalanobis(center1,p,cov1_i)
        d2 = distance.mahalanobis(center2,p,cov2_i)
        
        # 近い方のクラスに判定する
        
        if(d1<d2):
            ax2.scatter(dx[x],dy[y],c="green",marker=".")
        else:
            ax2.scatter(dx[x],dy[y],c="red",marker=".")
            count2_red = count2_red+1 #カウントする
        
ax1.scatter(data_1[:,0],data_1[:,1])
ax1.scatter(data_2[:,0],data_2[:,1])
ax2.scatter(data_1[:,0],data_1[:,1])
ax2.scatter(data_2[:,0],data_2[:,1])

plt.savefig("image.png")
if(count1_red>count2_red):
    print("red decrease",count1_red-count2_red)
else:
    print("red increase",count2_red-count1_red)
    
print(Sw)    
