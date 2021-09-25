#zaba porusza sie po osi liczbowej
#chce ona dostac sie z pola o ind 0 do n - 1
#na kazdym polu stoi przekaska o jakiejs wartosci energetycznej
#skok z pola j na i kosztuje ją i - j energii
#trafiajac na jakies pole zjada przekaske ktora tam jest
#oblicz min ilosc skokow by zaba dostala sie na pole o ind n - 1
#a jej energia nigdy nie moze spasc ponizej 0

#tworze tablice dp[n][n] zapełnioną inf
#dp[x][y] min ilosc skokow gdy dostane sie na pole x i zostanie mi y energii

#mam 3 pętle
#pętla z end -> idx pola na jakie chce skoczyc [od 1 do n - 1]
#pętla z start -> pole z jakiego skacze [od 0 do i-1]
#pętla z startEnergy -> ilosc energii jaką posiada żaba na polu end [od end-start do n - 1]; od  end-start bo jakby było mniej to skok nie byłby możliwy

#endEnergy - > ilosc energii jaka mi zostanie gdy wykonam skok z pola j na i mając k energii
#endEnergy = startEnergy - (end-start) + A[end] (ilosc energii jaką posiada na polu end - koszt skoku + dodatek energii z pola end)
#czyli jesli endEnergy < n
#to dp[end][endEnergy] -> min liczba skoków by się dostać na pole end mając endEnergy energii
#dp[end][Energy] = min(dp[end][endEnergy]; dp[start][startEnergy] + 1)
#minimalna ilosc skokow to min z ostatniego wiersza

import math

def zbigniew(A):
        n = len(A)
        #min ilosc skokow by dostac sie na pole end(wiersz) majac endEnergy na nim(kolumna)
        dp = [[math.inf] * n for _ in range(n)]
        dp[0][A[0]] = 0


        for end in range(1,n): #pole na jakie chce skoczyc
            for start in range(end): #pole z jakiego skacze
                for startEnergy in range(end-start,n): #ilosc energii na polu start

                    endEnergy = startEnergy + A[end] - (end-start) #ilosc energii na polu end po zjedzeniu przekaski

                    if endEnergy < n: #czy nie jest za duzo tej energii
                        dp[end][endEnergy] = min(dp[end][endEnergy],dp[start][startEnergy]+1)

        return min(dp[-1])


A = [2,2,1,1,1,0]
print(zbigniew(A))
