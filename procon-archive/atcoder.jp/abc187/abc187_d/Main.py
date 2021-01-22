# from itertools import combinations
# import re
if __name__ == '__main__':
    n = int(input())
    li = []
    all_botes = 0
    t_botes = 0
    for i in range(n):
        a,t = map(int,input().split())
        li.append([a+t+a,a,t])
        all_botes += a
    li.sort()
    # print(all_botes)
    # print(li)
    ans = 0
    while all_botes // 2 >= t_botes:
        at,a,t = li.pop()
        all_botes += t
        t_botes += (a+t)
        ans +=1
    print(ans)