# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, 
# który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, wydający najpierw największą monetę, 
# nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

#tworze tablice dp rozmiaru value+1(value-kwota jaką chcemy uzyskać) wypełnioną wartościami inf
#dp[i] - minimalna ilosc monet jaką należy użyć aby stworzyc kwote i

from math import inf

def minCoins(coins,value):
    dp = [inf] * (value+1)
    dp[0] = 0

    for currVal in range(1,value+1):
        for coin in coins: 
            #jesli z uzyciem wybranej monety da sie stworzyc kwote currVal
            if coin <= currVal: 
                dp[currVal] = min(dp[currVal], dp[currVal-coin] + 1)

    return dp[value]
