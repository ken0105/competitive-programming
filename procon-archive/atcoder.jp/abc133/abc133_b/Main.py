import itertools
import math

if __name__ == '__main__':
    n,d = map(int,input().split())
    x = []
    for i in range(n):
        x.append(list(map(int,input().split())))

    ans = 0
    for i in itertools.combinations(x,2):
        d = 0
        for j in range(len(i[0])):
            d += (i[0][j] - i[1][j]) ** 2
        is_int = math.sqrt(d).is_integer()
        if is_int:
            ans += 1
    print(ans)