if __name__ == '__main__':
    s = input()
    ans = float('inf')
    for i in range(len(s) - 2):
        diff = abs(int(s[i] + s[i+1] + s[i+2]) - 753)
        ans = min(diff, ans)
    print(ans)