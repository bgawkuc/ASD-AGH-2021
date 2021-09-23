#problem z aktywnosciami
#tylko wykonuje je dwie osoby
#czy dadza one rade wykonac wszystkie czynnosci
#dwie osoby nazywam je p1,p2
#zwraca mi kolejnosc ktora aktywnosc wykonuje ktora osoba

#do tablicy wpisuje czas rozpoczecia,nr czynnosci, start(tzn ze sie zaczyna)
#do tablicy wpisuje czas zakonczenia,nr czynnosci, end(tzn ze sie konczy)
#ustawiam status obu osob na free
#przechodze liniowo po tab i sprawdzam pole tab[i][2] (status start/end)
#gdy jakas czynnosc ma status start to szukam wolnej osoby
#daje tej osobie status busy i wpisuje jej inicjaly do tabeli koelejnosc
#gdy trafie na status busy to sprawdzam kto robil to zadanie(kazde zadanie ma swoj numer) i znowu mu daje status free
#i tak dopoki nie przejde wszystkich czynnosci

def activities2(A):
    n = len(A)
    order = [None] * n #odpowiednio ktore zadanie robi osoba p1/p2 patrzac na wejsciowa tablice
    T = []

    for i in range(n): #dodaje do times osobno czas rozp,nr zad i start(czyli sie zaczyna) oraz analogicznie z czasem zakonczenia
        T.append([A[i][0],i,"start"]) #(poczatek,idx zad,start)
        T.append([A[i][1],i,"end"]) #(koniec,idx zad,end)

    T.sort(key=lambda a:a[0]) #sortuje po czasach
    print(T)

    #free-wolna, busy-zajeta
    p1 = "free"
    p2 = "free"

    for i in range(len(T)): #przegladam po kolei elementy

        if T[i][2] == "start": #gdy zaczyna sie czynnosc szukam wolnej osoby

            if p1 == "free": #jesli jest wolny
                p1 = "busy"
                order[T[i][1]] = "p1"

            elif p2 == "free":
                p2 = "busy"
                order[T[i][1]] = "p2"

            else: #gdy obie osoby są zajęte tzn ze nie da sie wykonac wszystkich czynnosci
                print("impossible")
                return

        else: #gdy czynnosc sie konczy(=end) to ta osoba ktora wykonywala czynnosc dostaje znowu status free

            if order[T[i][1]] == "p1":
                p1 = "free"

            elif order[T[i][1]] == "p2":
                p2 = "free"

    return order


x = [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]
print(activities2(x))
