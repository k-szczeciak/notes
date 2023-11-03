
Funkcjonalnosc
- [ ] po resecie FA ma sie pojawic nawa i numer wersji
- [ ] opcja HR
- [ ] opcja 844
- [ ] funkcaje na init_para, fa-para i reset-para, ew on-off-para:
	- 1: po wdraniu programu (tablela init)
	- 2: po wlozeniu  baterii (funkcja - brakuje)
	- 3: po aktywowaniu FA-SET (funkcja Init...())
- [ ] logika radia - sprawdzic i poprawic to co bylo z millimessa (to samo zaimplementrowac do MC, tam przemyslec te tryby jeszcze raz, a przede wszystkim: "Einst.RFMode = 2;" przemiescic i inny warunek na wyjscie)
- [ ]  usuniecie jednej resolution

produkcja:
- [ ] flashowanie radio z seggera
- [ ] program do kalibracji rozszerzyc - marcheck - i produkcja
- [ ] interface do precimara

Interfejsy
- [ ] Dodanie nowych rozkaow dla ANT od Nico i Ockera
- [ ] cykliczne wysylanie sprawdzic dla DKU1 i ANT

- [ ] units evaluation + dku1
- [ ] resolution evaluation + dku1
- [ ] helios preiser evaluation
- [ ] numery Funk dal nowych urzadzen

- [x] poprawic funk dir w MC (tak jak w MM)
- [ ] gdy hold jest aktywny to czy mozna wejsc do menue
- [ ] po VAR1 lub VAR2 - pokazac cyfry bo sie nie wysietla czyasami



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