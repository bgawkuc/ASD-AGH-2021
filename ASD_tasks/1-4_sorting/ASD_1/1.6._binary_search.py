#Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną
#niemalejąco tablicę A o rozmiarze n oraz liczbę x i sprawdza,
#czy x występuje w A. Jeśli tak, to
#zwraca najmniejszy indeks, pod którym x występuje.

def binarySearch(T,i,j,x):
    if i > j:
        return None
    c = (i+j) // 2
    if T[c] == x:
        res = binarySearch(T,i,c-1,x)
        if res == None:
            return c
        return res
    elif T[c] > x:
        return binarySearch(T,i,c-1,x)
    else:
        return binarySearch(T,c+1,j,x)

t = [0,1,2,3,3,3,4]
for i in range(len(t)):
    print(i,binarySearch(t,0,len(t)-1,t[i]))