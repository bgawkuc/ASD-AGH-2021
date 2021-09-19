#sortowanie przez kopcowanie
#O(nlogn)

#buduje kopiec poprzez wykonanie heapify dla calej listy od konca do pocztku
#przechodze po liscie od konca
#biore i-ty element, zamieniam go z tym co jest na idx 0
#wykonuje heapifyMax gdzie rodzica ustawiam na 0 a rozmiar tablicy n = i
#po przejsciu tablicy mam posortowany zbiór liczb
#skoro jest to heapifyMax -> sortuje rosnąco
#dla heapifyMin -> sortuje malejąco


#O(logn)
#gdy chce sortowac rosnąco
def heapifyMax(A,i,n): #i-rodzic
    l = 2 * i + 1 #lewe dziecko
    r = 2 * i + 2  #prawe dziecko
    maxi = i #maksymalna wartosc jest na początku w rodzicu

    #szukam najwiekszej wartosci dla indeksow l,r,maxi(rodic)
    if l < n and A[l] > A[maxi]:
        maxi = l
    if r < n and A[r] > A[maxi]:
        maxi = r

    # gdy najwieksza wartosc jest w dziecku
    if maxi != i:
        A[i], A[maxi] = A[maxi], A[i] #dziecko i rodzica zamieniam miejscem
        heapifyMax(A,maxi,n)


#O(logn)
#gdy chce sortowac malejąco
def heapifyMin(A,i,n):
    l = 2 * i + 1
    r = 2 * i + 2
    mini = i

    if l < n and A[l] < A[mini]:
        mini = l
    if r < n and A[r] < A[mini]:
        mini = r

    if mini != i:
        A[i], A[mini] = A[mini], A[i]
        heapifyMin(A,mini,n)


#buduje kopiec na bazie tablicy A
def bulitHeap(A):
    n = len(A)
    for i in range(n,-1,-1):
        heapifyMax(A,i,n)
    return A


def heapSort(A):
    n = len(A)
    bulitHeap(A)
    #wyciagam i-ty el z kopca, daje go na początek obecnej listy
    #wykonuje heapifyMax(sortowanie rosnąco)
    for i in range(n-1,0,-1):
        A[i], A[0] = A[0], A[i]
        heapifyMax(A,0,i) #i = 0; n = i
    return A


#O(logn)
#zamienia minHeap w maxHeap
def min2maxHeap(A):
    n = len(A)
    i = (n - 2) // 2
    while i >= 0:
        heapifyMax(A,i,n)
    return A


#O(logn)
#zamienia maxHeap w minHeap
def max2minheap(A):
    n = len(A)
    i = (n - 2) // 2
    while i >= 0:
        heapifyMin(A,i,n)
    return A

#O(logn)
#usuwa minimum z minHeap
def deleteMin(A):
    A[0] ,A[-1] = A[-1], A[0]
    A.pop()
    heapifyMin(A,0,len(A))


#usuwa maksimum z maxHeap
def deleteMax(A):
    A[0], A[-1] = A[-1], A[0]
    A.pop()
    heapifyMax(A,0,len(A))


def parent(i):
    return (i-1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


#O(logn)
#dodaje el do minHeap
def addToMinHeap(A,el):
    A.append(el)
    l = len(A) - 1
    #dopoki rodzic jest wiekszy od dziecka
    while parent(l) >= 0 and A[l] < A[parent(l)]:
        A[parent(l)], A[l] = A[l], A[parent(l)]
        l = parent(l)


#dodaje el do maxHeap
def addToMaxHeap(A,el):
    A.append(el)
    l = len(A) - 1
    #dopoki rodzic jest mniejszy od dziecka
    while parent(l) >= 0 and A[l] > A[parent(l)]:
        A[parent(l)], A[l] = A[l], A[parent(l)]
        l = parent(l)



A = [9,8,0,2,4,6,1]
print(heapSort(A))
