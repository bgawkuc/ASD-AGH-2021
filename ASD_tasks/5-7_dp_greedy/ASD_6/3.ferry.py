#mamy prom mający poklad dolny i gorny
#na kazdy poklad moga wjechac auta o max łącznej dlg L
#przed promem stoją auta kazdy o dlg A1,A2,...
#auto wjezdza na poklad dolny lub gorny
#oblicz ile max aut zmiesci sie na promie
#zadne auto nie moze ominac kolejki

#tworze sobie tablice sum prefiksowcyh
#zeby wiedziec jaka jest suma dlugosci i aut
#tworze tablice dp gdzie wierszami jest ilosc samochodow jakie biore
#a kolumnami dlg pokladu

#mam dwie pętle
#k - ilosc aut co juz wjechala na prom[0,n-1]
#s - jaka dlg pokladu lewego zajelo to k aut(część z nich zajęła tez prawy poklad)

#mam auto numer k(te co byly przed nim sa juz na promie)
#i jesli wartosc dp[k][s] wynosi True, tzn ze k aut wjechalo na prom dlg s
#moge sprobowac wpusic k+1 auto

#mam dwie opcje:
#wpuszczam na LEWY pas:
#jesli s + A[k] <= d czyli obecna dlg promu + dlg k+1 auta jest mniejsza od granicy dlg
#to moge wpuscic k+1 aut a auto k+1 ląduje na lewy pas
#czyli dp[k+1][s+A[k]] = True (UWAGA dlg pasa s sie powiększa)
#wpuszczam na PRAWY pas:
#jesli pref[k+1] - s <= d
#czyli dlg k+1 aut - s(dlg aut na lewym pasie) to tak na prawde jest dlg aut na prawym pasie
#i jesli dlg aut na prawym pasie <= d
#to moge wpuscic auto na prawy pas
#dp[k+1][s] = True (UWAGA dlg pasa s sie nie zmienia)

#wyniku szukam po wierszach(bo to ilosc aut na promie)
#szukam wiersza o jak najwiekszym numerze gdzie znajduje sie choc jedno True
#numer tego wiersza to ilosc aut jaka wjedzie na prom

def ferry_loading(A,d):
    n = len(A)

    #tablica z sumami prefiksowymi
    #pref[i] - suma dlg i samochodow
    pref = [0] * (n+1)
    for i in range(1,n+1):
        pref[i] = pref[i-1] + A[i-1]

    #tablica gdzie kolumny to dlg pokladu
    #wiersze to ilosc samochodu jakie bierzemy
    dp = [[False] * (d+1) for _ in range(n+1)]
    dp[0][0] = True #dla dlg 0 wjezdza 0 samochodow

    for k in range(n): #ilosc aut ktora wjechala na prom
        for s in range(d+1): #zajeta dlg lewego pokladu

            #gdy k samochodow zmiescilo sie na pokladach o dlg s kazdy
            #to probuje zmiescic k+1 samochodow na promie
            if dp[k][s] == True:

                #jesli na lewym pokladzie(o dlg s), zmiesci sie jeszcze auto o idx k
                #czyli ilosc aut bedzie k+1, będą one zajmowac s+A[k] pokladu
                if s + A[k] <= d:
                    dp[k+1][s+A[k]] = True

                #pref[k+1] - s to ilosc miejsca jaka zostanie na prawym pokladzie
                #gdy wpuszcze na niego auto i idx k, czyli na promie byloby k+1 aut
                #s czyli dlg lewego pasa się nie zmieni
                if pref[k+1] - s <= d:
                    dp[k+1][s] = True


    #wynikiem jest mozliwie najwieksza watosc i(ilosc aut)
    #czyli sszukam 1 wiersza i od tylu gdzie wystapilo choc jedno True
    for i in range(n,-1,-1):
        for j in range(d+1):
            if dp[i][j] == True:
                return i #ile aut moze wjechac

#INNY ZAPIS
def ferry(A, length):
    n = len(A)
    pref = [0] * n
    pref[0] = A[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + A[i]
    # dp[idx][l] czy patrzac do auta idx moze ono wjechac na prom dlg l
    dp = [[False] * (length + 1) for _ in range(n)]

    # gdy pokald ma dlg minimum A[0] to auto o idx 0 sie zmiesci
    for i in range(A[0], length + 1):
        dp[0][i] = True

    for idx in range(n - 1):
        for l in range(1, length + 1):

            # gdy na poklad dlg l udało sie wjecgac autom do indeksu idx włącznie
            if dp[idx][l]:
                # na lewy pas próbuje wpuscic auto o indeksie idx
                if l + A[idx + 1] <= length:
                    dp[idx + 1][l + A[idx + 1]] = True

                # na prawy pas próbuj wpuścić auto o indeksie idx
                if pref[idx + 1] - l <= length:
                    dp[idx + 1][l] = True

    # szuakam jak najdalszego indeksu wiersza gdy dlg pokladu(kolumna) to length
    # i ma on wartosc True
    idx = n - 1
    while dp[idx][length] is False:
        idx -= 1

    for i in range(n):
        print(dp[i])

    return idx

A=[2,3,4,4]
A1 = [1,2,3,2]
print(ferry_loading(A,6))