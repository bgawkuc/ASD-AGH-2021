#quicksort uzywajac metody hoare
#w partition mamy dwa wskazniki lewy i prawy
#piwot to 1 element
#lewy przesuwamy w prawo dopoki nie znajdziemy el >= pivota
#prawy przesuwamy w lewo dopoki nie znajdziemy el < pivota
#zamieniamy te 2 el meijscami
#dzialamy dopoki sie nie spotkaja

def partition(T,l,r):
    x = T[l] #pivot
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while T[i] < x: #dopoki lewy nie bedzie >= pivot
            i += 1

        j -= 1
        while T[j] > x: #dopoki prawy nie bedzie <= pivot
            j -= 1

        if i >= j: #gdzie sie spotkaja lub i przegoni j
            return j

        T[i], T[j] = T[j], T[i]
        print(T)


def qsort(T,l,r):
    if l < r:
        q = partition(T,l,r)
        qsort(T,l,q)
        qsort(T,q+1,r)

t = [8,1,0,2,9,6,4,3]
qsort(t,0,len(t)-1)
print(t)