#Dostajesz na wejściu tablicę A, która zawiera krotki z informacjami na temat godziny przyjazdu i odjazdu pociągu.
#Na dworcu znajduje się m peronów. Każdy pociąg musi wjechać na peron o swojej godzinie przyjazdu oraz wyjeżdza
#z niego o godzinie wyjazdu. Sprawdź czy m peronów to wystarczająca ilość dla pociągów z tablicy A.

def trains(A,m):
    n = len(A)
    #gdy peronów jest więcej niż pociągów
    if n <= m: return True
    
    #sortuje po czasach przybycia
    A.sort(key=lamda x: x[0]) 

    platform = [None] * m
    
    #pierwsze m pociagow wpuszczam na perony
    for i in range(m):  
        platform[i] = A[i]

    for i in range(m,n):
        #czy znalazłam peron dla pociągu o indeksie i
        possible = False
        
        #przeglądam perony
        for j in range(m):
            
            #jesli czas odjazdu pociagu ktory stoi na peronie j jest <= przyjazdu pociągu o indeksie i
            if platform[j][1] <= A[i][0]: 
                platform[j] = A[i]
                possible = True
                break 

        if possible == False:
            return False

    return True
