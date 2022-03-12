# Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie ∣B∣ = log n.
# Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A

# złożoność
#O(n+k) = O(n+logn) = O(n)

from math import ceil, log

def insertionSort(T,l,r):
    for i in range(l+1,r+1):
        el = T[i]
        j = i - 1
        while j >= l and T[j] > el:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = el
    return T

def binarySearch(el,T,l,r):
    mid = r - l // 2
    if l <= r:
        if el == T[mid]:
            return True,mid
        elif el < T[mid]:
            return binarySearch(el,T,l,mid-1)
        else:
            return binarySearch(el,T,mid+1,r)
    return False,None

def uniq(T):
    new = [[] for _ in range(ceil(log(len(T),2)))]
    j = 1
    new[0] = T[0]

    for i in range(1,len(T)):
        x,_ = binarySearch(T[i],new,0,j-1)
        if x == False:
            new[j] = T[i]
            j += 1
            insertionSort(new, 0, j - 1)
        if j == len(new):
            break
    return new

def countingSort(T):
    n = len(T)
    tabUniq = uniq(T)
    new = [None] * len(T)
    cnt = [0] * len(uniq(T))

    for i in range(n):
        _, ind = binarySearch(T[i],tabUniq,0,len(tabUniq)-1)
        cnt[ind] += 1

    for i in range(1,len(tabUniq)):
        cnt[i] += cnt[i-1]

    for i in range(n):
        _, ind = binarySearch(T[i], tabUniq, 0, len(tabUniq) - 1)
        cnt[ind] -= 1
        new[cnt[ind]] = T[i]

    for i in range(n):
        T[i] = new[i]
    return T

t = [3,3,2,4,3,2,2,2,1,4]
print(countingSort(t))