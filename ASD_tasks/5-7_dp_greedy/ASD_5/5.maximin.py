#mamy tablice z wartosciami
#kazda wartosc to ilosc h jakie musi poswiecic robotnik na pomalowanie domu
#mamy k robonikow
#robotnik moze pomalowac tylko domy znajdujace sie kolo siebie(spojny podciag)
#znajdz jak najbardziej sprawiedliwy podzial pracy tak by robotnicy potrzebowali
#mozliwie jak najbardziej równą ilosc godzin
#zwroc najmmniejsza z tych ilosci godzin
#f(i,T) -max wart podzialu a1,...,ai T pracownikow
#o-indeks od jakiego zaczyna dany pracownik
#f(i,t) = min(f(i-o,t-1),suma[(od j = o + 1, do i) aj])
