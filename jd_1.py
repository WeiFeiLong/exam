mn = list(map(int, input().split()))
n = mn[0]  # cm
m = mn[1] * 100  # cm
# n = 60
# m = 100

def pa(a, w):  # 每天爬ncm, 第a天时爬多少cm
    a_day = 0
    for x in range(a):
        one_day = 0.5 ** (x + 1) * w
        a_day += one_day
    # print(a_day)
    return a_day


last_len = m  # 初始剩下的长度
day_i = 0  # 初始天数

while last_len > n:  # 100>60,70>60,55<60
    day_i += 1
    a = pa(day_i, n)
    # print(a)
    last_len = m - a

print(day_i + 1)