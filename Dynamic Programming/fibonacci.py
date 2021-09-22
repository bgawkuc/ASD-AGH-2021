#problem ciagu fibonacciego
#ciag fib(0 po to by miec cos na 0 indeksie): 0,1,1,2,3,5,8,13...
#kazda liczba powstaje jako suma dwoch poprzednich
#tworze tablice w ktorej pod kazdym ind znajduje sie kolejny wyraz ciagu fib
#na koncu sciagam tylko ostatni el
#zlozonosc O(n)

def fib(n): #n - ktory wyraz ciagu fib chce dostac(0 sie nie liczy)
    if n <= 1: #dla wartosci mniejszych od 2
        return n

    T = [-1] * (n+1)
    T[0], T[1] = 0, 1 #wypelniam 0 i 1 wyraz ciagu

    for i in range(2,n+1): #kazdy kolejny jest sumą dwoch poprzednich
        T[i] = T[i-2] + T[i-1]
    return T[n] #pod ind n-tym znajduje sie n-ty wyraz

print(fib(7))



