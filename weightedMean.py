from scipy.stats import binom
from scipy.special import comb
m = 15
t = 111
w = 6

rho = 0.01
alpha = 0.1
ans = 0

mean = 0
for r in range(6):
    temp = (1-alpha)**r
    for v in range(18):
        temp2 = alpha**v
        print()
        temp1 = comb(r+v-1, v)
        ndash = t - (r-1)*(m-1) - v*(w-1)
        temp3 = (1 - binom.cdf(r+v-1, ndash, rho))
        ans += (temp1*temp2*temp3)
    ans *= temp
    # print(ans)
    mean += (ans*r)
    print(r, ans, mean)

mean /= 6
print(mean)
