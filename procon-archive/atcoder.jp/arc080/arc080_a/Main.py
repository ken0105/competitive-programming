if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))

    multiple4 = 0
    multiple2 = 0
    other = 0
    for num in a:
        if num % 4 == 0:
            multiple4 += 1
        elif num % 2 == 0:
            multiple2 += 1
        else:
            other += 1

    if (other <= multiple4 + 1 and multiple2 % 2 == 0) or (other + multiple2 <= multiple4 + 1) or\
            (multiple2 > 2 and other == 0) or (other == multiple4 and multiple2 % 2 == 1):
        print("Yes")
    else:
        print("No")


