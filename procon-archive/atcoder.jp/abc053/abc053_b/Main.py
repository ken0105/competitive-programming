from collections import deque

if __name__ == '__main__':
    s = input()
    print(s.rfind('Z') - s.find('A') + 1)

