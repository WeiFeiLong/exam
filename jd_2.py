np = list(map(int, input().split()))
n = np[0]  # 组
p = np[1]  # 价格上限
ku = []
for x in range(n):
    s_1 = list(map(int, input().split()))
    a = [s_1[2] / s_1[1]]  # 单位价格的魅力值
    s_1 = a + s_1  # 拼接在原数组前面
    ku.append(s_1)  # n*4唯数组

# n = 3
# p = 10
# ku = [[1.5, 2, 2, 3], [2.0, 1, 5, 10], [3.0, 2, 4, 12]]
pai = sorted(ku)[::-1]  # 单位价格的魅力值高的在前
# print(pai)

price_all = 0
sort_all = 0
for x in range(n):
    price = pai[x][1] * pai[x][2]
    price_all = price_all + price
    sort = pai[x][1] * pai[x][3]
    sort_all = sort_all + sort

if price_all <= p:  # 钱够多
    print(sort_all)

price_all = 0
sort_all = 0
for x in range(n):  # 循环n组装备
    for y in range(pai[x][1]):  # 循环每组装备的个数
        if price_all > p:  # 超过了p,撤回一步
            price_all = price_all - price_i
            sort_all = sort_all - sort_i
            break
        else:
            price_i = pai[x][2]
            price_all = price_i + price_all
            sort_i = pai[x][3]
            sort_all = sort_i + sort_all

print(sort_all, price_all)

for x in range(n):
    if (p - price_all) % pai[x][2] == 0:  # 找到取整
        sort_w = pai[x][3] * (p - price_all) / pai[x][2]
        sort_all = sort_all + sort_w

print(int(sort_all))
