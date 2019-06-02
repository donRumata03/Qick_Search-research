import random


def choose_shkvoren(length):
    shkvoren = random.randint(0, length - 1)
    return shkvoren


def qicksort(ms):

    global tempp_ms, msx
    msx = ms[:]
    tempp_ms = ms[:]

    qs(0, len(ms) - 1)
    print(ms)


def qs(beg, end):
    global tempp_ms, msx
    temp_ms = tempp_ms
    ms = msx
    shkvoren = ms[beg + choose_shkvoren(end - beg)]
    print(shkvoren)
    index_beg = beg
    index_end = end
    for i in ms[beg:end]:
        if i < shkvoren:
            temp_ms[index_beg] = i
            index_beg += 1
        elif i > shkvoren:
            temp_ms[index_end] = i
            index_end -= 1

    ms = temp_ms
    ms[index_beg:index_end-1] = [shkvoren] * (index_end - index_beg + 1)
