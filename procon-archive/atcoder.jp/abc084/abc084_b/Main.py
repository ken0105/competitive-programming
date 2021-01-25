import re

if __name__ == '__main__':
    is_int = "\d"
    a,b = map(int,input().split())
    s = input()
    try:
        for i in range(a):
            if not re.fullmatch(is_int, s[i]):
                raise Exception
        if s[a] != "-":
            raise Exception

        for i in s[a+1:]:
            if not re.fullmatch(is_int, i):
                raise Exception
        print("Yes")
    except:
        print("No")




