#mam n pojemnikow prostokatnych ,kwadratowych umieszczone w 1 cwiartce ukladu wspolzednych
#kazdy pojemnik jest opisany przez wspolrzedne lewego gornego rogu i prawego dolnego
#wiec kazdy pojemnik ma jakąs swoja powierzchnie
#pojemniki sa polaczone rurkami
#sprawdz ile pojemnikow bedzie calkowicie pelnych wiedzac ze nalano x powierzchni wody
#wlewamy wode od gory i splywa ona rownomiernie na sam dol do pojemnikow ktore sa najnizej

#zaczynam od obliczenia powierzchni kazdego pudelka, te pow wpisue do tab
#szukam minimalnej powierzchni
#okreslam wysokosc kazdego pudelka
#szukam h min i h max - czyli wartosci na osi OY od ktorej zaczynaja sie i na ktorej koncza sie pudelka
#strzelam w wartosci srodkowa miedzy hmin a hmax, licze ile powierzchni udalo mi sie zapelnic
#jesli te zapelnione pow =< x - min pow to moge strzelac  w nowy srodek powiedzy obecnym srodkiem a h max
#gdy zapelnione pow > x - min tzn ze juz nie ma szans ze zapelnie jakies cale pojemnniki, wiec sprawdzam ponizej
#dopoki nie osiagne takiej sytuacji ze juz albo nie ma pojemnikow albo curr pow == x - min pow
#wiec sprawdzam ile jest pelnych pod ta linia i to jest moim wynikiem