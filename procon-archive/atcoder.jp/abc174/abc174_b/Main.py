import math

i, distance = map(int, input().split())
count = 0
for _ in range(i):
    x, y = map(int, input().split())
    if math.sqrt(x * x + y * y) <= distance:
        count += 1
print(count)
