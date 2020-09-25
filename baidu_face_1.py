def FindMaxLen(str1, str2):
    import re
    str1 = str1.lower()
    str2 = str2.lower()
    a = re.findall(str2, str1)
    if len(a) > 0:
        return a[0]

    for x in range(len(str2)):
        s = str2[:-x - 1]
        b = re.findall(s, str1)
        if len(b) > 0:
            return b[0]


w = FindMaxLen('abcdefg', 'abcdefD')
print(w)