from scipy.special import binom
from scipy.special import comb
import matplotlib.pyplot as plt
import math

n = 15
lamda = 5
theta = 28
i = 3
r = 2
q = 1/r
Pr_of_O = 0.95
month = 30

# assumed:
tau = n/theta


eqn3 = (comb(n, i))
eqn3 *= pow(lamda/theta, n)
eqn3 *= pow(((theta/lamda)-1), n-i)

eqn4 = comb(lamda, r)*comb(i-1, r-1)/comb(lamda+i-1, i)

eqn5 = (eqn4*q)

tempEqn5 = 0
for i in range(1, r+1):
    tempEqn5 += pow(1-q, i-1)

eqn5 *= tempEqn5

eqn2 = eqn5*eqn3*Pr_of_O


eqn1Temp = (pow(math.e, -(tau*theta)))
eqn1Temp *= pow(tau*theta, n)/math.factorial(n)

eqn1 = eqn2*eqn1Temp

# for high cycle
Pr_X1 = (lamda+month)/theta
Pr_X0 = 1-Pr_X1
Pr_X2 = 0


# For intermediate cycle
Pr_X00 = 0
Pr_X22 = (lamda/theta)
Pr_X11 = 1-Pr_X22

# For Short Cycle
Pr_X000 = 0
Pr_X222 = 2-((lamda+month)/theta)
Pr_X111 = ((lamda+month)/theta)-1

Pr_C_given_X0 = 0
Pr_C_given_X1 = eqn1
Pr_C_given_X2 = eqn1*(2-eqn1)

Pr_C = Pr_X0*Pr_C_given_X0 + Pr_X1*Pr_C_given_X1+Pr_X2*Pr_C_given_X2
Pr_C1 = Pr_X00*Pr_C_given_X0 + Pr_X11*Pr_C_given_X1+Pr_X22*Pr_C_given_X2
Pr_C2 = Pr_X000*Pr_C_given_X0 + Pr_X111*Pr_C_given_X1+Pr_X222*Pr_C_given_X2


Pl = 0.28
g = 1.8
Pe = (Pr_C*(1-Pl))/(1+Pr_C*Pl*g)
Pe1 = (Pr_C1*(1-Pl))/(1+Pr_C1*Pl*g)
Pe2 = (Pr_C2*(1-Pl))/(1+Pr_C2*Pl*g)


print("eqn1: ", eqn1)
print("eqn2: ", eqn2)
print("eqn3: ", eqn3)
print("eqn4: ", eqn4)
print("eqn5: ", eqn5)

print("Total Fecundability for high cycle: ", Pr_C)
print("Total Fecundability for intermediate cycle: ", Pr_C1)
print("Total Fecundability for lower cycle: ", Pr_C2)
print("Effective Fecundability for higher cycle: ", Pe)
print("Effective Fecundability for Intermediate cycle: ", Pe1)
print("Effective Fecundability for lower cycle: ", Pe2)
