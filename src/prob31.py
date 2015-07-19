#!/usr/bin/python

COIN_SET = [1, 2, 5, 10, 20, 50, 100, 200]

def count_change(total, coin_set):
    if total < 0:
        return 0
    
    if total == 0:
        return 1

    if len(coin_set) == 0:
        return 0

    coin = coin_set[-1]
    return (count_change(total - coin, coin_set) +
            count_change(total, coin_set[0:-1]))
        

if __name__ == "__main__":
    print count_change(200, COIN_SET)
