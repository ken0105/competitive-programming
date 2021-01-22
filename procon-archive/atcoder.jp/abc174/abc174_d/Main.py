N = int(input())

li = list(input())

r_count = li.count('R')

ideal_li = list('W' for _ in range(len(li)))

for i in range(r_count):
    ideal_li[i] = 'R'

unmatch_count = 0
for i in range(len(li)):
    if li[i] != ideal_li[i]:
        unmatch_count += 1

print(unmatch_count // 2)
