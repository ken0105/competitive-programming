if __name__ == '__main__':
    n = int(input())
    a1 = list(map(int,input().split()))
    a2 = list(map(int,input().split()))
    candies = 0
    for i in range(n):
        candies = max(candies,sum(a1[0:i+1]) + sum(a2[i:]))
    print(candies)