quantity = int(input())
li = list(map(int, input().split()))

count = 0

while all(a % 2 == 0 for a in li):
        li = [a/2 for a in li]
        count += 1
print(count)