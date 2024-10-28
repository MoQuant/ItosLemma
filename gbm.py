import numpy as np
import matplotlib.pyplot as plt
import random as rd

def dWT():
    return rd.randint(-10, 10)/100.0

def GBM(S, mu, v, t, n):
    W_t = np.cumsum([dWT() for i in range(n)])
    return S*np.exp((mu - 0.5*pow(v, 2))*t + v*W_t)


S0 = 100
mu = 0.05
vol = 0.25
t = 12/365.0
n = 1000
paths = 200

fig = plt.figure()
ax = fig.add_subplot(111)

stockPrice = 0
for p in range(paths):
    price = GBM(S0, mu, vol, t, n)
    x = list(range(len(price)))
    ax.plot(x, price, color='blue', linewidth=0.8)
    stockPrice += price[-1]
    ax.set_title(f'Stock Price: {stockPrice/(p+1)}')
    plt.pause(0.1)

plt.show()
