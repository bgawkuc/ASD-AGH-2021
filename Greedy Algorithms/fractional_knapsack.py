#Problem plecakowy, w którym można brać ulamkowe części przedmiotów.

#Na podstawie tablicy wag i profitow obliczam zysk/1kg i sortuje tablice po najwiekszych takich wartosciach.
#Patrząc na taką tablice staram się wybierać całe przdmioty, gdy nie będzie to możliwe to biorę część przedmiotu.
#Wybieram przedmioty zaczynając od maksymalnego zysku za 1kg.

def knapsack(W,P,maxW):
    n = len(W)
    A = [[0] * 2 for _ in range(n)]

    for i in range(n):
        A[i][1] = i
        A[i][0] = P[i]/W[i] #zysk za kg
    
    #sortuje po wartości zysk/kg malejąco
    A.sort(key= lambda x: x[0],reverse=True)

    p = 0.0

    for i in A:
        if maxW > 0: 
            idx = i[1]
            
            #gdy da sie zabrac caly przedmiot
            if W[idx] <= maxW: 
                p += P[idx]
                maxW -= W[idx]
            
            #gdy caly przedmiot sie nie miesci
            else: 
                p += maxW * (P[idx]/W[idx])
                return p
