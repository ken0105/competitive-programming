import re


def main():
    x = input()
    ans = re.sub(r'\..+',"",x)
    print(ans)

if __name__ == '__main__':
    main()
