# from funcs import *

import random

from matplotlib import pyplot as plt
import time


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


def qicksort(ms):

    global tempp_ms, msx
    msx = ms[:]
    tempp_ms = ms[:]

    qs(0, len(ms) - 1)
    print(ms)


def qs(beg, end):
    global ms, temp_ms

    shkvoren = ms[beg + choose_shkvoren(end - beg)]
    print(shkvoren)
    index_beg = beg
    index_end = end
    for i in ms[beg:end+1]:
        if i < shkvoren:
            temp_ms[index_beg] = i
            index_beg += 1
    for i in ms[end:beg:-1]+[ms[beg]]:
        if i > shkvoren:
            temp_ms[index_end] = i
            index_end -= 1

    ms = temp_ms
    ms[index_beg:index_end-1] = [shkvoren] * (index_end - index_beg - 1)



n_iter = 10
ns = [100, 150, 200, 350, 500, 750, 1000, 1500, 2000, 3500, 5000, 7500, 10000, 15000, 20000, 35000, 50000, 75000, 100000, 150000, 200000, 250000, 300000, 400000, 500000]
#ns = [150000, 200000, 250000, 300000, 400000, 500000]
max_x = 51
m = 10000
times = 100
mxs = []

for n in ns:



    minim = 100000
    min_x = 0
    timings = []
    xs = []

    for tx in range((max_x+1)//2):
        x = tx*2 + 1

        t0 = time.clock()

        for _ in range(times):
            ms = [random.randint(0, m) for _ in range(0, n)]
            quick_sort(ms, x)
        t = (time.clock() - t0)/times
        if t < minim:
            minim = t
            min_x = x
        print(str(round(100 * x / max_x)) + "%")
        print(x, t)
        timings.append(t)
    print(timings)
    print("###############")
    print(min_x)
    print("###############")
    mxs.append(min_x)

print(mxs)

plt.plot(ns, mxs)
plt.show()



