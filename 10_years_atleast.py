# import numpy as np
from scipy.stats import binom
alpha = 0
t = 111
m = 15
r = 0
n = t - (r - 1)*(m - 1)
rho = 0.01
print(1 - binom.cdf(r-1, n, rho))
