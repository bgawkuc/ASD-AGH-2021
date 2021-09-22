#mamy pret dlugosci n
#tniemy go na kawalki dlugosci 1,2,.. czy n metrow
#kawalek jest zawsze liczba calkowita
#znamy ceny odpowiednio 1,2,3..n metrowego kawalka
#ile wynosi maksymalny zysk przy pocieciu preta i jakie sa dlg kawalkow
#tablica P zawiera ceny poszczegolnych kawalkow
#czyli indeks 1-cena dlg 1m,

#f(n) - max zysk ze sprzedazy preta dlg n
#f(n) = max{P[i] + f(n-i)}, 1 <= i <= n
#f(0) = 0
#f(n) = max(f(n),price[i] + r[n-i])
#czyli tniemy pret na kawalek dlugosci i,
#i wywolujemy funkcje dla ceny P[i] + F(n-i)

#r[n] - tab ktora mowi jaki moze byc max profit dla dlg n
#s[n] - tab w ktorej zapamietuje numer wzietego akurat kawalka

#przebiegem dwoma pętlami
#pierwsza okresla mi current profit
#a druga nr pręta do ktorego się będę odnosić
#jesli max profit < profit j elementu + wartosc r[i-j](profit dla reszty dlg)
#to wartosc max profit zmieniam na taką
#i do tab z num wpisuje nr preta

#w tablivy val zapisuje max profit dla pręta dlg i
#przechodze liniowo po dlugosciach mozliwych od 1 do n
#w drugiej pętli sprawdzam odc j jaki odcinam obecnie z pręta od dlg 1 az do dłg i
#i spr czy wieksza jest obecna maxVal czy p[j] + val[i-j](odciecie na kawalek dlg j + zarobek dla reszty dlg pręta)


#NAJPROSTSZA IMPLEMENTACJA
def cutRod(P):
    n = len(P)
    dp = P[:]
    #dp[i] - max zarobek przy sprzedazy pręta o dlg i
    #i-dlg pręta
    for i in range(2,n):
        for cut in range(i): #na jakie kawałki tne pręt
            dp[i] = max(dp[i],P[cut]+dp[i-cut])
    return dp

#idx 1 : cena 1m,idx 2: cena 2m itd
p = [0, 1, 2, 7, 9, 6, 5]  # mam pret dlg n-1 czyli 6m
print(cutRod(p))

#gdy nie musze odtwarzac wyniku
from math import inf
def cutRod1(p):
    n = len(p) #dlugosc preta
    val = [0] * (n+1) #max wartosc jaką zarobie na pocieciu pręta dlg i

    for i in range(1,n+1): #i-obecna dlg pręta
        maxVal = -inf #ustawiam maxval na bardzo małą wartosc

        for j in range(0,i): #j-idx kawalka, dla j = 0 mam kawałek dlg 1m, dla j = i -1 mam kawalek dlg i
            maxVal = max(maxVal, p[j] + val[i-j-1])

        val[i] = maxVal

    return val[n] #zarobek dla pręta dlg n


#idx = 0 cena 1m, idx = 1 cena 2m itd
p = [1,2,7,9,6,5] #mam pret dlg n czyli 6m
print(cutRod1(p))