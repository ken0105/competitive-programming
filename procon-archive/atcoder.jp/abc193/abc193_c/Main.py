def main():
    n = int(input())
    ans = 0
    seen = set()
    for i in range(2,10**5+1):
        for j in range(2,50):
            candidate = i ** j
            if candidate <= n and candidate not in seen:
                seen.add(candidate)
                ans += 1
            elif candidate in seen:
                continue
            else:
                break
    print(n - ans)

if __name__ == '__main__':
    main()