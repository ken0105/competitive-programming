from itertools import combinations
if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(n):
        x,y = map(int,input().split())
        li.append((x,y))
    ans = 0
    for i in combinations(li,2):
        k = (i[1][1] - i[0][1]) / (i[1][0] - i[0][0])
        if abs(k) <= 1:
            ans += 1
    print(ans)