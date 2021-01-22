if __name__ == '__main__':
    a,b = map(str,input().split())
    sum_a = 0
    sum_b = 0
    for i in a:
        sum_a += int(i)
    for i in b:
        sum_b += int(i)
    if sum_a >= sum_b:
        print(sum_a)
        exit()
    else:
        print(sum_b)