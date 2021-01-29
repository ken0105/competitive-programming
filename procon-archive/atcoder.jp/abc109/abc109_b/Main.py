if __name__ == '__main__':
    n = int(input())
    seen = set()
    words = []
    for i in range(n):
        word = input()
        if word in seen:
            print("No")
            exit()
        if i > 0 and words[-1][-1] != word[0]:
            print("No")
            exit()
        seen.add(word)
        words.append(word)
    print("Yes")
