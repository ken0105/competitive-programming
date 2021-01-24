if __name__ == '__main__':
    S = input()
    before = S[0]
    for s in S:
        if s != before:
            print("Lost")
            exit()
    print("Won")