from math import floor
if __name__ == '__main__':
    def __calc(a,b,x):
        return floor(a*x/b) - a * floor(x/b)

    a,b,n = map(int,input().split())
    if n >= b:
        print(__calc(a,b,b-1))
    else:
        print(__calc(a,b,n))