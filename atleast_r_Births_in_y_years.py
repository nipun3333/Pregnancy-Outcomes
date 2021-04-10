from scipy.stats import binom
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np


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
    y = 10   # Number of years taken in consideration
    m = 15   # infecundable period (in months) after L conception
    t = y*12 - 9   # number of months - calculated from years(y)
    w = 6   # infecundable period (in months) after fetal loss
    rho = 0.01  # probability of conception (assuming contraceptive is used)
    alpha = 0.25  # aplha = mortality (probability that a given conception will end in fetal loss)
    rem = list()


    print("Fetal Moratlity Percet : ", alpha*100, "%")
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
        temp3 = (1 - binom.cdf(r+v-1, ndash, rho))
        ans += (temp1*temp2*temp3)
        # print("=======", ans)
    ans *= temp
    ans = (1 - ans)
    print(f"Probability of 0 birth : {ans}")
    # rem.append(ans)
    rem.append(1)
    for r in range(1, y//2 + 1):
        temp = (1-alpha)**r
        ans = 0
        maxv = findv(t, r, m, w)
        for v in range(maxv + 1):
            # print("========", v)
            temp2 = alpha**v
            # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
            temp1 = comb(r+v-1, v)
            ndash = find_ndash(t, r, m, v, w)
            temp3 = (1 - binom.cdf(r+v-1, ndash, rho))
            ans += (temp1*temp2*temp3)
            # print("=======", ans)
        ans *= temp
        print(f"Probability of atleast {r} birth/births : {ans}")
        rem.append(ans)

    # print(sum(rem)-rem[0])
    plt.plot(rem, color='black')
    plt.title(f"Atleast r-birth in {y} years\n{alpha*100}% Mortality")
    plt.xlabel('r - births')
    plt.ylabel('Probability of atleast r-birth')
    plt.plot(rem, 'ro')
    plt.grid()
    plt.xticks(np.arange(0, y//2 + 1, 1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.show()
