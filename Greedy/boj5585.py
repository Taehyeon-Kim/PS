money = 1000 - int(input())
count = 0

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    count += (money // coin)
    money %= coin

print(count)
