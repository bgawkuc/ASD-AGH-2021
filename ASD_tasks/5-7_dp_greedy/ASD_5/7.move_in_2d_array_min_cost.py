#dostajemy tablice mXn wypelniona watrosciami(koszt wejscia)
#znajdz minimalny koszt z dostania sie z [0][0] do [m-1][n-1]
#mozna poruszac sie tylko w bok lub dol
#wszystkie koszty sa dodatnie

#f(i,j) - minminalny koszt by dojsc na pole T[i][j]
#f(i,j) = min{f(i-1,j), f(i,j-1)} + T[i][j]
#w 0 wierszu moge poruszac sie tylko w prawo a w 0 kol tylko w dół
#tworze sobie tablice res o rozm m na n w ktrej bede zapisywac wyniki
#0 kolumne wypelniam wartosciami z 0 kol z wejsciowej tab
#analogicznie robie z 0 wierszem i potem uruchamiam funkcje
#przechodze wierszami potem po tablicy res
#wynik jest na polu res[m-1][n-1]
#metoda  bottom up

#res[i][j] to koszt dojscia na pole i,j
#wynosi i tyle co pole w macierzy C[i][j] + koszt z pola z którego przyszłam
#koszta pól z których mogłam przyjść:
#wiersz 0 moge zapelnic jedynie ruchem z lewej do prawej
#kolumne 0 moge zapelnic jedynie ruchem z gory na doł
#reszta pól to min z pola po lewej i pola po prawej + koszt pola

def chessboard(C):
    m = len(C)
    n = len(C[0])
    res = [[0] * n for _ in range(m)]

    # w wierszu 0 mam tylko 1 rodzaj ruchu
    for j in range(n):
        res[0][j] = res[0][j-1] + C[0][j]

    # w kolumnie 0 mam tylko 1 rodzaj ruchu
    for i in range(m):
        res[i][0] = res[i-1][0] + C[i][0]


    for i in range(1,m): #wiersze
        for j in range(1,n): #kolumny
            res[i][j] = min(res[i-1][j],res[i][j-1]) + C[i][j] #biore min z pole na lewo i pola u góry + koszt pola i,j

    for i in range(m):
        print(res[i])

    return res[m-1][n-1]

t = [[9, 1, 1],
     [2, 2, 1],
     [2, 2, 1]]
m = [
    [4,7,8],
    [2,1,1],
]
print(chessboard(t))