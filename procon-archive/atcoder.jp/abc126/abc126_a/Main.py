def main():
    n,k = map(int,input().split())
    s = list(input())
    diff = ord('A') - ord('a')
    s[k-1] = chr(ord(s[k-1]) - diff)
    print("".join(s))
if __name__ == '__main__':
    main()

