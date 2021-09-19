#sortowanie kubełkowe
#zlozonosc O(n) dla rozkladu jednostajnego

#tworze tyle kubełków co rozmiar tablicy
#przechodzę liniowo po tablicy
#ustalam idx kubełka do którego chce wrzucić element A[i]:
#szukam min i  max wartosci w A
#idx kubełka to : int( ( (A[i]-mini) / ((maxi-mini) * (n)) ) lub int( ( (A[i]-mini) / ((maxi-mini) * (n)) ) - 1
#drugi wzór zachodzi jedynie dla wartości max w tablicy
#potem przechodze liniowo po kubełkach i sortuje je insertionSortem
#znowu przechodze liniowo po kubełkach i dodaje ich zawartosc po kolei do wyniku

def insertionSort(A):
    for i in range(1,len(A)):
        el = A[i]
        j = i - 1
        while j >= 0 and el < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = el


def bucketSort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    maxi = max(A) #max wartosc w A
    mini = min(A)
    r = (maxi - mini) / n

    #dla przedzialu 1 elementowego, albo w którym wszystkie liczby sa taie same
    #nie ma czego sortowac
    if r == 0:
        return A

    for i in range(n):
        d = (A[i] - mini) / r - int((A[i] - mini) / r)

        if d == 0 and A[i] != mini:
            bucketIdx = int((A[i] - mini) / r) - 1
        else:
            bucketIdx = int((A[i] - mini) / r)

        buckets[bucketIdx].append(A[i])

    output = []

    for i in range(n):
        insertionSort(buckets[i])
        output.extend(buckets[i])

    #dłuższy zapis, robi to samo
    # for i in range(n):
    #     insertionSort(buckets[i])
    #
    # output = []
    # print(buckets)
    #
    # for i in range(n):
    #     for j in range(len(buckets[i])):
    #         output.append(buckets[i][j])

    return output

A = [6,8,9,2,4,3,2,2,3,6,7,9,2]
A1 = [6,7,8]
print(bucketSort(A))
