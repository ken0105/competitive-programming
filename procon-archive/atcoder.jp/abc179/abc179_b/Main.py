N = int(input())
iterator = 0

for i in range(N):
    j,k = map(int, input().split())
    if j == k:
        iterator += 1
    elif iterator != 0:
        iterator = 0
    else :
        pass

    if iterator >= 3:
        print("Yes")
        exit()

print("No")