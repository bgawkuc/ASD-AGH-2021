#mam tablice m na n wypelniona wartosciami
#znajdz najdluzsza sciezke
#mozna sie poruszac po polach sasiadujacyh krawedziami o rosnacych wart
#czyli cena kazdego pola musi byc wyzsza od poprzedniego

#mamy pkt startowy
#f(i,j) = max{ f(i-1,j),f(i+1,j),f(i,j-1),f(i,j+1)} + 1
#f(i,j) = 1
#{f(i-1,j)-> i-1 >= 0,T[i-1][j] > T[i][j],(i+1,j),f(i,j-1),f(i,j+1):
#(analogiczne warunki do reszty przyp trzeba dodac)

#bez pkt startowego
#wzor sie nie zmieni
#funkcja taka sama, przechodze po calej tab i szukam tej sciezki
#tworze tab pomocnicza P wypelniam None w ktorej dodaje dlg sciezki dla danego pola
#czyli gdy jakies pole w P ma wartosc(!= None) to sie nie musze powtarzac i liczyc tego
#tylko moge isc dalej
#f(i,j) dlg najdluzszej sciezki w zaczynajacej sie w oi,j
#zloznosc O(m*n)

#tworze tablice rozmiarow taka jak wejsciowa
#rekurencja spr jaka jest najdluzsza sciezka zaczynajaca sie w tym polu
#i tak przechodze po całej tablicy

#funkcja rekurencyjna znajduja najdluzsza sciezke od pola i,j
def find_longest(i, j, A, m, n, dp):
    if i < 0 or i >= m or j < 0 or j >= n: #gdy wyjde poza obszar
        return 0

    if dp[i][j] != None: #gdy sciezka z tego pola juz była kiedys liczona
        return dp[i][j] #to zwracam jej wartosc

    x, y, z, w = -1, -1, -1, -1

    if j + 1 < n and A[i][j] < A[i][j + 1]:  # w prawo
        x = 1 + find_longest(i, j + 1, A, m, n, dp) #dlg sciezki to 1 + dlg sciezki od pola po prawej

    if j - 1 >= 0 and A[i][j] < A[i][j - 1]:  # w lewo
        y = 1 + find_longest(i, j - 1, A, m, n, dp) #dlg sciezki to 1 + dlg sciezki po lewej

    if i + 1 < m and A[i][j] < A[i + 1][j]:  # w dół
        z = 1 + find_longest(i + 1, j, A, m, n, dp) #dlg sciezki to 1 + dlg sciezki w dół

    if i - 1 >= 0 and A[i][j] < A[i - 1][j]:  # w góre
        w = 1 + find_longest(i - 1, j, A, m, n, dp) #dłg sciezki to 1 + dlg sciezki w góre

    dp[i][j] = max(x, max(y, max(z, max(w, 1)))) #szukam max wartosci sciezek w lewo,prawo,gore i dół
    return dp[i][j] #zwracam dłg max sciezki


def lengthOfPath(A):
    m = len(A)  # ilosc wierszy
    n = len(A[0])  # ilosc kolumn
    res = 1

    dp = [[None] * n for _ in range(m)] #tworze tablice w ktorej bede trzymac dlg sciezek dla odpowiednich pol

    for i in range(m): #przechodze po wierszach

        for j in range(n): #po kolumnach

            if dp[i][j] == None: #gdy sciezka dla tego pola nie była jeszcze liczona
                find_longest(i, j, A, m, n, dp) #sprawdzam najdluzsza sciezke zaczynajaca sie w i,j

            res = max(res, dp[i][j]) #zapamietuje wynik obecnie najdluzszej sciezki


    for i in range(m):
        print(dp[i])

    return res

#GDYBY TRZEBA BYLO ZNALEŹĆ MAX WAGE SUMY ELEMENTOW NA SCIEZCE
#reszta warunków jak w oryginalnym zadaniu

def mostValuablePath(A):
    n = len(A)
    m = len(A[0])
    dp =[[None] * m for _ in range(n)]
    maxi = 0

    def isIn(i,j):
        return 0 <= i < n and 0 <= j < m

    #oblicza wartosc sciezki zaczynajacej sie w polu o idx i,j
    def pathValue(i,j):
        if not isIn(i,j):
            return 0
        #gdy pole jest policzone
        if dp[i][j] is not None:
            return dp[i][j]

        up = left = right = down = A[i][j]

        if isIn(i-1,j) and A[i-1][j] > A[i][j]:
            down += pathValue(i-1,j)
        if isIn(i+1,j) and A[i+1][j] > A[i][j]:
            up += pathValue(i+1,j)
        if isIn(i,j-1) and A[i][j-1] > A[i][j]:
            left += pathValue(i,j-1)
        if isIn(i,j+1) and A[i][j+1] > A[i][j]:
            right += pathValue(i,j+1)

        return max(down,max(up,max(left,max(right,0))))


    for i in range(n):
        for j in range(m):
            if dp[i][j] is None:
                dp[i][j] = pathValue(i,j)
            maxi = max(maxi,dp[i][j])

    for i in range(n):
        print(dp[i])
    return maxi

a = [
    [3,7,9,0],
    [2,3,8,5],
]
print(lengthOfPath(a))
print(mostValuablePath(a))
