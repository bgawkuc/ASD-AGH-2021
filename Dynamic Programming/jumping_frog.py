#zab zbigniew skacze po osi liczbowej, ma dostac sie z 0 do n -1
#koszt skoku i do j (j>i) kosztuje go j - i energii
#na niektorych liczbach znajduja sie przekaski ktore dodaja mu energii
#podaj funkcje zbigniew(A) ktora na wejsciu otzrymuje tablice
#z wartosciami przekasek dla odpowiednich indeksow
#zwraca ona minimalna liczbe skokow by zbigniew dotarl do konca
#lub False gdy nie jest to mozliwe

#UWAGA TO JEST DYNAMIK O(n^3) - DA SIĘ LEPIEJ
#dp[x][y] - minimalna ilość skoków jaką się dostane na pole x
#kiedy na polu x mam y energii (wliczam zjedzoną przekoske co lezy na x)
#A-tablica z wartosciami przekąsek

#czyli mam 3 pętle:
#end -> [1,n-1], wybieram idx na jaki chce sie dostac
#end -> [0,end-1], wybieram idx z jakiego robie skok
#startEnergy -> [end-start,n-1], tyle energii mam przed skokiem

#obliczam endEnergy czyli ile będę mieć energii po skoku
#endEnergy = startEnergy - (end-start) + A[end]
#czyli jest to suma energii na polu startowym, zabrany koszt skoku i dodana wart przekaski na end

#dp[end][endEnergy] = min(dp[end][endEnergy]; dp[start][startEnergy]+1)
#wynik to bedzie min w ostatnim wierszu: min(dp[-1])

#LEPIEJ - ZACHŁANNY O(nlogn)
#zaba stoi na polu 0
#ustawiam min iosc skokow na 1 oraz zasieg na wartosc tego pola
#do pq dodaje wszystkie pola ktore są w zasięgu tzn (-wartosc pola,idx pola)
#dodaje z minusem by wyciągac po najwiekszych wartosciach energii
#dopoki zasięg nie będzie większy lub równy n-1:
#wyjmuje krotke (-wartosc pola,idx pola) z pq
#zasieg zwiekszam o abs(wartosc pola)
#ilosc skoków zwiększam o 1
#do kolejki dodaje wszystkie pola, które jeszcze do niej nie trafiły a znajdują się w nowym zasięgu
#na końcu zwracam liczbę skokrów


#ZACHŁANNY O(nlogn)
from queue import PriorityQueue
def zbigniew(A):
    n = len(A)
    #far - zasięg skoku żaby
    far = A[0]
    # ilosc skoków
    cnt = 1

    #gdy z pola o idx 0 doskoczę do końca to wystarczy tylko 1 skok
    if far >= n-1:
        return cnt

    q = PriorityQueue()
    #do pq  dodaje wszystkie pola w zasięgu żaby
    #dodaje z minusem by wyciągac po max energiach
    idx = 1
    while idx < n and idx <= far:
        q.put((-A[idx],idx))
        idx += 1

    #dopoki zasieg zaby jest mniejszy od indeksu ostatniego pola
    while far < n-1:
        #wyjmuje pole z kolejki o max energii, zwiekszam zasięg
        energy,i = q.get()
        far += abs(energy)

        #zwiekszam ilosc skokow
        cnt += 1

        # dodaje do pq wszyskie pola w nowym zasięgu
        while idx < n and idx <= far:
            q.put((-A[idx],idx))
            idx += 1

    return cnt


#DYNAMIK O(n^3)
def zab_Zbigniew(A):
    n = len(A)
    inf = float("inf")
    dp = [[inf] * n for _ in range(n)]
    dp[0][A[0]] = 0 #na pole 0 dostaje sie za pomocą 0 skoków i mam na niej A[0] energii

    for end in range(1,n): #na taki idx pola skacze
        for start in range(end): #z tego pola skacze
            for startEnergy in range(end-start,n): #tyle mam energii na startowym polu
                #tyle mam energii na koncowym polu
                endEnergy = startEnergy - (end-start) + A[end]

                #gdy il energii bedzie za duza to zmniejsze ją
                if endEnergy >= n:
                    endEnergy = n-1

                dp[end][endEnergy] = min(dp[end][endEnergy], dp[start][startEnergy] + 1)

    return min(dp[-1])
#3
A = [2,2,1,1,1,0]
#4
A1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(zab_Zbigniew(A1))
print(zbigniew(A1))