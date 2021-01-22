from collections import Counter

if __name__ == '__main__':
    a,b = map(int,input().split())
    print(max(0,a-2*b))