r = 1
m = 15
w = 6
rho = 0.01
alpha = 0.1
q = 1 - rho
p = (1-alpha)*rho
pi = alpha*rho

E1 = 9 + (r-1)*m + r*(q + w*pi)/p + 10
print(f'Mean number of months for {r}th live birth is {E1}')
