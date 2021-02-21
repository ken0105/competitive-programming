def main():
    s = list(input())
    for i,c in enumerate(s):
        if i % 2 == 1:
            if c.islower():
                print("No")
                exit()
        if i % 2 == 0:
            if c.isupper():
                print("No")
                exit()
    print("Yes")


if __name__ == '__main__':
    main()