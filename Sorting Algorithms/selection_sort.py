#sortowanie przez wybieranie
#O(n^2)

#przechodze liniowo po tablicy wybieram i-ty element
#patrze na wszystkie elementy na prawo od niego i szukam tam najmniejszego
#zamieniam element i-ty z najmniejszym znalezionym po jego prawej

def selectionSort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i+1,len(A)):
            if A[mini] > A[j]:
                mini= j

        A[i], A[mini] = A[mini], A[i]

    return A

A = [9,2,7,1,0,3]
print(selectionSort(A))