def gettwo(s):
    a = {}
    b = []
    for x in range(len(s)):
        if a.__contains__(s[x:x + 2]):
            a[s[x:x + 2]] += 1
        else:
            a[s[x:x + 2]] = 1
    a = sorted(a.items(), key=lambda x: x[1])[::-1]

    for x in range(len(a)):
        if a[x][1] == a[0][1]:
            b.append(a[x][0])
    return b


s = 'qewqewrdsafdsfdsgrfgdgfdcx'
print(gettwo(s))