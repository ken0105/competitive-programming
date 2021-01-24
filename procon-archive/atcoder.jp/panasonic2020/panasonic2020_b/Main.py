import math

if __name__ == '__main__':
    h, w = map(int,input().split())
    if h == 1 or w == 1:
        print(1)
        exit()
    print(math.ceil(h*w/2))