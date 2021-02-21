from collections import Counter

def main():
    n = int(input())
    s = input()
    w = [0] * n
    e = [0] * n
    for i in range(n):
        if i == 0:
            if s[i] == "W":
                w[i] += 1
            else:
                e[i] += 1
            continue
        if s[i] == "W":
            w[i] = w[i-1] + 1
            e[i] = e[i-1]
        else:
            e[i] = e[i-1] + 1
            w[i] = w[i-1]
    ans = n
    for i in range(n):
        w_cnt = w[i-1]
        if i - 1 < 0:
            w_cnt = 0
        candidate = w_cnt + (e[n-1] - e[i])
        ans = min(ans, candidate)
    print(ans)




if __name__ == '__main__':
    main()
