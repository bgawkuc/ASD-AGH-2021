#schody amazona
#dana jest tab a zawierajaca liczby naturalne >= 1
#stoje na polu o indeksie 0
#wartosc pola mowi jak max dlugi skok mozemy wykonac na inne pole
#policz na ile sposobow da sie dotrzec pod indeks n -1

#1 sposob
#f(i) ilosc sposobow na jakie mozna sie dostac z pola o ind i na pole o ind n-1
#tworze tablice P dlugosci n, jej ostatni el ma wartosc 1, reszta 0
#iteruje od konca
#wchodze na pole n - 2, sprawdzam jego wartosc x tzn ze P[n-2] dostanie sume wartosci P[n-2+y], 0 <= y <= x
#i tak przesuwam sie do 0 ind
#dla tab wejsciowej T: [2,1,3,2,1,0] tab P:[8,4,4,2,1,1]
#z T[4] da sie tylko isc na T[5] wiec P[4] = P[5]
#z T[3] da sie isc na T[4] lub na T[5] P[3] = P[4]+P[5]
#P[2] = P[3]+P[4]+P[5], P[1]= P[2], P[0] = P[1]+P[2]
#zwracam P[0]

def cntWays(A):
    n = len(A)
    ways = [0] * n #ilosc sposobow na jakie sie da dostac z i-tego pola na koncowe
    ways[n-1] = 1 #z ostatniego na ostatniego jest tylko 1 sposob

    for i in range(n-2,-1,-1): #sprawdzam kazde pole od tyłu tablicy
        for j in range(1,A[i]+1): #sprawdzam dla kazdej dlg skoku, max dlg skoku A[i]
            if j + i < n: #skok nie moze przeszkoczyc tablicy
                ways[i] += ways[i+j] #to do i-tego pola dodaje wartosc pola na które doskoczyłam
    print(ways)
    return ways[0]

T= [2,1,3,2,1,0]
print(cntWays(T))


#2 sposob
#f(i)-liczba sposobow na jakie mozemy dojsc na pozycje i
#robie to samo co w 1 sposobie tylko zaczynam od indeksu 0
#tworze tablice P
#P[0] = 1
#T = [2,1,3,2,1,0]
#z T[0] moge przejsc na T[1] lub T[2], czyli P[1] += P[0], P[2] += P[0]
#P[1] = P[2] = 1
#z T[1] moge na T[2] czyli P[2] += P[1], P[2] = 2
#z T[2] na T[3],T[4],T[5] czyli P[3], P[4], P[5] += P[2]
#P[3] = P[4] = P[5] = 2
#z T[3] na T[4] lub na T[5] czyli P[4], P[5] += P[3]
#P[4] = P[5] = 4
#z T[4] tlko na T[5] czyli P[5] += P[4]
#P[5] = 8

def cntWays2(A):
    n = len(A)
    ways = [0] * n #ilosc sposobow by dostac sie z pola 0 do i tego
    ways[0] = 1

    for i in range(n): #wybieram pole
        for j in range(1,A[i]+1): #sprawdzam jego wszystkie długosci skoków
            if i + j < n: #gdy nie przeskocze tablicy
                ways[i+j] += ways[i] #pole na które doskoczyłam dostaje wartosc pola z którego się dostałam

    print(ways)
    return ways[n-1]

T= [2,1,3,2,1,0]
print(cntWays2(T))