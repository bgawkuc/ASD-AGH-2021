#mamy czolg ktory chce dojechac z pkt O do jakiegos pkt a
#mamy jego pojemnosc baku(L)-pojemnosc w litrach, czolg startuje z pelnym bakiem
#czolg spala 1 litr na 1 km
#mamy dwie tablice S oraz P
#w s sa pkt na ktorych sa stacje benzynowe
#a w p sa podane odpowiednie cany za litr
#mamy 3 problemy
#a)oblicz min ilosc tankowan by dotrzec do pkt a
#b)oblicz min koszt dotarcia do pkt a gdy na stacji tankujemy dowolna ilosc paliwa
#c)oblicz min koszt dotarcia do pkt a gdy na stacji na ktorej sie zatrzymamy musimy zatankowac do pelna


#a) tankujemy na najdalszej stacji (do pełna) do ktorej jestesmy w stanie dojechac
#tankowanie wczesniej pozbawia nas optymalnego rozwiazania
#ale zmiana tankowania na dalsza nie pozbawia nas optymalnego rozwiazania

#A-pkt docelowy
#L-pojemnosc baku
#S-lista pkt na ktorych sa stacje

#dowod:
#jesli zakladam ze od stacji k mam optymalny wynik
#a jak wezmieemy stacje i i dojezdzamy do tej stacji co z stacji a to dostajemy ten sam wynik
#czyli sprzecznosc bo zalozylam ze od k jest ten optymalny wynik

def tank(A,L,S):
    currLocation = 0 #obecna lokalizacja
    cnt = 0 #ilosc odwiedzonych stacji
    lastStation = -1 #indeks stacji odwiedzonej ostatnio, na poczatku zadna to -1

    while True:

        if A - currLocation <= L: #gdy odleglosc od pkt A <= pojemnosci baku
            return cnt

        longestDist = currLocation + L #jak najdalej moge dojechac na pelnym baku
        idx = lastStation #index ostatnio odwiedzonej stacji


        while idx + 1 < len(S) and S[idx+1] <= longestDist: #szukam mozliwie najdalszej stacji, patrze na stacje o ind 1 wiekszym
            #gdy dam rade do niej dojechac to jade na nia(idx++)
            idx += 1  # ind najdalszej stacji z ktorej korzystam

        if (idx == lastStation): #gdy nie zwiekszymy indeksu tzn ze nie da sie dotrzec na zadna stacja
            #czyli nie dotrzemy do pkt A
            return None

        lastStation = idx
        cnt += 1
        currLocation = S[idx]
        print("ind odiwedzonej stacji: ",lastStation)

S = [1,3,6,7]
A = 10
L = 5
# print(tank(A,L,S))


#b)dojezdzamy do stacji i jesli z niej jestesmy w stanie dojechac do kolejnej stacji w ktorej cena za paliwo
#jest nizsza niz ta na ktorej stoimy to tankujemy tylko tyle zeby dojechac do kolejenj
#jesli nie ma w zasiegu stacji ktora ma ceny nizsze niz nasza to tankujemy do pelnia i przejezdzamy do stacji
#o najnizszych cenach w zasiegu

#rozw dynamiczne, sam pomysł
#f(i) min koszt by dotrzec na i-ty km
#f(k) = 0; k <= L(poj baku)
#f(k) = f(k-1) + min(P[r]); r nalezy od k - l + 1 do k - 1



from math import inf

def tank2(A,L,S,P):
    curr = 0 #obecna lokalizacja
    cost = 0
    last = -1 #indeks stacji odwiedzonej ostatnio, na poczatku zadna to -1
    maxL = L #max pojemnosc baku

    while True:

        idx = last #index ostatnio odwiedzonej stacji
        mini = inf #idx najtanszej stacji w okolicy

        while idx+1 < len(S) and S[idx+1] <= curr + L: #szukam najtanszej stacji w zasiegu baku
            if mini == inf:
                mini = idx + 1

            elif mini != inf and P[idx+1] <= P[mini]:
                mini = idx +1
            idx += 1

        L -= (S[mini]- curr) #jade na najtansza stacje w okolicy
        curr = S[mini] #obecne miejsce
        last = mini #ta stacja staje sie ostatnio odwiedzoną stacją

        j = mini
        newMini = inf


        while j + 1 < len(S) and S[j+1] - curr <= maxL: #patrze czy znajduje sie z przodu jakas tansza stacja
            if newMini == inf and P[j+1] < P[mini]:
                newMini = j + 1
            j += 1

        if newMini == inf: #czyli w zasiegu baku nie ma juz tanszej stacji

            if A - curr <= maxL: #gdy z tej stacji jestem w stanie dojechac do konca a przede mna nie ma tanszej
                if A - curr > L: #gdy jest to konieczne to dopelniam bak
                    lack = A - curr - L
                    cost += lack * P[mini]
                return cost

            #gdy nie jestem w stanie z tej stacji dojechac do konca
            #to na mini tankuje do pelna
            lack = maxL - L
            cost += lack * P[mini]
            L = maxL


        else: #gdy znajduje sie tansza stacja w zasiegu baku

            if S[newMini] - curr > L: #gdy na obecnym zapelnieniu baku nie dam rady dojechac do tanszej stacji
                lack = S[newMini] - curr - L #ilosc brakujacych litrow
                cost += lack * P[mini] #to tankuje tyle by dojechac do tanszej
                L += lack


