# import numpy as np
from scipy.stats import binom
alpha = 0
t = 171
m = 15
r = 2
n = t - (r - 1)*(m - 1)
rho = 0.01
print(1 - binom.cdf(r-1, n, rho))
