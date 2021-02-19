import math


def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_min =  min(min(min(min(a,b),c),d),e)
    print(5 + math.ceil((n - min_min) / min_min))

if __name__ == '__main__':
    main()