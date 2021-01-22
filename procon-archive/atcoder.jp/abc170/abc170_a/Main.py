import math

if __name__ == "__main__":
    n = list(map(int,input().split()))
    for i in range(len(n)):
        if n[i] == 0:
            print(i + 1)
            exit()
