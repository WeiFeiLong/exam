def get_next(list_people, begin, out_num):  # 个人编号数组list_people，开始报begin, 报out_num出局
    s1 = [x for x in range(1, out_num + 1)]  # 基础
    s = []  # 增加后的
    while len(s) < len(list_people):
        s += s1
    s = s * 2  # 增加的[1，2，...,out_num]
    s = s[s.index(begin):]

    for i in range(len(list_people)):  # 0,1,2,3,4,5
        if s[i] == out_num:
            list_people.insert(i, 0)
            list_people.pop(i + 1)
        p = s[i]  # 数数标志

    list_s = []
    for x in range(len(list_people)):
        if list_people[x] != 0:
            list_s.append(list_people[x])  # 将上面数组中的0去掉
    if p == out_num:  # 归零
        p = 0
    print('遇到3变0:', list_people)
    print('下个起始位：', p + 1)
    return list_people, list_s, p + 1


def get_lastnum(n, out_num):  # n个人，报out_num出局，n>=out_num
    a = get_next([x for x in range(1, n + 1)], 1, out_num)
    while len(a[1]) != 1:
        a = get_next(a[1], a[2], out_num)
    return a


for x in range(2, 100):  # 测试从2到99个人时，留下人的情况
    b = get_lastnum(x, 3)
    print('%d个人时，最终留下的是%d号' % (x, b[1][0]), '\n')
