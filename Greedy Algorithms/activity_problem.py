#Dostaje tablice z krotkami, ktore zawieraja inforamcje kiedy zaczyna sie i konczy dane cwiczenie.
#Znajdź, które ćwiczenia należy wybrać tak, by ich ilość była maksymalna, a żadne 2 nie mogą na siebie nachodzić.

#Sortuje czynnosci po czasie zakonczenia i dodaje do wyniku ćwiczenia, które mają początek większy lub równy od końca ostatnio dodanego.

def activity_problem(T):
    T.sort(key=lambda t: t[1])
    print(T)

    res = [] 
    index = 0
    res.append(T[0]) 

    for i in range(1,len(T)):
        # jesli czas rozpoczecia i-tej czynnosci jest pozniejszy od czasu zakonczenia ostatniej dodanej czynnosci
        if T[i][0] >= T[index][1]: #to go dodaje do listy wynikow
            res.append(T[i])
            index = i

    return res
