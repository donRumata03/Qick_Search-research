def right_bs(ms, num):
    if num > ms[-1]:
        return None
    if num < ms[0]:
        return None
    low = -1
    high = len(ms) # LOL
    while high - low > 1:
        mid = (low + high) // 2
        if ms[mid] > num:
            high = mid
        else:
            low = mid
    if ms[low] != num and ms[high] != num:
        return None
    return high


def left_bs(ms, num):
    if num > ms[-1]:
        return None
    if num < ms[0]:
        return None
    low = -1
    high = len(ms) # LOL
    while high - low > 1:
        mid = (low + high) // 2
        if ms[mid] >= num:
            high = mid
        else:
            low = mid
    if ms[low] != num and ms[high] != num:
        return None
    return high


N, M = map(int, input().split())
ms = list(map(int, input().split()))
mx = list(map(int, input().split()))


for i in mx:
    x = right_bs(ms, i)
    y = left_bs(ms, i)
    if x is None or y is None:
        print(0)
    else:
        print(y + 1, x)