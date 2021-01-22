from itertools import combinations
import re
if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(n):
        li.append(input())
    notmatch = [s.replace("!", "") for s in li if re.match('^\![a-z]+$',s)]
    notmatch = set(notmatch)
    match = [s for s in li if re.match('^[a-z]+$', s)]
    ans = notmatch.intersection(set(match))
    if len(ans) != 0:
        print(list(ans)[0])
    else:
        print("satisfiable")