import math
t = 51
alpha = 0.1
rho = 0.01
p = (1-alpha)*rho
print(p)
m = 15
q = 1 - 0.01
ans = 0
temp = p**t
r = 1
w = 6
pi = alpha*rho

for v in range(0, 8):
    y = t - (1 - r)*m - v*w - 1
    temp1 = (math.factorial(v+r+y-1)*(pi**v)*(q**y))
    temp2 = math.factorial(r-1)*math.factorial(v)*math.factorial(y)
    ans += (temp1/temp2)
    # print(ans)

ans *= temp

print(ans)
