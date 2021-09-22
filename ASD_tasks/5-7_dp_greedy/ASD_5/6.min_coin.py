#jaka jets minimalna ilosc monet by wydac daną kwote - value
#uzywam monet z tablicy coins

#tworze tablice rozmiaru value+1 wypłnioną inf
#dp[i] - minimalna ilosc monet jaką należy użyć aby stworzyc kwote i
#gdy jest to niemozliwe to wartosc dp[i] wynosi inf
#dp[0] = 0, poniewaz abyy utworzyc kwote 0 potrzebuje 0 monet

#mam 2 pętle
#przechodze liniowo po kwotach od 1 do value
#przechodze po monetach
#jesli wartosc monety <= kwoty to potencjalnie mogę uzyc tej monet
#wiec licze wtedy min z uzyciem lub nie uzyciem tej monety
#dp[i] = min(dp[i]; dp[i-coin] + 1)
#dp[i-coin] + 1 <- 1 bo uzywam monety coin + ilosc monet jaką potrzebuje by stworzyc reszte monet

from math import inf

def minCoins(coins,value):
    dp = [inf] * (value+1) #min ilosc monet by stworzyc kwote i
    dp[0] = 0 #by utworzyc kwote 0 potrzebuje 0 monet

    for currVal in range(1,value+1): #obecna kwota
        for coin in coins: #indeks monety ktora wybieram
            if coin <= currVal: #jesli z uzyciem wybranej monety da sie stworzyc kwote currVal

                #t[currVal] to minimum po obecnej ilosci monet potrzebnej by stworzyc tę kwotę
                #i ilosci monet potrzebnej by stworzyc reszte kwoty powiekszonej o 1(moja obecna zabrana moneta)
                #reszta kwoty to roznica obecnej kwoty - wartosc monety
                #t[currVal - coins[j]] -> ilosc monet jaka potzrebuje by policzyc reszte kwoty przy uzyciu monety coins[j]
                dp[currVal] = min(dp[currVal], dp[currVal-coin] + 1)

    return dp[value]


coins = [9, 7, 5, 2]
coins1 = [3,4,2,5]
print(minCoins(coins1,13))