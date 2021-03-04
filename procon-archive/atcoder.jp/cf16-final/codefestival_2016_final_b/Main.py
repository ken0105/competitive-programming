def main():
    n = int(input())
    rem = n
    for i in range(n,0,-1):
        if rem > (i - 1) * i // 2:
            print(i)
            rem -= i

if __name__ == '__main__':
    main()
