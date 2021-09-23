#problem szeregowania zadan
#kazde zadanie jest pidane jako przedzial poczatek-koniec
#wybierz jak najliczniejszy zbior zadan tak by zadne 2 nie nachodzily sie

#wybieram przedzial ktory konczy sie najwczesniej
#poprawne rozumowanie
#zloznosc O(nlogn)

#dowod poprawnosci algorytmu:->dowod nie w prost
#rozwazmy 1 moment w ktorym nasz algorytm dokonal wyboru
#uniemozliwiajacego wyboru skonstruowania optymalnego rozwiazania
#1 przedzial wybrany ptrzez nasz alg
#mozemy wybrac tez najwczesniejszy przedzial(rozw opt( z jaiegos rozw optymalnego
#te dwa przedzialy musza sie przecinac bo inaczej rozw algorytmu byloby dluzsze
#tworzymy nowe rozw przez wyciecie 1 przedzialu z rozw opt
#i zastepujemy go przedzialem wybranym przez algorytm
#dochodzimy do sprzecznosci czyli alg jest poprawny

