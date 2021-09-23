#dostaje tablice z krotkami ktore zawieraja inf o ktorej zaczyna sie i konczy dane cwiczenie
#sprawdz ile da sie najwiecej ich zrobic jesli zadne nie moga sie odbywac rownoczesnie

#zlozonosc O(nlogn)
#sortuje moje czynnosci po czasie zakonczenia
#dodaje do tab czynnosc ktora zakonczy sie najwczesniej
#przechodze w petli po kolejnych krotkach
#jesli czas rozpoczecia czynnosci wybranej w petli >= czasu zakonczenia ostatniej czynnosci
#to moge dodac taką czynnosc bo nie bedzie mi kolidowala


def activity_problem(T):
    T.sort(key=lambda t: t[1])
    print(T)

    res = [] #tablica wynikow
    index = 0 #index dla krotek z res
    res.append(T[0]) #dodaje czynnosc ktora ma 1 czas zakonczenia

    for i in range(1,len(T)):
        # jesli czas rozpoczecia i-tej czynnosci jest pozniejszy od czasu zakonczenia ostatniej dodanej czynnosci
        if T[i][0] >= T[index][1]: #to go dodaje do listy wynikow
            res.append(T[i])
            index = i

    return res

t1 = [(8, 12), (2, 13), (12, 14),(1, 4), (3, 5), (0, 6), (6, 10), (8, 11),(5, 7), (3, 8), (5, 9)]
print(activity_problem(t1))