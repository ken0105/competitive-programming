from bisect import bisect_left

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = []
    ans = 0
    for i in a:
        index = bisect_left(l, i)
        if index == len(l):
            l.append(i)
            ans += len(l)
        else:
            ans += 1
            l = [i]
    print(ans)

if __name__ == '__main__':
    main()
