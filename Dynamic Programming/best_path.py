#mam macierz m na n
#wypełniona jest ona pola bezpiecznymi (o wartosci 0 oraz 1)
#oraz niebezbiecznymi (o wartosci -1)
#znajdz taką sciezke zaczynającą sie w 0,0 tak by liczb pól odwiedzonych z 1 była mozliwie jak największa
#w wierszach parzystyvh mozna isc tylko w dół lub w prawo
#a w nieparzystych w dół lub lewo

#tworze maciezr pomocnicza o takich samych wymiarach jak wejsiowa
#dp[i][j] oznacza wartosc najlepszej sciezki(czyli takiej co ma najwiecej 1)
#kończaca sie w i,j
#jesli A[i][j] = -1 to dp[i][j] = -1
#jesli i jest parzyste tzn ze przyszlam albo z dp[i-1][j] albo z dp[i][j-1]
#jesli i jest nieparzyste tzn ze przyszlam z dp[i][j+1] albo z dp[i-1][j]
#oczywiscie wchodzac na pole i,j sprawdzam czy to A[i][j] != -1 zeby sie dało na nie wejsc
#trzeba uwazac by nie wyjsc poza obszar macierzy


def isIn(m,n,x,y):
    if 0 <= x < m and 0 <= y < n:
        return True
    return False


def bestPath(M):
    m = len(M) #ilosc wierszy
    n = len(M[0]) #ilosc kolumn
    dp = [[0] * n for _ in range(m)]
    best = 0 #najwieksza ilosc 1 w sciezce


    for i in range(m): #przechodze rzedami

        if i % 2 == 0: #gdy rzad jest parzysty
            for j in range(n):  # w parzystych rzedach wypelniam po kolumnach od lewej od prawej

                if M[i][j] == -1: #gdy pole ma wartosc - 1
                    dp[i][j] = 0 #tzn ze nie da sie na nie dostac wiec ilosc '1' wynosi 0

                elif i == 0 and j == 0: #ilosc '1' w polu 0,0 wynosi wartosc tego pola bo z niego startuje
                    dp[i][j] = M[i][j]

                else: #moge sie poruszaac albo z lewej do prawej albo z góry na dół
                    up = left = 0

                    if isIn(m,n,i - 1,j): #gdy przychodze z góry na dół
                        up = dp[i-1][j]

                    if isIn(m,n,i,j - 1): #gdy przychodze z lewej do prawej
                        left = dp[i][j-1]

                    better = max(up,left) #szukam max wart z lewej i gory

                    if better != 0: #i jesli okaze sie ze byla ona wieksza od 0
                        dp[i][j] = M[i][j] + better #to ustawiam wartosc dostania sie do tego pola

                        if dp[i][j] > best: # i sprawdzam czy nie jest ona wieksza od najwiekszej
                            best = dp[i][j]
                    else: #a jak nie to ustawiam wartosc pola na 0
                        dp[i][j] = 0

        else: #gdy poruszam sie po nieparzystych rzędach
            for j in range(n-1,-1,-1): #w nieparzystych rzedach wypelniam od kolumny prawej do lewej

                if M[i][j] == -1: #gdy trafie na pole o wart -1(brak mozliwosci ruchu)
                    dp[i][j] = 0

                else:
                    up = right = 0

                    if isIn(m,n,i-1,j): #ruch z góry na dół
                        up = dp[i-1][j]

                    if isIn(m,n,i,j+1): #ruch z pola z prawej na to po lewej
                        right = dp[i][j+1]

                    better = max(up,right) #biore wieksza z tych wartosci

                    if better != 0: #i jesli ona jest dodatnia to taką tworze z niej ściezke
                        dp[i][j] = M[i][j] + better #dlg sciezki to wartosc pola + wartosc better

                        if dp[i][j] > best:
                            best = dp[i][j]

                    else:
                        dp[i][j] = 0
    for i in range(m):
        print(dp[i])

    return best #zwracam wartosc best

M = [
        [1,1,1,1,1],
        [1,0,0,1,1],
        [1,1,-1,1,1],
        [-1,1,1,1,1],
        [1,1,-1,-1,1]
    ]
print(bestPath(M))


