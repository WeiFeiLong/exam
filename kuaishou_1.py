def get_sqrt(n):
    left = 0
    right = n
    for x in range(100):
        center = (left + right) / 2
        if center ** 2 > n:
            right = center
        if center ** 2 < n:
            left = center
    return center


import math

n = 9786650
a = math.sqrt(n)
b = get_sqrt(n)
print(abs(a - b), '\n', '%.2f' % b)