#wybor zadan z terminala
#mam zadanie do wykonania
#kazde z nich znajduje sie w 3 elementowej tablicy
#ktora zawiera nr zadania, deadline, profit
#gdy jakies zadanie uda mi sie wypelnic przed uplywem deadline to otrzmuje za nia profit
#znajdz zadania ktore sie da zrobic tak by zysk byl mozliwie jak najwiekszy

#sortuje zadania po zysku od najwiekszych do najmniejszych
#szukam max deadline
#tworze tab o jego rozmiarze
#przechodze po tab wejsciowej
#patrze na deadline pierwszego i umieszczam go na miejsce o ind deadline - 1(ostatni moment w ktorym da sie wykonac zad
#by dostac za niego zysk)
#gdyby to nie bylo mozliwe to szukam od miejsca deadline - 1 w dol pustego miejsca
#gdtby takiego miejsca nie bylo tzn ze nie da sie umiescic takiego obiektu
#zlozonosc o(n^2)

# def profit(el):
#     return el[2]

def jobs(A):
    n = len(A)
    A.sort(key=lambda a: a[2],reverse=True) #sortuje po profitach malejaco

    maxDeadline = A[0][1] #szukam najw deadline
    for i in range(1,n):
        if A[i][1] > maxDeadline:
            maxDeadline = A[i][1]

    tasks = [None] * maxDeadline #tworze tablice o rozm maxdealine

    for i in range(n):
        lastMoment = A[i][1] - 1 #ostatni moment w ktorym da sie zaczac zadanie by zyskac za nie profit

        for j in range(lastMoment,-1,-1): #szukam miejsca by umiescic zadanie, staram sie je umiescic jak najdalej

            if tasks[j] == None: #gdy ten moment jest wolny to umieszczam zadanie
                tasks[j] = A[i][0]
                break

    return tasks #zwracam liste nr zadan ktore udalo mi sie zrobic


#zadania: (nr zad, max czas zakonczenia, profit)
b = [(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25),
     (6, 2, 20), (7, 5, 8), (8, 7, 10), (9, 4, 12), (10, 3, 5)
    ]
print(jobs(b))