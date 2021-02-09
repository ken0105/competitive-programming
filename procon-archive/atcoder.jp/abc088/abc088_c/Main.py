from collections import Counter

if __name__ == '__main__':
    c1 = list(map(int,input().split()))
    c2  = list(map(int,input().split()))
    c3 = list(map(int,input().split()))

    diff = abs(c1[0] - c2[0])
    for a,b in zip(c1,c2):
        if diff != abs(a-b):
            print("No")
            exit()

    diff = abs(c2[0] - c3[0])
    for a, b in zip(c2, c3):
        if diff != abs(a - b):
            print("No")
            exit()
    print("Yes")

