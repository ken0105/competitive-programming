from collections import deque, Counter

if __name__ == '__main__':
    n = int(input())
    d = list(map(int,input().split()))
    m = int(input())
    t = list(map(int,input().split()))
    cnt_d = Counter(d)
    for score in t:
        num = cnt_d.get(score)
        if num is None or num <= 0:
            print("NO")
            exit()
        else:
            cnt_d[score] = cnt_d.get(score) - 1
    print("YES")