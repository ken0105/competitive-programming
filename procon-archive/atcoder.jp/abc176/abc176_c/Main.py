n = int(input())

li = list(map(int, input().split()))
sum_diff = 0

for i in range(len(li)):
    if i > 0:
        diff = li[i] - li[i - 1]
        if li[i] - li[i - 1] < 0:
            li[i] = li[i] + abs(diff)
            sum_diff += abs(diff)
print(sum_diff)
