#Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
#oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.

#sprawdzam elementy parami, mniej porownan
def minmax(T):
    mini = T[-1] #daje na ost el
    maxi = T[-1]
    for i in range(0,len(T)-1,2):

        if T[i] < T[i+1]: #porownuje elementy parami
            if T[i] < mini: #ten mniejszy jest kandedatem na mini
                mini = T[i]
            if T[i+1] > maxi:
                maxi = T[i+1]

        else: #T[i] >= T[i+1] #wiekszy jest kandydatem na maxi
            if T[i] > maxi:
                maxi = T[i]
            if T[i+1] < mini:
                mini = T[i+1]

    return mini,maxi

print(minmax([7,2,8,4,1,9]))