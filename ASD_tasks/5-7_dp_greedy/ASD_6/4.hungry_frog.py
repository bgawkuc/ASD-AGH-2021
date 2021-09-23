# Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
# wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
# jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
# niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
# dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
# skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
# każdej z liczb.

#dp[x][y] - minimalna ilość skoków jaką się dostane na pole x
#kiedy na polu x mam y energii (wliczam zjedzoną przekąske co lezy na x)
#złożoność: O(n^3)

def frog(A):
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
