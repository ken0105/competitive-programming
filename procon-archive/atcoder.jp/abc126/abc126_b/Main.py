def main():
    s = input()
    left = int(s[0:2])
    right = int(s[2:])
    ans = "NA"
    if 1 <= right <= 12 and 1<= left <= 12:
        ans = "AMBIGUOUS"
    elif 1 <= right <= 12:
        ans = "YYMM"
    elif 1<= left <= 12:
        ans = "MMYY"
    print(ans)





if __name__ == '__main__':
    main()