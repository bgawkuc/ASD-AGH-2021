#sortowanie bąbelkowe
#zlozonosc O(n^2)

#wybieram sobie i-ty element z tablicy po kolei
#tworze zakres od 0 do len(A) - i - 1
#z ktorego wybieram elementy j
#sprawdzam czy A[j] > A[j+1] -> czy wiekszy element stoi przed mniejszym
#jesli tak to zamieniam je miejscami

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)- i - 1):
            if A[j] > A[j+1]:
                A[j+1], A[j] = A[j], A[j+1]
    return A

A = [9,2,0,4,5,7]
print(bubbleSort(A))