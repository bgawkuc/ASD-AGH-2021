#gramy z 2 graczem
#wybieramy sobie jedna wartosc z jednego z koncow tablicy 1D i dodajemy do swojej sumy
#to samo robi nasz przeciwnik
#zakladajac ze przeciwnik gra optymalnie jaka max sumę mozemy uzbierac

#slabe podejscie - przeciwnik ulatwia nam wygranie
#mamy sie odowlywac rekurencyjnie do tab o 2 mniejszej
#f(i,j) - najwieksza suma jaka jestesmy w stanie uzyskac w tab T[i:j]
#f(i,j) = max(f(i+1,j-1) + T[i]; f(i+1,j-1) + T[j]; f(i+2,j) + T[i]; f(i+2,j)+T[j])

#to jest gdy przeciwnik gra optymalnie
#ja wybieram sobie el z poczatku lub konca
#a przeciwnik bierze el z poczatku lub konca ale mozliwie jak najwiekszy
#wiec do mojego wyniku dodaje min wartosc
#f(i,j) = max(T[i] + min(f(i+2,j),f(i+1,j-1)); T[j] + min(f(i,j-2),f(i+1,j-1))
#f(i,j) = T[i], j == i
#f(i,j) = max(T[i],T[j), j ==i + 1(2 elementowy przedzial)

#tablica res zapelnia sie przekatnymi
#tablica res- wspolrzedne mi mowia od jakiego indeksu zaczynam i na jai koncze gre
#wszystko pod przekatna gorna jest 0
#na przekatnej glownej jest wpisana tab A
#a potem po kolei uzupelniam przekatne nad nia az dojde do prawego gorneo rogu
#gdzie znajduje sie wynik

#po kolei biore przedzialy 1,2,...,n-elementowy i ustalam indeksy startowe oraz koncowe
#gdy przedzial jest min 3 elementowy to do mojej wybranej wartosci dodaje min z reszty(bo przeciwnik wezmie max)
#i w odpowiednie miejsce przypisuje wartosc maxymalnego wyboru dla mnie

#res[j-i][j] - moj max wynik gdy gram na tablicy o koncowym idx j oraz poczatkowym j - i


#ŁATWIEJSZA IMPLEMENTACJA
def game(A):
    n = len(A)
    #dp[x][y]- najlepszy wynik gdy gram na planszy zaczynajac sie na idx x i konczacej na idx y
    #rozmiar y - x + 1
    dp = [[0] * n for _ in range(n)]

    #gdy gram na planszy rozpoczynajacej sie i konczacej sie na tym samym idx (rozmiar 1)
    #to moj 'zarobek' to wartosc tego pola
    for i in range(n):
        dp[i][i] = A[i]

    #gdy gram na planszy o rozmiarze 2 to moj zarobek to wieksza z wartosci
    for i in range(n-1):
        dp[i][i+1] = max(A[i],A[i+1])

    #wybieram rozmiar tablicy
    #poczatek i na podstawie tego mam koniec przedziału
    for size in range(2,n):
        for l in range(n):
            r = l + size
            if r < n:
                #gdy ja wybieram lewy el
                #to przeciwnik grajac optymalnie wybierze wiekszy z pol l+1 i r
                #wiec mi przypadnie z minimum z tego
                dp[l][r] = max(dp[l][r],A[l] + min(dp[l+2][r],dp[l+1][r-1]))
                #gdy ja wybieram prawy el
                #to przeciwnik grajac optymalnie wybierze wiekszy z pol r+1 i l
                #wiec mi przypadnie z minimum z tego
                dp[l][r] = max(dp[l][r],A[r] + min(dp[l][r-2],dp[l+1][r-1]))

    #najlpszy wynik w planszy zaczynajacej sie w idx 0 a konczacej w idx n-1
    return dp[0][n-1]


#TRUDNIEJSZA IMPLEMENTACJA
def biggestScore(A):
    n = len(A)

    res = [[0] * n for _ in range(n)]

    for i in range(n): #i + 1 = ilosc elementow w grze
        for j in range(i,n): #koncowy indeks

            k = j - i #startowy indeks

            #w petle x,y,z wejde w momencie gdy bede grała dla gry i >= 2 czyli gdy gra ma min 3 elementy
            x = 0
            #gdy w rundzie wzieto 1 i 2 element
            if (k + 2) <= j:
                x = res[k+2][j]

            y = 0
            #gdy w rundzie wzieto 1 i ostatni element
            if (k + 1) <= (j - 1):
                y = res[k+1][j-1]

            z = 0
            #gdy wzieto ostatni i przedostatni element
            if k <= (j-2):
                z = res[k][j-2]

            #(x,y) i (y,z) to przedzialy jakie zostaną po ruchu moim i przeciwnika
            #minimum z nich bo przeciwnik wezmie maximum skoro gra optymalnie
            #ja wybieram A[k] lub A[j] element i do tego dodaje min wartosc z zakresu
            #(bo przeciwnik wezmie max z zakresu)
            #min (a,b) bo zostanie nam minimalny przedzial skoro oboje wzielismy optymalne wyniki
            #A[k]+ min(x,y) - ja biore 1 el a przeciwnik bierze 2 lub oststni
            #A[j]+min(y,z) - ja biore ostatni el a przeciwnik bierze 1 lub przedostatni
            res[k][j] = max(A[k] + min(x,y), A[j] + min(y,z))

    for i in range(n):
        print(res[i])

    return res[0][n-1]

arr3 = [ 20, 30, 2, 2, 2, 10]
a = [1,4,2,3]
a1 = [5,1,4,2,3]
print(biggestScore(arr3))




