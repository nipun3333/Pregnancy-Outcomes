r = 1  # number of birth
m = 15  # infecundable period (in months) after L conception
w = 6   # infecundable period (in months) after fetal loss
rho = 0.01  # probability of conception (assuming contraceptive is used)
alpha = 0.1  # aplha = mortality
q = 1 - rho   # Monthy probability that no conception occurs
p = (1-alpha)*rho   # Monthly probability that conception ends in live birth
pi = alpha*rho    # Monthly probability that conception ends in fetal loss

E1 = 9 + (r-1)*m + r*(q + w*pi)/p + 10
print(f'Mean number of months for {r}th live birth is {E1}')
