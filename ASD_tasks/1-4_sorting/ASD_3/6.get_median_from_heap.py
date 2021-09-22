# Proszę przedstawić W jaki sposób zrealizować strukturę danych, która pozwala wykonywać
# operacje: 2. RemoveMedian (wyciągnięcie mediany).

#Tworzę 2 kopce: min i max. Dodaje elementy z listy do min. Jeśli rozmiar min będzie o 2 większy od max to
#usuwam najmniejszy element z min i dodaje go do max. 
#Wynikiem będzie najmniejszy element w kopcu min (lub najmniejszy w kopcu min i największy w kopcu max).

def heapifyMin(A, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    mini = i

    if l < n and A[l] < A[mini]:
        mini = l
    if r < n and A[r] < A[mini]:
        mini = r

    if mini != i:
        A[mini], A[i] = A[i], A[mini]
        heapifyMin(A, mini, n)

def deleteMin(A):
    A[0] ,A[-1] = A[-1], A[0]
    mini = A[-1]
    A.pop()
    heapifyMin(A,0,len(A))
    return mini, A

def parent(i):
    return (i-1) // 2

def addToMinHeap(A,el):
    A.append(el)
    l = len(A) - 1
    while parent(l) >= 0 and A[l] < A[parent(l)]:
        A[parent(l)], A[l] = A[l], A[parent(l)]
        l = parent(l)


def addToMaxHeap(A,el):
    A.append(el)
    l = len(A) - 1
    while parent(l) >= 0 and A[l] > A[parent(l)]:
        A[parent(l)], A[l] = A[l], A[parent(l)]
        l = parent(l)


def getMedian(A):
    minHeap, maxHeap = [], []

    for i in range(len(A)):
        #dodaje element do kopca min
        addToMinHeap(minHeap, A[i]) 

        #gdyby wielksoc kopca min była o 2 wieksza od kopca max to najmniejszy el z min przenosze do max
        if len(minHeap) - len(maxHeap) >= 2:
            mini, minHeap = deleteMin(minHeap)
            addToMaxHeap(maxHeap, mini)


    if len(minHeap) == len(maxHeap):
        return maxHeap[0], minHeap[0]

    elif len(minHeap) > len(maxHeap):
        return minHeap[0]
