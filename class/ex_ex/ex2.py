import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
cm = plt.get_cmap("tab10")

def f(x, y, mu, S):
  x_norm = (np.array([x, y]) - mu[:, None, None]).transpose(1, 2, 0)
  return np.exp(- x_norm[:, :, None, :] @ np.linalg.inv(S)[None, None, :, :] @ x_norm[:, :, :, None] / 2.0) / (2*np.pi*np.sqrt(np.linalg.det(S)))

x = y = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(x, y)

#平均
mu = np.array([0,0])
mu2 = np.array([10,10])

#共分散行列
S = np.array([[20,0],[0,20]])
S2 = np.array([[1,0],[0,40]])

Z = f(X,Y, mu, S)[:, :, 0, 0]
#平均が異なり分散は等しい
Z2 = f(X,Y, mu2, S)[:, :, 0, 0]
#平均が等しく分散が異なる
Z3 = f(X,Y, mu, S2)[:, :, 0, 0]

fig2 = plt.figure()
ax2 = plt.subplot(111)

#平均が異なり分散は等しい
cs = ax2.contourf(X*2,Y*2,Z+Z2,100)
plt.savefig("ex1.png")

#平均が等しく分散が異なる
cs2 = ax2.contourf(X*2,Y*2,Z+Z3,100)
plt.savefig("ex2.png")