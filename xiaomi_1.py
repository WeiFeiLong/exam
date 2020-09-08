import re

str_in = input().split(' ')
ans = []

for x in str_in:

    num = re.findall(r'[0-9]', x)   # 找出所有的数字
    a = re.findall(r'[a-z]', x)     # 找出所有的小写
    A = re.findall(r'[A-Z]', x)     # 找出所有的大写
    str_not = re.sub(r'\w', '', x)  # 找出所有的字符

    if len(x) < 8 or len(x) > 120:  # 字符长度不符合规则
        ans.append(1)
    elif len(num) > 0 and len(a) > 0 and len(A) > 0 and len(str_not) > 0:  # 包含四种格式
        ans.append(0)
    else:   # 没有包含4种
        ans.append(2)
for x in ans:
    print(x)