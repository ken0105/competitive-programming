from collections import deque

if __name__ == '__main__':
    s = input()
    if "S" in s and "N" in s and "E" in s and "W" in s:
        print("Yes")
    elif "S" not in s and "N" not in s and "E" not in s and "W" not in s:
        print("Yes")
    elif "S" in s and "N" in s and "E" not in s and "W" not in s:
        print("Yes")
    elif "S" not in s and "N" not in s and "E" in s and "W" in s:
        print("Yes")
    else:
        print("No")






