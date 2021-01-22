import math

if __name__ == "__main__":
    x,y = map(int,input().split())

    if y % 2 != 0:
        print("No")
        exit()
    if y / 2 - x <0:
        print("No")
        exit()
    if y /2 -x > x :
        print("No")
        exit()
    print("Yes")