#INNA IMPLEMENTACJA, MOZLIWE ZE BARDZIEJ ZROZUMIAŁA
def tankD(S,P,gas,end):
    #station,price-info czy jest stacja i jaka jest tam cena za litr
    station = [False] * (end+1)
    price = [None] * (end+1)
    for idx in range(len(S)):
        station[S[idx]] = True
        price[S[idx]] = P[idx]

    cost = 0 #koszt podrozy
    idx = 0 #obecny indeks
    currGas = gas #obecna ilosc paliwa

    while True:
        #gdy z pozycji idx jestem w stanie dojechac do konca bez tankowań
        if idx + currGas >= end:
            return cost

        #szukam najblizszej stacji i na nią jadę
        new = None
        for i in range(idx+1,idx+gas+1):
            if i <= end and station[i]:
                new = i
                #zuzycie paliwa na dojechanie na stacje i-tą
                currGas -= (i-idx)
                break

        #gdy nie ma zadnej stacji w zasiegu baku tzn ze nie da sie dojechac do konca
        if new is None:
            return False
        else:
            idx = new

        #szukam stacji w zasięgu baku z tanszych paliwem
        new = None
        for i in range(idx+1,idx+gas+1):
            if i <= end and station[i] and price[i] < price[idx]:
                new = i
                break

        #gdy nie ma w zasiegu stacji idx stacji z tanszym paliwem
        if new is None:
            #gdy po zatankowaniu(lub bez niego) dostane sie na tym baku do konca
            if idx + gas >= end:
                #ilosc brakującego paliwa(ujemna to brakuje)
                missing = currGas - (end-idx)
                #jesli trzeba to tankuje
                if missing < 0:
                    cost += (abs(missing) * price[idx])
                    currGas += abs(missing)
                #zwracam wynik
                return cost
            #gdy nawet zatankowanie do pełna nie pozwoli mi dojechac do konca
            else:
                #to na stacji idx tankuje do pełna
                cost += ((gas-currGas) * price[idx])
                currGas = gas

        #gdy w zasięgu jest tansza stacja to tankuje tyle by dostac sie na nią
        else:
            #missing - jak jest ujemne to tyle litrow brakuje, wiec tyle tankuje na idx
            missing = currGas - (new-idx)
            if missing < 0:
                cost += (abs(missing) * price[idx])
                currGas += abs(missing)


#24
s = [10,40,54]
p = [3,5,2]
a = 60
l = 50
#7
s1 = [3,5,6,8]
p1 = [2,3,1,4]
a1 = 9
l1 = 4
#41
A0 = 25
S0 = [ 2, 4, 6, 9, 11, 13, 16, 18, 20]
C0 = [ 4, 3, 2, 3, 3, 5, 4, 2, 4]
L0 = 7
#34
A1 = 30
S1 = [1, 9, 15, 16, 17, 27]
C1 = [1, 100, 10, 15, 1, 30]
L1 = 14
print(tank2(a,l,s,p))

#c) jak wybiore jakąs stacje to juz musze na niej tankowac do pelna
#dp = [[inf,gas] * (len(S)+1)]
#dp[i][0] - najtanszy koszt dojechania do itej stacji
#dp[i][1] - ilosc paliwa jaką mmam w itej stacji
#P[i] - koszt tankowania na i-tej stacji
#S(i) - odlgl i-tej stacji od poczatku
#min koszt dojechania do pola i to: min po tym polu, oraz sumie gdy tankuje w j(DO PEŁNA) i jade z niej do i
#dp[i][0] = min(dp[(i][0] + (dp[j][0]+(S[i]-S[j])*P[j]); S[i] - S[j] <= gas
#gdy dp[i][0] == dp[j][0]+(S[i]-S[j])*P[j] - zatankowałam w j
#to dp[i][1] = gas - (S[i]-S[j]) - ilosc paliwa w i

from math import inf

#jak zatrzymam sie na jakiejs stacji to musze zatankowac w niej do pełna
def tank3(S,P,gas,end):
    n = len(S)
    #dp[i][0],dp[i][1] - koszt dojechania do i-tej stacji(idx 0) majac w baku iles paliwa na niej(idx 1)
    dp = [[inf,gas] for _ in range(n+1)]
    #gdy najblizsza stacja jest poza pojemnością baku
    if S[0] > gas:
        return False

    #koszt dojechania do stacji odłegłych <= pojemnosc baku - wynosi 0
    idx = 0
    while S[idx] <= gas:
        dp[idx][0] = 0
        dp[idx][1] -= S[idx]
        idx += 1

    #do tablic stacji i cen dodaje punkt koncowy
    S.append(end)
    P.append(None)

    #gdy curr == n tzn ze patrze na punkt koncowy
    for curr in range(idx,n+1):
        prev = curr - 1
        #gdy najblizsza stacja jest oddalona o wiecej niz pojemnosc baku tzn ze nie jest to mozliwe
        if S[curr] - S[prev] > gas:
            return False

        #patrze na wszystkie stacje przed z których da się dojechac do curr
        while prev >= 0 and S[curr] - S[prev] <= gas:

            #wartosc kosztow w curr to minimum:
            #po tym polu (gdy nie tankuje w prev)
            #po tankowaniu w prev + koszcie jaki tzreba było wydac na paliwo w prev by zatankować do pełna
            dp[curr][0] = min(dp[curr][0],dp[prev][0]+P[prev]*(gas-dp[prev][1]))

            #gdy zatankowałam w prev
            if dp[curr][0] == dp[prev][0] + P[prev] * (gas-dp[prev][1]):
                #to ilosc paliwa w curr to od calego baku odjęta roznica odlgl
                dp[curr][1] = gas - (S[curr] - S[prev])
            prev -= 1

    return dp[n][0]


#gdy zatrzymuje sie na stacji o idx: 0(1l) i 2(4l)
#1 * 3 + 2 + 4 = 11
S2 = [1,3,5,6,7]
P2 = [3,4,2,2,3]
A2 = 9
L2 = 4
# print(tank3(S2,P2,L2,A2))











