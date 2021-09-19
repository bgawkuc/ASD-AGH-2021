#sortowanie przez wstawianie
#złożoność O(n^2)

#iteruje po wejsciowej tablicy
#ustawiam el na wartosc obecengo pole
#j ustawiam na idx o 1 mniej
#dopoki el jest mniejszy od A[j] oraz j >= 0
#to na pole A[j+1] wstawiam wartosc A[j]
#i zmniejszam idx j o 1
#gdy warunek przestanie byl spelniony to dobry moment by wstawic el
#A[j+1] = el
#i powtorka w pętli dla nowego elementu

#działa to tak
#dopoki znajde cos wiekszego od el
#to na idx j + 1 wstawiam pole j
#tak jakby "przesuwam je w prawo"
#i to powtarzam dopoki nie trafie na mniejszy element
#wtedy za tym mniejszym (j+1) wstawiam mój

def insertionSort(A):
    for i in range(1,len(A)):
        el = A[i]
        j = i - 1
        while el < A[j] and j >= 0:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = el
    return A

A = [2,8,3,0,7,3,1]
print(insertionSort(A))