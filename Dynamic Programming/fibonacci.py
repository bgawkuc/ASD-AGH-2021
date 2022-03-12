# Wypisz n-ty wyraz ciągu Fibonacciego.
# Ciąg Fibonacciego to ciąg liczb, gdzie każda jest sumą dwóch poprzednich.
# Pierwsze dwa elementy to 1 i 1.

def fib(n):
    A = [-1] * n
    A[0], A[1], = 1, 1

    for i in range(2, n):
        A[i] = A[i - 2] + A[i - 1]

    return A[n - 1]
