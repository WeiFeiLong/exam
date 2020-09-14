from functools import reduce
mn = input().split(' ')
m = int(mn[0])
n = int(mn[1])
S = input().split(' ')
s = []

for x in range(n):
    s.append(int(S[x]))
sor = sorted(s)
num = 0
add = 0
sum_s = int(reduce(lambda x, y: x + y, sor))
if sor[0] > m:
    print(0)
elif sum_s <= m:
    print(n)
else:
    for x in sor:
        # print(x)
        num = num + x
        add += 1
        if num > m:
            print(add-1)
            break