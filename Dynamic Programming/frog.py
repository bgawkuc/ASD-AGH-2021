#Dostajesz na wejściu tablice A. A[i] - wartość przekąski na i-tym polu.
#Żab Zbiegniew znajduje się na polu o indeksie 0 i chce dokończyć na koniec tablicy.
#Skacząc z pola a do b zużywa b-a energii. Każda przekąska dodaje żabie energii.
#Oblicz minimalną ilość skoków jaką żaba potrzebuje, by przebyć trasę

#dp[x][y] - minimalna ilość skoków jaką się dostane na pole x
#kiedy na polu x mam y energii (wliczam zjedzoną przekąske co lezy na x)
#złożoność: O(n^3)

def Zbigniew(A):
    n = len(A)
    inf = float("inf")
    dp = [[inf] * n for _ in range(n)]
    dp[0][A[0]] = 0 
    
    #start,end-indeks na jakim zaczynam i kończe skok
    #startEnergy,endEnergy-ilość energii na polu start i end(po zjedzeniu przekąski z tego pola)
    for end in range(1,n): 
        for start in range(end): 
            for startEnergy in range(end-start,n): 
                endEnergy = startEnergy - (end-start) + A[end]
                
                if endEnergy >= n:
                    endEnergy = n-1

                dp[end][endEnergy] = min(dp[end][endEnergy], dp[start][startEnergy] + 1)

    return min(dp[-1])
