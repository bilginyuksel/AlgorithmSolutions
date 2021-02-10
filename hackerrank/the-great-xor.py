def greatXor(num):
    power = 0
    result = 0
    while num != 0:
        if num & 1 == 0:
            result += 2 ** power
        power += 1
        num >>= 1
    return result

test = int(input())
for _ in range(test):
    num = int(input())
    print(greatXor(num))

