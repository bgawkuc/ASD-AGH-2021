#kody huffmana
#kod binarny z symbolami rownej dlg nie musi byc optymalny
#symbole   a   b   c   d  e
#wystepow 700 200 120 300 10
#zapis    000 001 010 011 100
#czyli suma 3 * 700 + 3 * 200 + ..+ 3 * 10 = 3990

#inny sposob to zrobienie drzewa - alg zachlanny
#
#        *
#       / \ 1
#      /   * 630
#    0/   / \ 1
#    /  0/   * 350
#   /   /   /  \ 1
#  /   /   /    * 130
# /   /   /    /  \
#a   d   b    c    e
#700 300 200 120  10
#0   10  110 1110  1111
#suma -> 2220

#algorytm zachlanny - weź 2 symbole o najmniejszje czestosci x y
#polacz je w nowy symbol (xy) o czestosci f(xy) = f(x) + f(y)
#usun x, y
#powtarzaj powyzsze az nie zostanie tylko  1 - korzen drzewa
#zloznosc O(nlogn)

#dowod poprawnosci
#T-korzen drzewa
#B(T) koszt drzewa
#B(T) = suma (od s-symbol) f(s) 8 dT(s);
#f(s) czestosc s
#dT(s) dl kodu sumbolu s w dzrewie T

#krok 1: dwa najrzadsze sumbole mozna umiescic we wspolnym wezle
#x,y - dwa najnowsze symbole
#a,b dwa symbole w najdluzszej galezi drzewa
#T-pewne optymalne dzrewo
#T' - drzewo powstale z T przez zamiane a oraz x
#B(T') = B(T) + ((f(a)-f(x))*dT(x) + (-f(a)+f(x)) * dT(a)
#B(T') = B(T) + (f(a)-f(x))*(dT(x)-dT(a))
#                  >= 0       <= 0
#               |________________________|
#                       czyli <= 0
#tworze T'' w ktorym zaminiam b i y
#B(T'') <= B(T') <= B(T)

#krok 2:
#optymalna podstruktura
#mamy drzewo T
#dodajemy na koniev symbole x oraz y
#tak powstaje T'
#czyli B(T') = B(T) + f(x) + f(y)

#te kroki pokazuja poprawnosc algorytmu
#1 krok -> mozna wykonac 1 iteracje algorytmu
#2 krok -> mozemy to zrobic optymalnie
#i tak w kółko