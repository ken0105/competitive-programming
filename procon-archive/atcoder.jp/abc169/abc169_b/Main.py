import math

if __name__ == "__main__":
    n = int(input())
    li = list(map(int,input().split()))
    sum = 1
    if 0 in li:
        print(0)
        exit()
    for i in li:
        sum *= i
        if sum > 10 ** 18:
            print(-1)
            exit()
    print(sum)