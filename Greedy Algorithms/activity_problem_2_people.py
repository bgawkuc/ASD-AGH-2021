# Dostaje tablice zadań A wypełnioną krotkami, które zawierają informacje na temat początku i końca czynności.
# Sprawdź czy wszystkie czynności mogą zostać zrealizowane przez 2 osoby, jeśli każda osoba może jednocześńie wykonywać
# maksymalnie 1 czynność.

def activities(A):
    n = len(A)
    # kto wykonuje zadanie o indeksie i
    order = [None] * n

    # każda zadanie rozdzielam na 2 krotki - jedna z czasem rozpoczenia, a druga z zakończenia
    T = []
    for i in range(n):
        T.append([A[i][0], i, "start"])
        T.append([A[i][1], i, "end"])

    T.sort(key=lambda a: a[0])

    # status każdej osoby ustalam jako wolna
    p1 = "free"
    p2 = "free"

    for i in range(len(T)):
        if T[i][2] == "start":

            if p1 == "free":
                p1 = "busy"
                order[T[i][1]] = "p1"

            elif p2 == "free":
                p2 = "busy"
                order[T[i][1]] = "p2"

            # gdy obie osoby są zajęte tzn ze nie da sie wykonac wszystkich czynnosci
            else:
                print("impossible")
                return

        else:

            if order[T[i][1]] == "p1":
                p1 = "free"

            elif order[T[i][1]] == "p2":
                p2 = "free"

    return order
