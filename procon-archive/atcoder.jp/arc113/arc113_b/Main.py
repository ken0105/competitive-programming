def main():
    a,b,c, = map(int,input().split())
    a %= 10
    loop = 2
    cycle_list = [a]
    while a != pow(a, loop, 10):
        cycle_list.append(pow(a,loop,10))
        loop += 1
    cycle = loop - 1
    if cycle == 0:
        print(a)
        exit()
    ans = pow(b, c, cycle)
    print(cycle_list[ans-1])




if __name__ == '__main__':
    main()