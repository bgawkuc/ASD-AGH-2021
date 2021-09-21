#sortowanie przez wybieranie
#O(n^2)

def selectionSort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i+1,len(A)):
            if A[mini] > A[j]:
                mini= j

        A[i], A[mini] = A[mini], A[i]

    return A
