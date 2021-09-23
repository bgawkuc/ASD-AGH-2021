#mam ciezarowke o jakiejs pojemnosci k
#oraz pudelka z ktorych kazdy ma przypisana wage
#kazda waga jest jakas potega dwojki
#znajdz minimalna ilosc pudelek tak by wypelnic maksymalnie przyczepe do pojemnosci k

#wystarczy posortowac wagi malejąco
#przechodze od najwiekszej
#i sprawdzam czy nie przekracza ona wagi obecnej
#jesli nie to wybieram to pudelko
#to zadziala dzieki temu ze mam wartosci typu 1,2,4,8,16,32,64
#bo kazda waga jet dwa razy wieksza wiec nie ma mozliwosci by to nie zadzialalo


def loading(A,x):
    n = len(A)
    A.sort() # sortuje tablice A rosnaca
    cnt = 0 #licznik ilosci pudelek
    idx = n - 1 #zaczynam od idx najciezszego pudelka

    while x > 0 and idx >= 0:

        if x >= A[idx]: #gdy wahga pudelka nie przekracza pojemnosci
            cnt += 1
            x -= A[idx]
        idx -= 1

    return cnt

t = [2, 2, 4, 8, 1, 8, 16]
#dla wagi 27 >= 16 + 8 + 2 + 1 -> 4 obiekty
print(loading(t,27))