class Solution:
    def getHouses(self, t, xa):
        # write code here
        a = []
        b = []
        ans = 2  # 初始最少2种方案 左和右
        n_house = int(len(xa) / 2)  # 房子的个数
        for x in range(n_house):  # 计算每个房子的范围 0 1
            n_left = xa[2 * x] - xa[2 * x + 1] / 2
            n_right = xa[2 * x] + xa[2 * x + 1] / 2
            a.append(n_left)
            a.append(n_right)
            b.append(a)
            a = []

        # print(b)
        for x in range(n_house - 1):  # 循环房子间隔
            l_house = b[x][1]  # 左房子上边界
            h_house = b[x + 1][0]  # 右房子下边界
            if h_house - l_house == t:
                ans += 1
            elif h_house - l_house >= t:
                ans += 2
            else:
                ans = ans
        print(ans)
        return ans


Solution().getHouses(2, [-1, 4, 5, 2])