n = int(input())
li = list(map(int, input().split()))

alice_sum = 0
bob_sum = 0
game = 0
li.sort(reverse=True)
for i in li:
    game += 1
    if game % 2 == 0:
        bob_sum += i
    else:
        alice_sum += i

print(alice_sum - bob_sum)
