from collections import deque

def is_win(dq, turn):
    if len(dq) == 0:
        print(turn.upper())
        exit()
    else:
        return False

def main():
    sa = input()
    sb = input()
    sc = input()
    sa = deque(sa)
    sb = deque(sb)
    sc = deque(sc)
    turn = "a"
    while True:
        if turn == "a" and not is_win(sa, turn):
            turn = sa.popleft()
        elif turn == "b" and not is_win(sb, turn):
            turn = sb.popleft()
        elif turn == "c" and not is_win(sc, turn):
            turn = sc.popleft()





if __name__ == '__main__':
    main()