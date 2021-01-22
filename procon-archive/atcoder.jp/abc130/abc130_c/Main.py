import math

if __name__ == '__main__':
    W,H,x,y = map(int,input().split())
    square = W * H
    ans = square / 2
    if W /2 == x and H /2 == y:
        print(ans,1)
    else:
        print(ans,0)
