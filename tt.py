def merge(a,b, np):
    c = []
    shkvoren1 = 0
    shkvoren2 = 0
    while len(a) != shkvoren1 and len(b) != shkvoren2:
        if a[shkvoren1] <= b[shkvoren2]:
            c.append(a[shkvoren1])
            shkvoren1 += 1
        else:
            c.append(b[shkvoren2])
            shkvoren2 += 1
            np += 1
    if len(a) == shkvoren1:
        c += b[shkvoren2:]
    else:
        c += a[shkvoren1:]
    return c, np


def sorting(ms, np):
    if len(ms) <= 1:
        return ms, np
    else:
        middle = int(len(ms)/2)
        x = sorting(ms[:middle], np)
        a = x[0]
        np = x[1]
        x = sorting(ms[middle:], np)
        b = x[0]
        np = x[1]
        return merge(a, b, np)


n = int(input())

ms = list(map(int, input().split()))

ms = sorting(ms, 0)
m = 1
last = ms[0][0]

for i in ms[0]:
    if last != i:
        m +=1
        last = i

print(m)
