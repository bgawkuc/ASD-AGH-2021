#dana jest posortowana tablica oraz liczba x.
#proszę napisać program, który stwierdza czy istnieją indeksy i oraz j
#takie, że A[i] + A[j] = x.

#ustawiam i na poczatkowy idx a j na koncowy idx
#jesli idx i >= j to zwracam False
#jesli suma A[i] + A[j] jest mniejsza od x to zwiekszam idx i
#jesli suma A[i] + A[j] jest wieksza od x zmniejszam idx j
#jesli suma A[i] + A[j] jest rowna x to zwiacam A[i] oraz A[j]


def exist(A,i,j,x):
    if i >= j:
        return False
    if A[i] + A[j] > x: #gdy suma jest za duza to z prawej zmniejszam zakres
        return exist(A,i,j-1,x)
    elif A[i] + A[j] < x: #gdy suma jest za mala to z lewej zwiekszam zakres
        return exist(A,i+1,j,x)
    else :
        return A[i], A[j]

t = [1,3,4,8,11]

print(exist(t,0,len(t)-1,12))
