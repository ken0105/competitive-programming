N = int(input())

# if N < 7:
#     print(-1)
#     exit()
if N % 2 == 0 or N % 5 == 0:
    print(-1)
    exit()
i = 0
num = 0
while True:
    num = (num * 10 + 7) % N
    i += 1
    if num == 0:
        print(i)
        exit()

K = int(input())

if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()

i = 0
ai = 0
while True:
    ai = (ai * 10 + 7) % K
    i += 1
    if ai == 0:
        break
print(i)