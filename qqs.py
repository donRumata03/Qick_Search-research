ms = list(map(int, input().split()))

n = len(ms)
buckets = [[] for i in range(n)]

for i in ms:
    buckets[int(i * n)].append(i)
