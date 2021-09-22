#dostaje na wejsciu string zlozony z liter a-z
#zwroc jego najdluzszy fragment ktory jest palindromem
#palindrom - wyaz czytany od lewej i od prawej brzmi tak samo
#podciag ma byc spojny
#zloznosc o(n^2)

#dp[i][j] czy slowo zaczynajace sie na indeksie i a konczace na indeksie j jest palindromem
#zapełniam najpierw najwiekszą przekątne
#dp[i][j] == True dla i == j bo słowa 1 literowe zawszw są palindromammi
#dp[i][i+1] == True jesli A[i] == A[i+1] bo slowa 2 literowe są palindromamami
#wtw gdy składają sie z tych samych liter

#przechodze teraz pętlami:
#1 petla wyznacza mi dlugosc obecnego slowa - length
#2 petla wyznacza polczatek obecnego slowa l
#r = l + length
#jesli dp[l][r] == True oraz jesli A[l-1] == A[r+1]
#to dp[l-1][r+1] równiez jest palindromem
#wynikiem bedzie zakres l,r w tablicy dp dla ktprych roznica
#miedzy l oraz r jest najwieksza, wartosc wynosi True
#bo to jest najdluzszy palindrom

def palindrome(A):
    n = len(A)
    dp = [['F'] * n for _ in range(n)]
    #najpierw max palindromem lest 1 litera w slowie
    start = end = 0
    l = 1

    #slowa 1literowe są palindromami
    for i in range(n):
        dp[i][i] = 'T'

    #slowa 2literowe są palinromami wtw gdy obie litery są takie same
    for i in range(n-1):
        if A[i] == A[i+1]:
            dp[i][i+1] = 'T'
            #nowy palindrom
            if l < 2:
                start = i
                end = i+2
                l = 2

    #sprawdzam tablice,wyjmuje slowo zaczynajace sie na l i konczace na r
    #jesli slowo to było palindromem i litery l-1 oraz r+1 są równe
    #to slowo od l-1 do r+1 jest rowniez palindromem
    #najdluzszy palindrom znajduje sie na najmnieszej przekatnej
    for length in range(n):
        for l in range(n):
            r = l + length
            if l > 0 and r < n-1:
                #jesli slowo od l do r jest palindromem to
                #jak wezme nową litere z lewej i nową z prawej ktore są rowne to slowo od l-1 do r+1 jest palindromem
                if dp[l][r] == 'T':
                    if A[l-1] == A[r+1]:
                        dp[l-1][r+1] = 'T'
                        if r + 1 - (l - 1) + 1 > l:
                            start = l-1
                            end = r+1
                            l = r+1 -(l-1) + 1

    return A[start:end+1]

A = 'kkokkak'
print(palindrome(A))