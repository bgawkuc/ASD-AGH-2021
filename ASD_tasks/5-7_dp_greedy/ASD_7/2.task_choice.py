# Mamy dany zbiór zadań A, każde zadanie o indeksie i posiada: numer A[i][0], termin wykonania A[i][1] (liczba naturalna) oraz zysk A[i][2] za wykonanie w
# terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie A[i][0] zostanie
# wykonane przed przekroczeniem swojego terminu A[i][1], to dostajemy za nie nagrodę A[i][2] (pierwsze wybrane
# zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi do maksymalnego zysku.

def task(A):
    n = len(A)
    #sortuje po zyskach malejąco
    A.sort(key=lambda a: a[2],reverse=True) 
    
    #szukam najpóźniejszego terminu wykonania
    maxDeadline = A[0][1]
    for i in range(1,n):
        if A[i][1] > maxDeadline:
            maxDeadline = A[i][1]

    t = [None] * maxDeadline 

    for i in range(n):
        #ostatni moment w ktorym da sie zaczac zadanie by zyskac za nie profit
        lastMoment = A[i][1] - 1 
        
        #szukam miejsca by umiescic zadanie, staram sie je umiescic jak najdalej
        for j in range(lastMoment,-1,-1): 
            #gdy w tym momencie nie zaczyna się inne zadanie
            if t[j] == None: 
                t[j] = A[i][0]
                break
    
    #zwracam liste momentów w jakich trzeba zacząc określone zadania by uzyskac największy zysk
    return t
