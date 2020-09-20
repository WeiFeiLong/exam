n = int(input())
d = []
for x in range(n):
    s = input()
    d.append(s)
# print(d)
# d=['ABCABDABDABEABEABF', 'ABCABDAEC']

for x in d:
    b = []
    f = []
    if len(x) % 3 == 0:
        len_x = int(len(x) / 3)
        for y in range(len_x):
            a = x[y * 3:y * 3 + 3]
            b.append(a)
        # print(b)
        for x in range(len_x - 1):
            flag = 0
            b_x = [b_i for b_i in b[x]]
            b_x1 = [b_i1 for b_i1 in b[x + 1]]
            for i in b_x:
                if i in b_x1:
                    b_x1.pop(b_x1.index(i))
                    flag += 1
            # print(flag)
            f.append(flag)
        f.sort()
        # print(f)
        if f[0] >= 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
