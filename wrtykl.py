def bs(lst, num):
    low = 0
    high = len(lst)
    while high - low > 1:
        mid = (low + high) // 2
        if lst[mid] > num:
            high = mid
        else:
            low = mid
    return lst[low], lst[high]


n, k = map(int, input().split())

ms = list(map(int, input().split()))

mx = list(map(int, input().split()))


for i in mx:
    print(bs(ms, i))