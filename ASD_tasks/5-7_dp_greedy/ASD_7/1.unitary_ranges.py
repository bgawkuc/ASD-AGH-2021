#przedzialy jednostkowe
#mamy tablice z jakimis wartosciami
#znajdz minimalna ilosc przedzialow jednostkowych tak by pokryly one wszystkie wartosci
#przedzialy jednostkowe to takie np:[0.71;1.71] -> maja zakres 1

#sortuje pkt rosnaco, po początkach
#moj pierwszy predzial: [1pkt;1pkt+1]
#sprawdzam ile pkt on pokryje
#potem znajduje kolejny przedzial zaczynajacy sie od pkt ktory ten ostatni nie pokryl
#i tak w kółko

def ranges(A):
    n = len(A)
    A.sort()
    idx = 0
    cnt = 0

    while idx < n:
        cnt += 1
        end = A[idx] + 1

        while idx < n and A[idx] <= end:
            idx += 1

    return cnt

x = [0.25, 0.3, 1.25, 2.7, 0.1, 0.5, 1.6]
print(ranges(x))
