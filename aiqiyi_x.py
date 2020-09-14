from collections import Counter

s = input().split(' ')
# s = 3, 2, 3
n = len(s)  # 长度
k = n / 2  # 出现次数
a = []
for x in range(n):
    a.append(int(s[x]))

b = list(set(a))
c = Counter(a).most_common()
for x in range(len(b)):
    a = c[x]
    if a[1] > k:
        print(a[0])
        break
