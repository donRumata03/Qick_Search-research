st = "abcdefghijklmnopqrstuvwxyz"

dic = {}
main_ms = []

for i in range(len(st)):
    x = str(st[i])
    dic[x] = i
    main_ms.append(0)

msc = main_ms[:]


def getkey(i):
    return dic[i]


st1 = list(input())
st2 = list(input())

if len(st1) != len(st2):
    print("NO")
    exit(0)

for i in st1:
    main_ms[dic[i]]+=1

for i in st2:
    msc[dic[i]] += 1

flag = True

for i in range(len(msc)):
    if msc[i] != main_ms[i]:
        flag = False
        break

print("YES") if flag else print("NO")

