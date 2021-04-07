from numpy import random
from scipy.stats import binom
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np


def findv(t, r, m, w):
    return (t-1-(r-1)*m)//w


# def find_lamda():
#     return random.randint(4, 9)


# def find_theta():
#     return random.randint(25, 33)


# def find_i(max_n):
#     return random.randint(0, max_n+1)


def find_ndash(t, r, m, v, w):
    return t - (r-1)*(m-1) - v*(w-1)


def find_rho(n):
    # theta = find_theta()
    # lamda = find_lamda()
    theta = 28
    lamda = 6
    # i = find_i(n)
    i = n*(int(theta/lamda))
    ans = comb(n, i)
    ans *= ((lamda/theta)**n)
    ans *= ((theta/lamda - 1)**(n-i))
    ans *= (30/theta)
    return ans


if __name__ == '__main__':
    m = 15
    y = 15
    t = y*12 - 9
    w = 6
    alpha = 0.25
    rem = list()
    # min_row = 10
    # max_row = -1
    # Innovation
    max_cotial_acts = 2
    rho = find_rho(max_cotial_acts)

    print("Fetal Moratlity Percent : ", alpha*100, "%")
    print("Period of time: ", y, "Years")
    temp = (1-alpha)
    ans = 0
    maxv = findv(t, 1, m, w)
    for v in range(maxv + 1):
        r = 1
        # print("========", v)
        temp2 = alpha**v
        # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
        temp1 = comb(r+v-1, v)
        ndash = find_ndash(t, r, m, v, w)
        # rho = find_rho(max_cotial_acts)
        # min_row = min(rho, min_row)
        # max_row = max(rho, max_row)
        temp3 = (1 - binom.cdf(r+v-1, ndash, rho))
        ans += (temp1*temp2*temp3)
        # print("=======", ans)
    ans *= temp
    ans = (1 - ans)
    print(f"Probability of 0 birth : {ans}")
    # rem.append(ans)
    rem.append(1)
    for r in range(1, 11):
        temp = (1-alpha)**r
        ans = 0
        maxv = findv(t, r, m, w)
        for v in range(maxv + 1):
            # print("========", v)
            temp2 = alpha**v
            # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
            temp1 = comb(r+v-1, v)
            ndash = find_ndash(t, r, m, v, w)
            # rho = find_rho(max_cotial_acts)
            # min_row = min(rho, min_row)
            # max_row = max(rho, max_row)
            temp3 = (1 - binom.cdf(r+v-1, ndash, rho))
            ans += (temp1*temp2*temp3)
            # print("=======", ans)
        ans *= temp
        print(f"Probability of atleast {r} birth/births : {ans}")
        rem.append(ans)
        # print(min_row, max_row)
        print(rho)

    plt.plot(rem)
    plt.title(f"Atleast r-birth in {y} years\n{alpha*100}% Mortality")
    plt.xlabel('r - births')
    plt.ylabel('Probability of atleast r-birth')
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.show()
