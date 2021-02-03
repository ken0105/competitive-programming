if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    odds = 1
    for num in a:
        if num % 2 == 1:
            odds *= 1
        else:
            odds *= 2
    print(pow(3,len(a))- odds)