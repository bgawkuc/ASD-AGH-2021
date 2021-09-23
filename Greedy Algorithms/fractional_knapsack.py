#problem plecakowy ale mozna brak ulamkowe części

#na podstawie tablicy wag i profitow obliczam zysk/1kg
#sortuje po najwiekszych takich wartosciach
#sprawdzam czy da sie wziac caly rzedmiot o obecnym max zysku/kg
#jesli tak to go biore
#jak nie to sprawdzam ile kg jego da sie wybrac to biore

def knapsack(W,P,maxW):
    n = len(W)
    A = [[0] * 2 for _ in range(n)]

    for i in range(n):
        A[i][1] = i
        A[i][0] = P[i]/W[i] #zysk za kg

    A.sort(key= lambda x: x[0],reverse=True) #sortuje wg 1 el malejaoa, czyli jeso pos od max zysk/kg
    print(A)

    p = 0.0

    for i in A:#biore przedmioty od tych po max zysku/kg

        if maxW > 0: #gdy mam miejsce w plecaku
            idx = i[1] #indeks przedmiotu z wejsciowej tab

            if W[idx] <= maxW: #gdy da sie zabrac caly przedmiot
                p += P[idx]
                maxW -= W[idx]

            else: #gdy caly przedmiot sie nie miesci
                p += maxW * (P[idx]/W[idx])
                maxW = 0
    return p

P = [1,2,3,4]
W = [6,5,4,2]
print(knapsack(W,P,8)) #biore caly przedmiot o Proficie 4 oraz 3 oraz 2kg * (2/5=0.4) czyli zysk: 7.8