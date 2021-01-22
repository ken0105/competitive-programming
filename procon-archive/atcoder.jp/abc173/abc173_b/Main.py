loop_count = int(input())

ac_count = 0
wa_count = 0
tle_count = 0
re_count = 0

for i in range(loop_count):
    result = input()
    if result == 'AC':
        ac_count += 1
    elif result == 'WA':
        wa_count += 1
    elif result == 'TLE':
        tle_count += 1
    else:
        re_count += 1

print("AC x {0}".format(str(ac_count)))
print("WA x {0}".format(str(wa_count)))
print("TLE x {0}".format(str(tle_count)))
print("RE x {0}".format(str(re_count)))


