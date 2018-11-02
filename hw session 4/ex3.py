prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0

for i in prices.keys():
    for j in stock.keys():
        if i == j:
            print(i)
            print("price:", prices[i])
            print("stock:", stock[j])
            total += (prices[i]*stock[j])
    print()
print("Total capital made:", total)