import math

if __name__ == '__main__':
    x,y = map(int,input().split())
    l = [x]
    while l[-1] * 2 <= y:
        l.append(l[-1] * 2)
    print(len(l))