def main():
    n = int(input())
    total = 0
    ab_list = [map(int,input().split()) for _ in range(n)]
    ab_list.reverse()
    for a, b in ab_list:
        if (a + total) % b != 0:
            total += b - (a + total) % b
    print(total)

if __name__ == '__main__':
    main()