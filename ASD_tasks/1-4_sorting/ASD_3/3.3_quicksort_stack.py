#quicksort ze stosem
#z uzyciem pop i append (pop sciaga ostatni el ze stosu)

def partition(T,l,r):
    pivot = T[r]
    i = l
    for j in range(l,r):
        if T[j] <= pivot:
            T[i],T[j] = T[j],T[i]
            i += 1
    T[i],T[r] = T[r],T[i]
    return i

#zajmuje tylkon O(logn) pamieci dzieki temu ze dzialam najpierw tylko na mniejszym przedziale a potem na wiekszym
def qsort(T):
    S = []
    n = len(T)
    l = 0
    r = n - 1
    S.append((l,r))
    while len(S) > 0:
        (l,r) = S.pop()
        if l < r:
            q = partition(T,l,r)
            if q - l < r - q: #gdy lewa czesc jest mniejsza
                S.append((q+1,r)) #najpierw dodaje krotke z prawej czesci
                S.append((l,q-1)) #potem dodaje krotke mniejszego przedialu
                # bo to ja sciagne ze stosu i dla niej mam dzialac
            else:
                S.append((l,q-1))
                S.append((q+1,r))

t = [9,2,8,7,1,0]
qsort(t)
print(t)