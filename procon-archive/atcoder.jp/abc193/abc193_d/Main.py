from operator import mul
from functools import reduce

def calc(score):
    d = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    ans = 0
    for i in range(5):
        d[score[i]] += 1
    for i in list(d.keys()):
        ans += int(i) * 10 ** d[i]
    return ans

def minus(card, s, t):
    for i in s:
        card[i] -= 1
    for i in t:
        card[i] -= 1
    return card

def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    k = int(input())
    card = {"1":k, "2":k, "3":k, "4":k, "5":k, "6":k, "7":k, "8":k, "9":k}
    s = input()
    t = input()
    s = s[0:-1]
    t = t[0:-1]
    card = minus(card, s, t)
    ope = []
    total = (k * 9 - 8) * (k * 9 - 9)
    kakuritu = 0
    for i in range(1,10):
        for j in range(1,10):
            if card[str(i)] == 0 or card[str(j)] == 0:
                continue
            s += str(i)
            t += str(j)
            if calc(s) > calc(t):
                if i != j:
                    kakuritu += card[str(i)] * card[str(j)]
                else:
                    kakuritu += card[str(i)] * (card[str(i)] - 1)
            s = s[0:-1]
            t = t[0:-1]
    print(kakuritu/total)

if __name__ == '__main__':
    main()

