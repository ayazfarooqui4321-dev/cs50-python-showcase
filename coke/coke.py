
def main():
    bottle_price = 50
    coin_denomination = [25, 10, 5]

    while bottle_price > 0:
        coin = int(input("Insert Coin: ").strip())

        if coin in coin_denomination:
            bottle_price -= coin
        if bottle_price > 0:
            print(f"Amount Due: {bottle_price}")


    if bottle_price < 0:
        change = -bottle_price
    else:
        change = bottle_price

    print(f"Change Owed: {change}")

main()
