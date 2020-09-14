n = int(input())
b = []
for x in range(n):
    a = input()
    a = [int(x) for x in a]
    b.append(a)
c = b  # 复制一个二维矩阵
# print(b, c)

for x in range(n):
    x += 1
    for y in range(n):
        y += 1
        try:
            if b[x][y] == 0 and b[x - 1][y] == 1 and b[x][y - 1] == 1 and b[x + 1][y] == 1 and b[x][y + 1] == 1:
                c[x][y] = 1
        except:
            pass
# print(c)

for x in range(n):
    a = ''
    for y in range(n):
        a = a + str(c[x][y])
    print(a)
