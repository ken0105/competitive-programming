def main():
    n = input()
    for i in range(20):
        length = len(n)
        if length % 2 == 1 and n[0:length//2] == n[length//2+1:][::-1]:
            print("Yes")
            exit()
        elif length % 2 == 0 and n[0:length//2] == n[length//2:][::-1]:
            print("Yes")
            exit()
        n = "0" + n
    print("No")


if __name__ == '__main__':
    main()
