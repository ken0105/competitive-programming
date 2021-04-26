n = int(input())
li = [int(input()) for i in range(1, n + 1)]

li.sort()
num_previous = 0
count = 0
for i in li:
    if i == num_previous:
        pass
    else:
        count += 1
        num_previous = i

print(count)
