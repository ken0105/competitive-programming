import re

if __name__ == '__main__':
    s = input()
    # now = -1
    # for w in "keyence":
    #     ok = False
    #     for index,i in enumerate(s):
    #         if index <= now:
    #             continue
    #         if i == w:
    #             now = index
    #             break
    #         if index == len(s) - 1:
    #             print("NO")
    #             exit()
    # print("YES")

    pattern = ["k[a-z]*eyence","k[a-z]*eyence","ke[a-z]*yence","key[a-z]*ence","keye[a-z]*nce","keyen[a-z]*ce","keyenc[a-z]*e","keyence[a-z]*"]

    ok = False
    for p in pattern:
        if re.fullmatch(p, s):
            print("YES")
            exit()
    print("NO")
