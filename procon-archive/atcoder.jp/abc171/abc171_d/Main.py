from collections import Counter
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    ac = Counter(a)
    s = 0
    for k in ac:
        s += k * ac[k]
    q = int(input())
    for i in range(q):
        b,c = map(int,input().split())
        s = s + (c-b) *  int(ac.get(b) or 0)
        ac[c] += int(ac.get(b) or 0)
        ac[b] = 0
        print(s)
