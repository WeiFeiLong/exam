w = input().split(' ')
n = int(w[0])  # 礼物个数
m = int(w[1])  # 需要购买数
k = int(w[2])  # 颜值
s = input().split(' ')
b = []
ans = 0  # 方案个数
for x in range(n):
    a = int(s[x])
    b.append(a)  # 礼物数组
# print(b)

ad = []

for x in range(n - m + 1):  # 指针
    h = 0
    a = b[x:x + m]  # m每次取的数组
    # print(a)
    for x in range(m):  # 循环每个小数组
        if a[x] >= k:  # 满足
            h = h + 1
    # print(h)
    if h == m:
        ans += 1
print(ans)
