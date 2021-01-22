from bisect import bisect, bisect_right, bisect_left

if __name__ == "__main__":
    n = int(input())
    ab = []
    for i in range(n):
        a,b = map(int,input().split())
        ab.append((b,a))
    ab.sort()
    time = 0
    for b,a in ab:
        time += a
        if time > b:
            print("No")
            exit()
    print("Yes")
