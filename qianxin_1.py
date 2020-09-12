class Solution:
    def maxCandies(self, candies, coin, n):
        # print(candies)
        len_c = len(candies)
        num = 0
        w = []
        for x in range(len_c):
            if coin[x] == 0:
                num = num + candies[x]  # 计算本应该拿多少
            else:
                w.append(candies[x])  # 计算另外个人的糖果数组
        # print(num, w)

        if n % 2 == 1:
            n_1 = int((n + 1) / 2)
        else:
            n_1 = int(n / 2)  # 输出n_1表示可以取另外个人的多少包糖果
        # print(n_1)

        len_w = len(w)
        if len_w <= n_1:  # 如果可取的包数大于另一个人的，都取了
            max_w = sum(w)
        else:
            for x in range(len_w - n_1 + 1):
                # print(x)
                max_w = max(sum(w[:n_1]), sum(w[x:x + n_1]))  # 找出可取的最大连续包的糖果
                # print(max_w)

        num_max = num + max_w
        print(num_max)
        return num_max


Solution().maxCandies([3, 5, 7, 2, 8, 8, 15, 3], [1, 0, 1, 0, 1, 0, 1, 0], 3)
