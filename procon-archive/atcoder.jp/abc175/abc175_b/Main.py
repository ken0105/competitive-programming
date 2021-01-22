import itertools

n = int(input())

li = list(map(int,input().split()))

li = list(itertools.combinations(li, 3))

count = 0

for i in li:
    amari = sum(i) - max(i)
    if amari > max(i):
        if len(set(i)) == 3:
            count += 1

print(count)


