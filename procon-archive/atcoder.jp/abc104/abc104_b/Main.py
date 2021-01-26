import re
from collections import Counter

if __name__ == '__main__':
    s = input()
    if s[0] != "A":
        print("WA")
        exit()

    c_cnt = Counter(s[2:-1])
    if c_cnt.get("C") != 1:
        print("WA")
        exit()

    s = s.replace("A","")
    s = s.replace("C", "")

    pattern = "[a-z]+"

    if re.fullmatch(pattern, s):
        print("AC")
        exit()
    else:
        print("WA")
        exit()

