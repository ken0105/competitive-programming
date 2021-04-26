i = int(input())
count_prev = 0
x_prev = 0
y_prev = 0
for _ in range(i):
    count, x, y = map(int, input().split())
    if count < x + y or count % 2 != (x + y) % 2 or count - count_prev < abs(x - x_prev) + abs(y - y_prev):
        print("No")
        quit()
    else:
        count_prev = count
        x_prev = x
        y_prev = y

print('Yes')


