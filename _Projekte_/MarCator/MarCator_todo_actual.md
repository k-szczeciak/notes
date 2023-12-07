
Funkcjonalnosc
- [x] po resecie FA ma sie pojawic nawa i numer wersji
- [ ] opcja HR (needed HW), optymalizacja pomiaru, filter i czestosc sprawdzania bateri
- [ ] opcja 844
- [ ] funkcaje na init_para, fa-para i reset-para, ew on-off-para:
	- 1: po wdraniu programu (tablela init)
	- 2: po wlozeniu  baterii (funkcja - brakuje)
	- 3: po aktywowaniu FA-SET (funkcja Init...())
- [ ] logika radia - sprawdzic i poprawic to co bylo z millimessa (to samo zaimplementrowac do MC, tam przemyslec te tryby jeszcze raz, a przede wszystkim: "Einst.RFMode = 2;" przemiescic i inny warunek na wyjscie)
- [ ] usuniecie jednej resolution
- [ ] jeden interface na raz, kabel albo ant
- [ ] dodac HOLD
- [ ] init i fa - para funkcje
- [ ] czy sie wylacza bez messsystem
- [ ] nie wylacza sie samo w autooff
- [ ] Niebling: std: min, max, musi funkcjonowac rowniez preset
- [ ] lo-bat, czy kasowac flage lo bat? nie., w menue czy sprawdzac lo-bat, - 
- [ ] za szybko dziala zegar w 1086 - np ubat i baterie tylko w hr (pewnie czestotliwosc odsierzania)
- [ ] zdezaktywowac pomiar baterii w nie HR- pokazuje poprawnie dopiero przy  ref ustawione na 3V ale mierzone jest 2.2V do masy (gorny rezystor 0,56V, ucieka gdzies 0,2V, czy to rezystor wewnetrzny)
- [ ] testy ogolne poboru pradu oraz 
- [ ] czasami sie nie wlacza automatycznie od sondy, kabel dku1, po dluzszym czasie ???
- [ ] sprawdzenie i upewnienie sie czy nie zostaja jakies artefakty (abstract layer Display)
- [ ] 844 - preset i reset poprawic, dodac jakis przedzial w celu lepszej detekcji zmiany punktu przegiecia (okno lub filtr???)
- [ ] letd-t stralka LP do tylu z ustawieniami
- [ ] 844 zablokowac kierunek pomiaru
- [ ] na kablu nie wylacza sie tylko inkrmentuje: dlaczego sie nie wylacza oraz dlaczego inkrmentuje (to samo bylo w EMV przy resecie)
- [ ] poukladac procedure startowa po optymalizacji startu przejz Jensa w DigMC.c
- [ ] 844 - gdzie indziej zrobic ta histereze nie AnzWert tylko wczesniej???, lub przesledzic AnZWertRaw - to calosc przemyslec

produkcja:
- [x] flashowanie radio z seggera
- [ ] program do kalibracji rozszerzyc - marcheck - i produkcja
- [ ] interface do precimara

Interfejsy
- [ ] Dodanie nowych rozkaow dla ANT od Nico i Ockera
- [ ] cykliczne wysylanie sprawdzic dla DKU1 i ANT
- [ ] units evaluation + dku1
- [ ] resolution evaluation + dku1
- [ ] helios preiser evaluation
- [x] numery Funk dal nowych urzadzen
- [ ] usunac ART No z ANT
- [ ] sprawdzic ustawienia nico co do uart - ponoc dziala mu to lepiej

- [x] poprawic funk dir w MC (tak jak w MM)
- [ ] gdy hold jest aktywny to czy mozna wejsc do menue
- [ ] po VAR1 lub VAR2 - pokazac cyfry bo sie nie wysietla czyasami
- [ ] czy po factory reset reset czy inny zestaw parametrow
- [ ] Ub sie nie pojawia za 2 -gim razem



Prio 3:
- [ ] ??? sendString() length eval dokonczyc
- [ ] ??? dodac LCD1 and LCD0 - aktualizacja na bierzaco
- [ ] ??? dodac LCDMEM do ANT oraz LCD1, i symulacja klawiszy
- [ ] ??? czy polaczenie kablem to permanentnie zalaczony moze byc
- [ ] ??? przesylanie parametrow jako zrzut FRAM
- [ ] ??? status LED-ow
- [ ] ??? dodac do pliku wynikowego numer wersji
- [ ] ??? (parametry do excela i automatyzacja)
- [ ] ??? symulacja zegara
- [ ] ??? krzywa kalibracyjna
- [ ] ??? testy automatyczne
- [ ] ??? architektura SW, tak aby sie dalo robic symulacje
- [ ] ??? biblioteka ogolna do schnitstellen
- [ ] ??? testy jednostkowe i automatyczne z precimar
- [ ] ??? czy da sie zrobiuic detekcje display type - nie koniecznie potrzebny
- [ ] ??? po polaczeniu - wykryciu kabla wyslac wiadomosc - jestem
- [ ] ??? podlaczoiny kablem to permanentnie wlaczony ???
- [ ] dodac LCD1? i LCD0? wysylanie tylko zmian jezeli zaistnialy za kazdym cyklem (tez ledow) - tylko mozliwe jezeli kabel podlaczony
LED? - status ledow

- [ ] millimess: [[Millimess_todos]]


?
??? czy switching off powinien byc niemozliwy gdy jest hold???

!!! interfejsy zrobic jako modul i w osobnym repo na gitlabie, nie trzeba wtedy nic uzgadniac !!!