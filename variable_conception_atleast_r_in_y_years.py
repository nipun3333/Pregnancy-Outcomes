from scipy.stats import binom
from scipy.special import comb
import matplotlib.pyplot as plt
import math
import numpy as np

#Part of our innovation
def conception_probability():
    """
    :returns: probability of conception
    """
    n = 15   # Coital Frequency in one cycle
    tau = 0.26  # mean daily probability of intercourse
    theta = 28  # Cycle Length
    lamda = 4  # Fertile Period in one cycle
    q = 0.6  # Probablity of conception from single day of intercourse
    pr_of_o = 0.95  # Probability that cycle is ovulatory
    month = 30  # Number of days in a month

    # eqn1
    eqn1 = 0

    for e1 in range(0, n + 1):

        eqn1Temp2 = (pow(math.e, -(tau * theta)))
        eqn1Temp2 *= pow(tau * theta, e1) / math.factorial(e1)  #Prob of Coital frequency using Poison distribution

        eqn2 = 0
        for i in range(1, e1 + 1):
            eqn2Temp2 = (comb(e1, i)) * pow(lamda / theta, e1) * pow(((theta / lamda) - 1), e1 - i)
            eqn5 = 0
            for r in range(1, lamda + 1):
                eqn4 = comb(lamda, r) * comb(i - 1, r - 1) / comb(lamda + i - 1, i)
                eqn5Temp1 = eqn4 * q
                eqn5Temp2 = 0
                for x in range(1, r + 1):
                    eqn5Temp2 += (pow(1 - q, x - 1))
                eqn5 += eqn5Temp1 * eqn5Temp2
            eqn2 += eqn2Temp2 * eqn5 * pr_of_o

        eqn1 += eqn1Temp2 * eqn2

    # for high cycle
    Pr_X1 = (lamda + month) / theta
    Pr_X0 = 1 - Pr_X1
    Pr_X2 = 0

    # For intermediate cycle
    Pr_X00 = 0
    Pr_X22 = (lamda / theta)
    Pr_X11 = 1 - Pr_X22

    # For Short Cycle
    Pr_X000 = 0
    Pr_X111 = 2 - ((lamda + month) / theta)
    Pr_X222 = ((lamda + month) / theta) - 1

    Pr_C_given_X0 = 0
    Pr_C_given_X1 = eqn1
    Pr_C_given_X2 = eqn1 * (2 - eqn1)

    Pr_C = Pr_X0 * Pr_C_given_X0 + Pr_X1 * Pr_C_given_X1 + Pr_X2 * Pr_C_given_X2
    Pr_C1 = Pr_X00 * Pr_C_given_X0 + Pr_X11 * Pr_C_given_X1 + Pr_X22 * Pr_C_given_X2
    Pr_C2 = Pr_X000 * Pr_C_given_X0 + Pr_X111 * Pr_C_given_X1 + Pr_X222 * Pr_C_given_X2

    Pl = 0.28
    g = 1.8
    Pe = (Pr_C * (1 - Pl)) / (1 + Pr_C * Pl * g)
    Pe1 = (Pr_C1 * (1 - Pl)) / (1 + Pr_C1 * Pl * g)
    Pe2 = (Pr_C2 * (1 - Pl)) / (1 + Pr_C2 * Pl * g)

    print("Prob of conception for in cycle: ", eqn1)
    print()
    print("Prob of conception in a month for a high cycle: ", Pr_C)
    print("Prob of conception in a month for a intermediate cycle: ", Pr_C1)
    print("Prob of conception in a month for a low cycle: ", Pr_C2)
    print()
    print("Prob of effective conception for high cycle : ", Pe)
    print("Prob of effective conception for intermediate cycle : ", Pe1)
    print("Prob of effective conception for low cycle : ", Pe2)

    return Pe2


def findv(t, r, m, w):
    """
    :param t: total number of months
    :param r: numbers of Live birth which has occured
    :param m: infecundable period (in months) after L conception
    :param w: infecundable period (in months) after fetal loss
    :return: maximum value of fetal loss possible given r, t, m and w
    """
    return (t-1-(r-1)*m)//w


def find_ndash(t, r, m, v, w):
    """
    :return: availabe months for conception
    """
    return t - (r-1)*(m-1) - v*(w-1)


if __name__ == '__main__':
    y = 10           # Number of years taken in consideration
    alpha = 0.25   # aplha = mortality (probability that a given conception will end in fetal loss)
    m = 15           # infecundable period (in months) after L conception
    t = y * 12 - 9   # number of months - calculated from years(y)
    w = 6            # infecundable period (in months) after fetal loss

    rho = conception_probability()  #Probability of Conception

    rem = list()

    print("Fetal Moratlity Percet : ", alpha * 100, "%")
    print("Period of time: ", y, "Years")
    temp = (1 - alpha)
    ans = 0
    maxv = findv(t, 1, m, w)
    for v in range(maxv + 1):
        r = 1
        # print("========", v)
        temp2 = alpha ** v
        # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
        temp1 = comb(r + v - 1, v)
        ndash = find_ndash(t, r, m, v, w)
        temp3 = (1 - binom.cdf(r + v - 1, ndash, rho))
        ans += (temp1 * temp2 * temp3)
        # print("=======", ans)
    ans *= temp
    ans = (1 - ans)

    rem.append(ans)
    for r in range(1, y - 1):
        temp = (1 - alpha) ** r
        ans = 0
        maxv = findv(t, r, m, w)
        for v in range(maxv + 1):
            # print("========", v)
            temp2 = alpha ** v
            # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
            temp1 = comb(r + v - 1, v)
            ndash = find_ndash(t, r, m, v, w)
            temp3 = (1 - binom.cdf(r + v - 1, ndash, rho))
            ans += (temp1 * temp2 * temp3)
            # print("=======", ans)
        ans *= temp
        print(f"Probability of atleast {r} birth/births : {ans}")
        rem.append(ans)

    plt.plot(rem, color='black')
    plt.title(f"{y} years and {alpha * 100}% Mortality")
    plt.xlabel('r - births')
    plt.plot(rem, 'ro')
    plt.grid()
    plt.ylabel('Probability of atleast r-birth')
    plt.xticks(np.arange(0, y - 1 , 1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.show()
