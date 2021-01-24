import math

if __name__ == '__main__':
    a,b = input().split()
    num = int(a + b)
    for i in range(1,1000):
        if num == i ** 2:
            print("Yes")
            exit()
    print("No")