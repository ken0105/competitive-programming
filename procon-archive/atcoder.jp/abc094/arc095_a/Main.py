def main():
    n = int(input())
    x = list(map(int,input().split()))
    middles = dict()
    seen = set()
    x_s = sorted(x)
    point = n // 2 -1
    for i,num in enumerate(x_s):
        if num in seen:
            continue
        seen.add(num)
        if x_s[point] < num:
            middles[num] = x_s[point]
        elif x_s[point] > num:
            middles[num] = x_s[point + 1]
        else:
            middles[num] = x_s[point + 1]


    for i in x:
        print(middles[i])

if __name__ == '__main__':
    main()