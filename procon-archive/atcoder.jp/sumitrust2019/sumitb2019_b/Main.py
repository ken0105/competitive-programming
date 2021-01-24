import math

if __name__ == '__main__':
    n = int(input())
    for i in range(1,50001):
        if n == math.floor(i * 1.08):
            print(i)
            exit()
    print(":(")
