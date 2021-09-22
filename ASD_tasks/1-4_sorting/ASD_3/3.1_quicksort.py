#quicksort ktory zuzywa jedynie O(logn) pamieci
#zuzywa tyle pamieci tylko bo najpierw sie zajmujemy max przedzialem dlg n//2
#i potem na kazdym kroku ten przedzail zmniejsza,y dopoki sie nie skonczy
#a potem dopiero zaczynamy robic przedzial drugiej strony od pivota

def partition(T,l,r):
    pivot = T[r]
    i = l - 1
    for j in range(l,r):
        if T[j] <= pivot:
            i += 1
            T[i],T[j] = T[j],T[i]
    i += 1
    T[i],T[r] = T[r],T[i]
    return i

def quicksort(T,l,r):
    while l < r:
        q = partition(T,l,r)
        if q - l < r - q:
            quicksort(T,l,q-1)
            l = q + 1 #lewy indeks idzie za pivota by zaczac teraz wywolywac prawa czesc
        else:
            quicksort(T,q+1,r)
            r = q - 1 #prawy indeks idzie przed pivota by zaczacwywolywav lewa czesc

t = [9,2,1,8,0,2,4,3]
quicksort(t,0,len(t)-1)
print(t)