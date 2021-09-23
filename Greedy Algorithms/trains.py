#mamy tablice pociagow
#dla kazdego pociagu mamy informacje na temat h przyjazdu i odjazdu
#mamy sprawdzic czy stacja majac m peronow jest w stanie obsluzyc wszystkie pociagi
#tzn aby kazdy pociag mial peron w czasie od przybycia do odjazdu

#sortuje pociagi po godzinach przybycia
#na perony wpuszczam m pierwszych pociagow
#zaczynam sprawdzac kolejne pociagi
#gdy dla i-tego pociagu jego czas przyjazdu >= od czasu odjazdu j-tego pociagu to wpuszczam go na jego peron
#gdy po sprawdzeniu wszystkich peronow nie znajde wolnego dla j tego pociagu to zwracam False


def arrival(el):
    return el[0]

def trains(A,m):
    n = len(A)
    if n <= m: return True

    A.sort(key=arrival) #sortuje po czasach przybycia

    platform = [None] * m

    for i in range(m): #pierwsze m pociagow wpuszczam na perony
        platform[i] = A[i]

    for i in range(m,n): #kolejne pociagi
        possible = False

        for j in range(m): #kolejne perony

            if platform[j][1] <= A[i][0]: #jesli czas odjazdu pociagu ktory stoi na peronie jest <= przyjazdu kolejnego
                platform[j] = A[i]
                possible = True
                break #bo znalazlam peron dla tego pociagu

        if possible == False:
            return False

    return True

a = [(2.00, 2.30), (2.40, 3.20), (3.10,3.12), (3.13,4.40), (3.20,4.00), (4.00,5.20)]
print(trains(a,2))