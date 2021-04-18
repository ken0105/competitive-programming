from operator import itemgetter


def main():
    n = int(input())
    li = []
    for _ in range(n):
        x,l = map(int, input().split())
        li.append((x-l,x+l))
    li = sorted(li, key=itemgetter(1))
    s_b,t_b = li[0]
    ans = n
    for s,t in li[1:]:
        if t_b > s:
            ans -= 1
        else:
            s_b = s
            t_b = t
    print(ans)

if __name__ == '__main__':
    main()
