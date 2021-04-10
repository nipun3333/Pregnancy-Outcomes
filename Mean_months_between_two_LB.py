m = 15   # infecundable period (in months) after L conception
w = 6    # infecundable period (in months) after fetal loss
rho = 0.270170263818779   # probability of conception (assuming contraceptive is used)
alpha = 0.25  # aplha = mortality
q = 1 - rho   # Monthy probability that no conception occurs
p = (1-alpha)*rho   # Monthly probability that conception ends in live birth
pi = alpha*rho    # Monthly probability that conception ends in fetal loss
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
