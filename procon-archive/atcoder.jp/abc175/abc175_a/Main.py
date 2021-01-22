rs = list(input())


s_count = rs.count('S')
ans = 0

if s_count == 1:
    if rs[1] == 'S':
        ans = 1
    else:
        ans = 2
elif s_count == 2:
    ans = 1
elif s_count == 0:
    ans = 3
else:
    ans = 0
print(ans)

