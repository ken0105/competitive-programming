import math


def main():
    r,x,y = map(int, input().split())
    total = math.sqrt(x ** 2 + y ** 2)
    if total < r:
        print(2)
    else:
        print(math.ceil(total / r))

if __name__ == '__main__':
    main()
