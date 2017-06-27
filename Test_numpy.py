import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=50, normed=1)
plt.show()
(n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()

v = np.random.normal(mu.sigma, 10000)
plt.hist(v, bins=50, normed=1)
plt.show()
(n, bins) = np.histogram(v, bins=50, normed=True)
