#mam formułe logiczną w postaci CNF
#czyli jest to koniunkcja klauzul
#a kazda klauzula sklada sie z alternatywy iterałów
#formuła spełnia wartosc taką ze kazdy iterał
#wystepuje w niej dokładnie 2 razy: raz z negacją i raz bez niej
#znajdz rozwiazanie tej formuły

#tworze graf dwudzielny
#po lewej stronie znajdują się iterały(bez negacji)
#a po prawej wszystkie klauzule
#miedzy iterałem a klauzulą stawiam krawedź gdy iterał występuje w klauzuli
#niezaleznie od tego czy jest on z zaprzeczeniem czy bez
#po stworzeniu grafu szukam w nim max skojarzenia
#gdy je znajde to patrze na jego krawedzie i jakie on wierzchołki tworzy:
#gdy iterał w klauzuli jest bez negacji to otrzymuje 1
#gdy jest z negacją to otrzymuje 0
#gdy rozmiar max skojarzenia wynosi tyle co ilosc klauzl tzn ze graf posiada rozwiązanie