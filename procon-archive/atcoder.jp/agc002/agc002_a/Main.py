import math

if __name__ == '__main__':
    a,b = map(int,input().split())
    if a <= 0 <= b:
        print("Zero")
        exit()
    if 0 < a < b:
        print("Positive")
        exit()

    nums = abs(a-b) + 1
    if nums % 2 == 1:
        print("Negative")
    else:
        print("Positive")