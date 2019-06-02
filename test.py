import numpy as np
import time
import random
from matplotlib import pyplot as plt


def choose_shkvoren(ms, x):
    shkvorens = []
    for i in range(x):
        shkvorens.append(ms[random.randint(0, len(ms) - 1)])
    shkvorens.sort()
    return shkvorens[int(x/2 - 0.5)]


def quick_sort(nums, x):
    if len(nums) <= 1:
        return nums
    q = choose_shkvoren(nums, x)

    s_nums = []
    m_nums = []
    e_nums = []
    for n in nums:
        if n < q:
            s_nums.append(n)
        elif n > q:
            m_nums.append(n)
        else:
            e_nums.append(n)

    return quick_sort(s_nums, x) + e_nums + quick_sort(m_nums, x)


m = 1000
n = 100000
mxs = 15
times = 2000
ts = []
xs = []
for tx in range((mxs + 1) // 2):
    x = tx * 2 + 1
    xs.append(x)
    c = 0
    for i in range(100):
        ms = [random.randint(0, m) for _ in range(0, n)]
        t0 = time.clock()
        quick_sort(ms, x)
        t = time.clock() - t0
        c+= t
    ts.append(c/100)
    print(c/100)

plt.plot(np.array(xs), np.array(ts))
