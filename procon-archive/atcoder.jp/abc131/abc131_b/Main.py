import itertools

if __name__ == '__main__':
    n,l = map(int,input().split())
    azi = []
    for i in range(1,n+1):
        azi.append(i+l-1)

    taberu = float('inf')
    for i in azi:
        taberu = min(i,abs(taberu))

    print(sum(azi) - taberu)