#wstawianie el na koniec kopca

def heapify(T,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    maxi = i
    if l < n and T[maxi] < T[l]: maxi = l
    if r < n and T[maxi] < T[r]: maxi = r
    if maxi != i:
        T[i],T[maxi] = T[maxi],T[i]
        heapify(T,n,maxi)

def built_heap(T):
    n = len(T)
    for i in range(n//2,-1,-1):
        heapify(T,n,i)
    return T

def heap_sort(T):
    n = len(T)
    built_heap(T)
    for i in range(n-1,0,-1):
        T[i],T[0] = T[0],t[i]
        heapify(T,i,0)

def parent(i):
    return (i-1) // 2

def add_to_heap(T,el,n): #n-dlg obecnie tab
    T[n] = el#na koncu mam 1 puste miejsce
    i = n
    while parent(i) >= 0 and T[i] > T[parent(i)]:
        T[i],T[parent(i)] = T[parent(i)],T[i]
        i = parent(i)

t = [0,8,3,4,5,7,9,1]
heap_sort(t)
print(t)
t1 = [9,8,6,7,5,None]
add_to_heap(t1,8,5)
print(t1)