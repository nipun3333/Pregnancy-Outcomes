m = 15
w = 6
rho = 0.3
alpha = 0
q = 1 - rho
p = (1-alpha)*rho
pi = alpha*rho
l = []

for r in range(1, 6):
    E1 = 9 + (r-1)*m + r*(q + w*pi)/p + 10
    # print(f'Mean number of months for {r}th live birth is {E1}')
    l.append(E1)

count = 0
summ = 0
for i in range(1, len(l)):
    count += 1
    # print(summ)
    summ += (l[i] - l[i-1])

print(f'Mean Interval Betweeen two Live Births is {summ/count}')
