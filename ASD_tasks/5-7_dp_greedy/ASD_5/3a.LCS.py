# Mamy dane dwie tablice, A[m] i B[n]. Należy znaleźć ich najdłuższy wspólny podciąg.

#tworzę tablice dp 2d, rozmiaru długość słowa A na długość słowa B
#dp[a][b]- dlg max wspolnego podciagu jaki sie da uzyskac patrzac na litery o indeksach od 0 do a w A i od 0 do b w B

def lcs(A, B):
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

            # jesli litery pod indeksem a1 i b1 są takie same
            if A[a1] == B[b1]:
                dp[a1][b1] = dp[a1 - 1][b1 - 1] + 1
            # jesli sa rozne
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
    
    return res[::-1]
