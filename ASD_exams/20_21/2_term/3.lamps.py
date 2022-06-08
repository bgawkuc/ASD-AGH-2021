# mam zestaw n lampek
# kazda lampka posiada przycisk którego wciśnięcie zmienia jej kolor
# odpowiednio: zielony-> czerowny-> niebieski-> zielony... (i tak w kółko)
# dostaje tablice m przedziałów, w numerach lampek zawartych w przedziale wciskam przyciski
# określ jaka maksymalna liczba lampek w danym momencie świeciła sie na niebiesko
# na poczatku wszystkie lampki świecą sie na zielono

# n-ilosc lampek
# A-lista przedziałów
def lamps(n, A):
    color = [0] * n
    currBlue = maxBlue = 0

    for i in range(len(A)):
        for j in range(A[i][0], A[i][1] + 1):

            if color[j] == 0:
                color[j] = 1

            # gdy zmieniam na niebieski
            elif color[j] == 1:
                color[j] = 2
                currBlue += 1

            # gdy zmieniam z niebieskiego
            elif color[j] == 2:
                color[j] = 0
                currBlue -= 1

        maxBlue = max(maxBlue, currBlue)

    return maxBlue


# 6
A = [(7, 8), (2, 5), (2, 5), (6, 8), (5, 8), (9, 9), (7, 7), (1, 3), (9, 9), (7, 9)]
print(lamps(10, A))
