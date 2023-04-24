import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons

from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
import mglearn

# 学習データの生成
np.random.seed(2)
n=50

moons = make_moons(n_samples=n*2, noise=0.1, random_state=0,shuffle=False)
x1=moons[0][0:n,0]
y1=moons[0][0:n,1]
z1=np.zeros(n)+1
x2=moons[0][n:n*2,0]
y2=moons[0][n:n*2,1]
z2=np.zeros(n)-1

data=np.zeros((n*2,3))
data[0:n,0]=x1
data[0:n,1]=y1
data[0:n,2]=0
data[n:n*2,0]=x2
data[n:n*2,1]=y2
data[n:n*2,2]=1

mlp = MLPClassifier(hidden_layer_sizes=(1000), max_iter = 200000)
#mlp = MLPClassifier(hidden_layer_sizes=(5,5), max_iter = 200000)
#mlp = MLPClassifier(hidden_layer_sizes=(5,5,5), max_iter = 200000)
#mlp = MLPClassifier(hidden_layer_sizes=(5,5,5,5,5), max_iter = 200000)

mlp.fit(data[:,0:2], data[:,2])


# 描画
plt.figure(figsize=(12, 8))
_x1 = np.linspace(data[:, 0].min() - 0.5, data[:, 0].max() + 0.5, 100)
_x2 = np.linspace(data[:, 1].min() - 0.5, data[:, 1].max() + 0.5, 100)
x1, x2 = np.meshgrid(_x1, _x2)
X_stack = np.hstack((x1.ravel().reshape(-1, 1), x2.ravel().reshape(-1, 1)))

y_pred = mlp.predict(X_stack).reshape(x1.shape)
custom_cmap = ListedColormap(['mediumblue', 'orangered'])
plt.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)
mglearn.discrete_scatter(data[:,0],data[:,1], data[:,2])
plt.savefig("re.png")