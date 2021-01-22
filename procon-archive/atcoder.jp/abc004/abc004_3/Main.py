# import itertools
# import math

# if __name__ == '__main__':
n = int(input())
l = ["1", "2", "3", "4", "5", "6"]
amari = n % 30
for i in range(amari):
    tmp = l[i % 5]
    tmp2 = l[i % 5 + 1]
    l[i % 5] = tmp2
    l[i % 5 + 1] = tmp
ans = ""
for i in l:
    ans += i
print(ans)
