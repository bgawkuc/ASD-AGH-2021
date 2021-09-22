#najdluzszy wspolny podciag
#longest common subsequence
#mam tablice A i B dlg n kazda
#sprawdz jakiej dlugosci jest najdluzszy wspolny podciag

#zlozonosc O(n*m)
#f(i,j) =
#1) 0 dla i = 0 lub j = 0
#2) f(i-1,j-1) + 1 dla i,j >0 i Ai = Bj
#3)max(f(i-1,j),f(i,j-1)) dla i,j > 0 i Ai != Bj

#tworze wymiarach dlg slowa A + 1 na dlg slowa B + 1
#dp[a][b] dlg max wspolnego podciagu jaki sie da uzyskac patrzac na a liter z A i b liter z B

def LCS(A,B):
    m = len(A)
    n = len(B)

    #tablica rozmiarow dlg kazdego slowa + 1
    dp = [[0] * (n+1) for _ in range(m+1)]

    for a in range(1,m+1): #wyninek dlugosci a z ciągu A
        for b in range(1,n+1): #wycnek dlugosci b z ciagu B

            #gdy liczby o idx a-1 i b-1 sa rowne
            #to pole dostaje wartosc taką jaka była na ukos + 1
            #czyli max dlg podciagu jaka byla dla ciagow o dlg a-1 oraz b-1
            if A[a-1] == B[b-1]:
                dp[a][b] = dp[a-1][b-1] + 1

            #gdy liczby są różne
            #to biorę wieksza wartosc z ciagow dlg a-1 i b oraz ciagow dlg a i b-1
            else:
                dp[a][b] = max(dp[a-1][b], dp[a][b-1])

    #odtwaram rozwiazanie
    #od tyłu
    lcs = []
    i, j = m,n

    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            lcs.append(A[i-1])
            i-= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs[::-1], dp[m][n]

#CZYTELNIEJSZY ZAPIS
def lcs2(A, B):
    a = len(A)
    b = len(B)
    # slowo A- wiersze, słowo B - kolumny
    dp = [[0] * (b) for _ in range(a)]

    # wypełniam kolumne 0
    for a1 in range(a):
        if A[a1] == B[0]:
            dp[a1][0] = 1

    # wypełniam wiersz 0
    for b1 in range(b):
        if A[0] == B[b1]:
            dp[0][b1] = 1

    for a1 in range(1, a):
        for b1 in range(1, b):

            # jesli el są sobie równe to wynik to pole o kol i wier o 1 mniejszym + 1
            if A[a1] == B[b1]:
                dp[a1][b1] = dp[a1 - 1][b1 - 1] + 1
            # jesli sa rozne to wynik to max z slowa konczacych sie na kol o 1 mniejszej
            # lub wierszu o 1 mniejszym
            else:
                dp[a1][b1] = max(dp[a1 - 1][b1], dp[a1][b1 - 1])

    res = []
    # ustawiam indeksy na sam tył, wynik odtwarzam od tyłu
    a1, b1 = a - 1, b - 1
    while a1 >= 0 and b1 >= 0:
        if A[a1] == B[b1]:
            res.append(A[a1])
            a1 -= 1
            b1 -= 1
        elif dp[a1 - 1][b1] > dp[a1][b1 - 1]:
            a1 -= 1
        else:
            b1 -= 1
    return res[::-1], dp[a - 1][b - 1]


a = [1,9,8,2,5,6]
b = [2,1,8,3,2]

print(LCS(a,b))