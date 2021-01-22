from itertools import product
if __name__ == '__main__':
    n = int(input())
    s = input()
    R = []
    G = []
    B = []
    for i in range(len(s)):
        if s[i] == "R":
            R.append(i)
        elif s[i] == "G":
            G.append(i)
        else:
            B.append(i)

    B = set(B)
    ans = 0
    p = product(R,G)
    for i,j in p:
        ans += len(B)
        if j + (j-i) in B:
            ans -= 1
        if (i+j)/2 in B:
            ans -= 1
        if i - (j-i) in B:
            ans -= 1
    print(ans)
