N = int(input())


num, num2,num3 = 1, 1, 1

for _ in range(N):
    num = num * 10 % 1000000007
    num2 = num2 * 9 % 1000000007
    num3 = num3 * 8 % 1000000007
print((num - num2 * 2 + num3) % 1000000007)
