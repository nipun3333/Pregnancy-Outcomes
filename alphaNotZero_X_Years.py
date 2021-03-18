from scipy.stats import binom
from scipy.special import comb


def findv(t, r, m, w):
    if r == 0:
        return (t-1)//w
    return (t-1-(r-1)*m)//w


def find_ndash(t, r, m, v, w):
    if r == 0:
        return t - v*(w-1)
    return t - (r-1)*(m-1) - v*(w-1)


if __name__ == '__main__':
    m = 15
    y = 15
    t = y*12 - 9
    w = 6
    rho = 0.01
    alpha = 0.1

    print("Fetal Moratlity Percet : ", alpha*100, "%")
    print("Period of time: ", y, "Years")
    for r in range(6):
        temp = (1-alpha)**r
        ans = 0
        maxv = findv(t, r, m, w)
        for v in range(maxv + 1):
            # print("========", v)
            temp2 = alpha**v
            # temp1 = comb(r+v-1, v) Does not work when r == 0 and thus drives answer to zero
            if r == 0:
                temp1 = 1
            else:
                temp1 = comb(r+v-1, v)
            ndash = find_ndash(t, r, m, v, w)
            temp3 = (1 - binom.cdf(r+v-1, ndash, rho))
            ans += (temp1*temp2*temp3)
            # print("=======", ans)
        ans *= temp
        print(f"Probability of atleast {r} birth/births : {ans}")
