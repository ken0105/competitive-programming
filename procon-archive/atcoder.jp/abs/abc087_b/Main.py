count = 0
a, b, c = [int(input()) for i in range(3)]
Sum = int(input())

for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if 500 * i + 100 * j + 50 * k == Sum:
                count += 1
print(count)