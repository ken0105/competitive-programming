itr_max, min, max = map(int, input().split())

ac_sum = 0
count = 0

for i in range(itr_max + 1):
    str_num = str(i)
    length = len(str_num)
    sum = 0
    for j in range(length):
        sum += int(str_num[j])
    if min <= sum <= max:
        ac_sum += i

print(ac_sum)