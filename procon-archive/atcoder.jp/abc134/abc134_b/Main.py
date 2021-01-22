import math

if __name__ == "__main__":
    n,d = map(int,input().split())
    print(math.ceil(n/(d*2+1)))