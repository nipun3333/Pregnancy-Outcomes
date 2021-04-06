from scipy.stats import binom
from scipy.special import comb
import matplotlib.pyplot as plt

# Assumptions Made which has to be Validated
# 1. Probability of Misscarriage/StillBirth  = 0.1
# 2. Non-susceptible period after Misscarriage or Still Birth  = 10


#Notations
# m = Infecundability to conception which leads to misscarriage/stillbirth
# w = Infecundability to conception which leads to Live Birth
# r = number of fetal loss



def findn(t, r, m, w):
    return (t-1-(r-1)*m)//w


def find_ndash(t, r, m, n, w):
    return t - (r-1)*(m-1) - n*(w-1)


if __name__ == '__main__':
    m = 10
    y = 10
    t = y*12 - 9
    w = 15
    rho = 0.01
    alpha = 0.1
    rem = list()


    print("Fetal Moratlity Percet : ", alpha*100, "%")
    print("Period of time: ", y, "Years")
    temp = alpha
    ans = 0
    maxn = findn(t, 1, m, w)
    for n in range(maxn + 1):
        r = 1
        # print("========", v)
        temp2 = (1-alpha) ** n
        # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
        temp1 = comb(r + n - 1, n)
        ndash = find_ndash(t, r, m, n, w)
        temp3 = (1 - binom.cdf(r + n - 1, ndash, rho))
        ans += (temp1*temp2*temp3)
        # print("=======", ans)
    ans *= temp
    ans = (1 - ans)
    print(f"Probability of 0 Stillbirth/Misscarriage : {ans}")
    rem.append(ans)
    for r in range(1, 6):
        temp = (alpha)**r
        ans = 0
        maxn = findn(t, r, m, w)
        for n in range(maxn + 1):
            # print("========", v)
            temp2 = (1-alpha) ** n
            # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
            temp1 = comb(r + n - 1, n)
            ndash = find_ndash(t, r, m, n, w)
            temp3 = (1 - binom.cdf(r + n - 1, ndash, rho))
            ans += (temp1*temp2*temp3)
            # print("=======", ans)
        ans *= temp
        print(f"Probability of atleast {r} Stillbirths/Misscarriages : {ans}")
        rem.append(ans)

    plt.plot(rem)
    plt.title(f"{y} years and {alpha*100}% Mortality")
    plt.xlabel('r - fetal-loss')
    plt.ylabel('Probability of atleast r-fetal-loss')
    plt.show()
