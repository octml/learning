#-*- coding utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mlpy
np.random.seed(0)
mean1, cov1, n1 = [1, 4.5], [[1,1],[1,2]], 20  # 20 samples of class 1
x1 = np.random.multivariate_normal(mean1, cov1, n1)
y1 = np.ones(n1, dtype=np.int)

mean2, cov2, n2 = [2.5, 2.5], [[1,1],[1,2]], 30 # 30 samples of class 2
x2 = np.random.multivariate_normal(mean2, cov2, n2)
y2 = 2 * np.ones(n2, dtype=np.int)

x = np.concatenate((x1, x2), axis=0) # concatenate the samples
y = np.concatenate((y1, y2))

K = mlpy.kernel_gaussian(x, x, sigma=2) # kernel matrix
xmin, xmax = x[:,0].min()-1, x[:,0].max()+1
ymin, ymax = x[:,1].min()-1, x[:,1].max()+1
xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.02), np.arange(ymin, ymax, 0.02))
xt = np.c_[xx.ravel(), yy.ravel()] # test points
Kt = mlpy.kernel_gaussian(xt, x, sigma=2) # test kernel matrix
fig = plt.figure(1)
cmap = plt.set_cmap(plt.cm.Paired)
for i, c in enumerate([1, 10, 100, 1000]):
    ka = mlpy.KernelAdatron(C=c)
    ax = plt.subplot(2, 2, i+1)
    ka.learn(K, y)
    ytest = ka.pred(Kt).reshape(xx.shape)
    title = ax.set_title('C: %s; margin: %.3f; steps: %s;' % (c, ka.margin(), ka.steps()))
    plot1 = plt.pcolormesh(xx, yy, ytest)
    plot2 = plt.scatter(x[:,0], x[:,1], c=y)
plt.show()