#zanelezienie mediany w tablicy za pomoca 2 kopcow min i max heap
#zloznosc o(logn)

#tworze 2 kopca: minHeap i maxHeap
#przechodze liniowo po tablicy
#dodaje el do minHeap O(logn)
#jesli rozmiar min heap jest wiekszy od rozmiaru maxHeap o 2
#to usuwam najmniejszy element z minHeap(O(n)) i dodaje go do maxHeap(O(n))
#na sam koniec:
#jesli rozmiary kopcow sa rowne to mediany są dwie: minimum z minHeap i maksimum z Maxheap
#a jesli rozmiar minHeap jest wiekszy to medianą jest jego minimum
#algorytm ma zlozonosc O(nlogn) -> przejscie po tablicy i tworzenie kopców


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


#usuwa minimum z minHeap
def deleteMin(A):
    A[0] ,A[-1] = A[-1], A[0]
    mini = A[-1]
    A.pop()
    heapifyMin(A,0,len(A))
    return mini, A


def parent(i):
    return (i-1) // 2


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


def getMedian(A):
    minHeap, maxHeap = [], []

    for i in range(len(A)):
        addToMinHeap(minHeap, A[i]) #dodaje element do kopca min

        #gdyby wielksoc kopca min była o 2 wieksza od kopca max to najmniejszy el z min przenosze do max
        if len(minHeap) - len(maxHeap) >= 2:
            mini, minHeap = deleteMin(minHeap)
            addToMaxHeap(maxHeap, mini)


    if len(minHeap) == len(maxHeap):
        return maxHeap[0], minHeap[0]

    elif len(minHeap) > len(maxHeap):
        return minHeap[0]

    else:
        return maxHeap[0]

A = [0,5,9,1,3,6,7]

print(getMedian(A))

