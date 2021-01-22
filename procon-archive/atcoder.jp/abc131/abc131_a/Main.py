from collections import Counter

if __name__ == '__main__':
    s = input()
    before = ""
    for i in s:
        if i == before:
            print("Bad")
            exit()
        before = i
    print("Good")