

- [MarCator Project](#marcator-project)
  - [1. Questions for meeting 08.11.2022:](#1-questions-for-meeting-08112022)
  - [2. next tasks:](#2-next-tasks)

# MarCator Project

- [x] batterie status?
	- ueber messsystem
- [x] normales bedien
	- ja, implementiert
- [ ] status nach dem start
- [x] przelaczanie tolerancji
- [x] richtung befehl Dir+/- nach CHA+/-


Fragen:
- [x] MIN MAX blinken vor der messung oder waerend
- [ ] wenn soll es "Start" wieder Zeigen 
- [x] Kann Preset wenn Min Max aktiv ist wechseln konnen
	- immer in menue und ueber taste, ausser messung
- [x] statt preset kann null wert sein
	- es its immer ein preset asusgewaehlt
	- ABS ist null
- [x] kan Hold funktion in standard modi aktiv sein
	- ja
- [ ] ausschalten und einschalten wenn moeglich?
- [ ] toleranz aktiv und umschalten?
	-  immer umschalten ist moeglich
	- aphaenging von innen oder aussenmessung
- [x] ablauf
- [ ] reset fuer min und max, neu starten
	- ja
- [ ] preset wechsel ist immer mit neues wert einstellung verbunden
- Verschiedene Toleranzen 3x

po rozmowie:
!!! zmiana w menue ustawienia preset wybor PRIII inna strzalka (tylko marcator ma 3xpresety), up - tylko do zmiany wartosci lub przejscia do nastepnego punktu zmiany, a right - do przechodzenia w menue do nast punktow oraz przesuwania po polach
- [x] !!! ABS zawsze do PRIII (pokazuja sie razem) kiedy reset to obydwa znikaja 
- [x] !!! MIN i MAX blink tylko wtedy gdy pomiar ma miejsce
!!! Zmiana PRIII w kazdym momencie (przez klawisz lub menue) oprocz trwania pomiaru
Hold zostawiamy przy std mode
prerset ma dotyczyc wartosci ekstermalnej
po zmianie na nowy preset  "Start"
to samo po zmianie na min max
preset po pomiaze - z maxa i mina
menu dopracowac np tol, wskazanie priii i tol abs
przejscie z std i reset do max min
przy przejsciu do min/max reset analogu i wartosci
ABS pokazuje sie w menue razem a pre
rozkazy schnittstelle przejzec
zerowanie przyciskiem res/start

czy mozna zmieniac preset w trakcie wyboru funkcji
czy mozna rozpoczac pomiar jezeli nie zostal wzbrany preset
czy hold moze zostac w normalnym trybie
kierunkek funkcji a min i max


po wylaczeniu i wlaczeniu powrot do poprzedniego stanu.
czy mozna wylaczyc w trakcie pomiaru

next:
- dokonczyc zmiany:
	- przeczytac bedienkonzept
	- preset z przycisku (brak resetu tylko zostaje minmax reset)
	- przelaczanie max i min od poczatku start
	- PRE III, nie przelaczanie pre w trakciepomiaru
	- dlugie wlaczanie przy starcie
	- 64 values
	- wszedzie "no fun" gdzie trzeba, np T6 jezeli pierwszy przebieg
	- zdezaktywowac reset przy pierwszym przejezdzie
	


	- ABS? przelaczenie jezeli Min lub Max
	- preset: nie mozna zmieniac w trakcie pomiaru oraz 
	- musi byc preset jezeli 
	- analiza wartosci startowej - jak nie jest z programatora oraz zakres pomiarowy
	- wysylanie danych przy stop (po zalaczeniu kabla nie pokazuje HOLD)
	- 64 wartosci na sekunde
	- bateria (w domu, sprawdzic dzialanie z zasilaczem)
	- timeout dla pomiaru
	- zerowanie wartosci starttowej aby wyeliminowac te wartosc poczatkowa duza
	- stop/data czy zaimplementowac hold, jezeli nie to no function
	- napis "Test" gdy sprawdza funk????
	- sprawdzic funkcje przez kabel czy nie wplywa na zachowanie
- dodac Min i Max na wyswietlaczu (napis)
- 2 wersje przez define std i br
- sprowdzenie poboru pradu
- refactoring
- symulacja
- unit testy (assert)
- optymalizacja zuzycia pradu
- sprawdzic overload, Einst.TaDelay, Einst.TolAnz2000


- !!!! sprawdzic alt pomiar


pytania 2023.03.31:
- czy ma byc najpierw MAX czy MIN ( wstarej jest najpierw min)
- czy ledy maja sie swiecic przy pomiarze tak jak przy std
- resetowanie PR przy przejsciu do funkcji - to bedzie tez wskaznie ze nie inicjalizacja, pytanie???
- cyz nie powinne tolerancja byc ustawiana automatycznie do presetu

pytania od sprzedawcow:
- warstwa komunikacyjna: dokumentacja, api, ?????


spotkanie 2023.04.11:
- [x] Zmiana kolejnosci w menue
- [x] 3x tolernacja przypisana do PR
- [x] tolernacja w menue blink razem z PRI PRII lub PRIII
- [x] Wyrzucic preset
- [ ] DK-U1 - TOL? jak w C1202
- [ ] Powiekszyc tolerancje dla wymiarow wiekszych od 1000mm - poczakac na odpowiedz od PM 
- [ ] wszystkie presety na 0 a tolerancje na tyle samo


next:
- przetestowac DK-U1 interface

inne pytania do englera:
podwyzka
monitory
wyjazd
maciek devops i frontend



neu 2023.04.14:
- 3x Toleranz:
	- ustawianie w menue
	- wartosci standardowe
	- ikony TOL z PRIII razem
- wprawadzanie tolerancji
- usuniety  napis "preset"
- zmiana kolejnosci w menue (najpierw preset potem tolerancja)
- 64 pomiary na sekunde w trybie min max
- timeout 120 sek
- autostart ale tylko w trybie normalnym

pytania:
1. czy wyjscie jezeli sie potwierdzi PRIII?
2. kiedy ma sie pojawiac PR razem z TOL
3. przy edycji TOL czy ma przejmowac ktory PR jest aktywny
4. jaki timeout dla pomiaru
5. czy autostart ma byc tez w min max?
6. brak wyslania pomiaru przy timeoutcie
7.  jaka tolerancja, i od jakiej wartosci

[[Marcator_touch_DK-U1]]

















neu 2023.04.14:
- 3x Toleranz:
	- Einstellung im Menü
	- Standardwerte
	- TOL-Symbole mit PRIII zusammen
	- 3x TOL
	- 3xTOLW (wert und eingabe)
	- Schnitstelle DK-U1 anpassung (bes. Befehle: PRE... TOL... TOLW...)
- Eingabe der Toleranz
- Untertitel "Preset" gelöscht
- Änderung der Reihenfolge im Menü (erst Preset dann Toleranz)
- 64 Messungen pro Sekunde im Min-Max-Modus
- Zeitüberschreitung 120 Sekunden
- Autostart aber nur im Standardmodus

Fragen:
1. soll es Menue verlasssen, wenn PR-Index bestätigt wird?
2. wann soll PR zusammen mit TOL erscheinen?
3. wenn TOL editiert wird, soll es PR-Index uebernomen sein?
4. welches Timeout für die Min MaxMessung
5. soll Autostart auch in min max -Modus sein?
6. kein Senden der Messung bei Timeout?
7. welche Toleranz-uberwachung ab 1000mm?
8. DK-U1 Schnitstelle: soll TOL mit PRE aktiviuert werden?

webcam: https://www.amazon.de/-/pl/dp/B08MP339XM/ref=sr_1_1?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=36X118QUI02EM&keywords=tracer+web007&qid=1681457533&sprefix=tracer+web007%2Caps%2C257&sr=8-1


schnitstelle:
- ~~welches Antwort soll geschickt werden wenn "Start" auf dem Display Steht - jetzt ist 0.000, soll das ERR3 (Auftrag kann nicht ausgeführt werden.) sein
- ~~ist OL? fuer MarCator relevant ist?
- soll DES? abfrage genau Wie in C1202 sein? ```DEVICE_<DEVICE>_<MASTER_PASSWORD>```
- soll PRE Antwort nur Aktive Preset antworten oder alle 3 auf einmal
- soll TOL Antwort nur Aktive Toleranz antworten oder alle 3 auf einmal
- (N)TOLW auf  TOLW`<no>` umstzen?
- ist ABS befehl fuer MarCator relevant?
- Was bedeutet RST_ABS???
- messung start und stopp impelmentieren (in C1202 es gibt START, STOP und PAUSE)
- PRE? und TOL? alle 3 auf einmal senden oder nur aktuele
- Neu: START und STOP - nur in BR-variannt
- DES? antwort mit DES1_XXXXX
- ID? Antwort ID1_TXXXXXXX_SXXXXXX



stand 26.04.2023:
- letzte Gespräch mit Hr Niebling 21.04.2023
- 3x Toleranz:
	- Einstellung im Menü
	- Standardwerte
	- TOL-Symbole mit PRIII zusammen
	- 3x TOL
	- 3xTOLW (wert und eingabe)
	- Schnitstelle DK-U1 anpassung (bes. Befehle: PRE... TOL... TOLW...)
- Eingabe der Toleranz geändert
- Änderung der Reihenfolge im Menü (erst Preset dann Toleranz)
- 64 Messungen pro Sekunde im Min-Max-Modus
- Zeitüberschreitung 300 Sekunden
- Autostart im allen Modi
- Schnitstelle:
	- Messung update
	- TOL neu 
	- PRE neu
	- ...
- dodanie do protokolu statusu: off, on, hello, ver ,..

popytac jacka i krzyska jakie maja uwagi 

zbudowac warsty i inetrakcj. jaka architektura:
paraEval()
#error hjgf
zmiana parametru przez funkcje a nie przypisanie
zastosoac SOLID, KISS i DRY

sprawdzic wszecie UTol i OTol gdzie jest wartosc: "999 999 99" a powinno byc "9999 999 99" bo moze byc wiecej niz 999.999 99 mm

moze dodac do opisu dlaczego error

| SkTeil |     condition for Tol     |    mark    |   range   |     mark     |    range    | new |    remark     |
| ------ |:-------------------------:|:----------:|:---------:|:------------:|:-----------:|:---:|:-------------:|
| 1      |             -             | 000.0001mm | ±0.002mm  | 0.000005inch | ±0.0001inch |     |               |
| 2      |             -             | 000.0002mm | ±0.004mm  | 00.00001inch | ±0.0002inch |     |               |
| 3      |       dTol <= 18um        | 000.0005mm | ±0.010mm  | 00.00002inch | ±0.0004inch |     |               |
| 4      |   18 um < dTol ≤ 36 um    | 0000.001mm | ±0.020mm  | 00.00005inch | ±0.001inch  |     |               |
| 5      |   36 um < dTol ≤ 72 um    | 0000.002mm | ±0.040mm  | 00.0001inch  | ±0.002inch  |     |               |
| 6      |   72 um < dTol ≤ 180 um   | 0000.005mm | ±0.100mm  | 00.0002inch  | ±0.004inch  |     |               |
| 7      |  180 um < dTol ≤ 360 um   | 0000.01mm  | ±0.200mm  | 00.0005inch  | ±0.010inch  |     |               |
| 8      |  360 um < dTol ≤ 720 um   | 0000.02mm  | ±0.400mm  |  00.001inch  | ±0.020inch  |     |               |
| 9      |  720 um < dTol ≤ 1800 um  | 0000.05mm  | ±1.000mm  |  00.002inch  | ±0.040inch  |     | only for Tol. |
| 10     | 1800 um < dTol ≤ 3600 um  |  0000.1mm  | ±2.000mm  |  00.005inch  | ±0.100inch  |  X  | only for Tol. |
| 11     | 3600 um < dTol ≤ 7200 um  |  0000.2mm  | ±4.000mm  |  00.01inch   | ±0.200inch  |  X  | only for Tol. |
| 12     | 7200 um < dTol ≤ 18000 um |  0000.5mm  | ±10.000mm |  00.02inch   | ±0.400inch  |  X  | only for Tol. |
| 13     |       18000 < dTol        |  0001.0mm  | ±20.000mm |      -       |      -      |  X  | only for Tol. |



czy rozszerzyc protokol o zmiane rozdzielczosci w trybie Tolerancji

czy zawsze poszerzac jezeli granice tol beda poza???


```
New User Interface concept impelmented.

__Main features:__
- New Min Max functions proceeding:
  - Start and Stop with separate button
  - First calibration run for setting up Preset value
  - Sending data after measurement
- new tolerances concetp:
  - 3x Tolerance, each fixed for Preset
  - Tolerance can be called only with Preset active
- Menue operation update:
  - Editing Tolerances (selection and edit)
  - New order in menue: First Preset then Tolerance
  - activation after leaving menue
- new DK-U1 commands and updates
- new scales for larger tolerances
- Dynamic Resolution adjustment for larger lenghts

- Bug fixes
- other improvements:
  - autostart
  - timeout 
  - hold function
```


maybe:
- parameter handling (hints at the end of "Library.c")
- - dokonczyc MC bedien i dku1 - pomyslec jak to zrobic generycznie
- pomyslec o embos?
- 



Questions:
- DKU1: TOL1 aktywacja tylko gdy jest PRE czy zapamietac ze zostalo aktywowane?
- czy ustawienia przez DKU1 wartosci TOL nie zalacza Preset, czy TOL1 ma aktywowac odrazu PREx
- MW? - wartosc - pre
- ABS czy ma byc zawsze w stosunku do PRE czy moze byc tez tryb osobny, tak chyba mowil engler
- Should be wake up on DKU1