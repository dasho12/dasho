#bodolt
def greedy_coin_change(tugrug):
    zoos = [25, 10, 5, 1]
    coin_count = {}
    
    for coin in zoos:
        count = tugrug // coin
        if count > 0:
            coin_count[coin] = count
            tugrug -= count * coin
            
    return coin_count

#1C
x= greedy_coin_change(67)
print(x)
