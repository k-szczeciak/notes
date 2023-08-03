

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

new:
- tolerance scale switching 1+ and 1-


Questions:
- DKU1: TOL1 aktywacja tylko gdy jest PRE czy zapamietac ze zostalo aktywowane?
- czy ustawienia przez DKU1 wartosci TOL nie zalacza Preset, czy TOL1 ma aktywowac odrazu PREx
- MW? - wartosc - pre
- ABS czy ma byc zawsze w stosunku do PRE czy moze byc tez tryb osobny, tak chyba mowil engler
- Should be wake up on DKU1
- delay 200ms ?
- CLEAN??? do czego to sluzy:
```
uChar _Ev = 0;
uChar _End = 0;

SaveAndClrLCD();
TextAnz(32);                                     // ' CLEAn ' anzeigen
do {
	_Ev = GetEvent();
	if (_Ev) {
		if (_Ev == T_OnOff) MenueEvent = E_Off;
		else if ((_Ev < S_START) && (_Ev != T_Clean)) _End = 1;
		DataReq = 0;
		P4IFG &= ~BIT4;                          // Interrupt Flag für P4.4 löschen (Req Duplex)
		P4IE |= BIT4;                            // Enable interrupt für P4.4 (Req Duplex)
		DuplexRXD[0] = '\0';
	}
	else EnterLPM;
} while (!_End && (MenueEvent != E_Off) && (MenueEvent != E_AutoOff));
RestoreLCD();
break;
```
- poprawa wyjscia z menue z PRE
- W startup - wersja: STD BR HR 844
- excel to c parms

od Jacka:
- asymetrycznie tol, lub wywalic  '0'
- wysylanie cont CDT1 z poziomu menu

[[ParamsMarCator]]


Hr Ocker:
Funk: jaki numer zarezerwowac na nowe marcatory

teraz sa:
Device Type Id (Bit0 .. Bit6): 
1    MarCator 1087R
2    MarCator 1087BR
3    MarCator 1086R
4    MarCal   16EWRi
5    Micromar 40EWRi
6    MarCal   18EWRi
7    Millimess 2000Wi
8    Millimess 2001Wi
9    817 CLT
10  44EWRi




2023.06.15:
version v0.6 [[Marcator_flashing]]
`V:\Benutzergruppen\Firmware_Software\Firmware\MarCator Touch 1087BR`
`V:\Entwicklung\Elektronik\Projekte\Digitaler MarCator 30377 Teil 2\15_Firmware`

done:
- Neu HW vorbereitung. verbindungen, segment war nicht richtig geluetet, 
	- 2 Wiederstaende muss abgeloettet sein um 500uA verbrauch zu vermeiden
	- ein zustand: 100 - 75uA
	- auszustand: 30uA
	![[Pasted image 20230615132820.png]]
- funk verbindung verbessert: unplausieble initialisierung [[2023-05-31]]
	- problem mit kein funk chip erkennung [[2023-06-05]]
- funk verbindung logic:
	- immer wenn gleies numer angegeben ist
	- timeout, weil der chip micht immer verbindungstrennung sendet
	- zusammen arbeitung kabel und ANT - unaphangig
	- verbindung zuverlaessigkeit und vorhersagbarkeit verbesserung (neu funk uartschnitstelle)
- neue ANT befahle


Fragen:
- neu baterie einstellung?
- MarCom  Kabel und ANT verbindung: ekentbar als 1087br zusammen mit alte Verisonen - MarCmo muss nach Teilnummer Fragen?
- can Kabel und Funk un aphaengig arbeiten?


podsumowanei spodkania:
- fixed aufloesung - poprzez Artnummer
- daten format - sprawdzic jak w sylvaku jest
- Ocker - numery ANT


23.06.2023:
- rozmowa z mario:
	- prad: sprawdzic mosfet i Rezystor R405 (lub wysterowac ponizszy ranzystor) 1MOhm
	- odlaczyc przetwornik DC/DC
	- spr. rezystor R504: 1MOhm
	- sprawdzic w programie czy sie cos nie zmienilo
	- sprawdzic wszystkie komponenty czy sa wlasciwe
- rozmowa o testach EMV
- Opis Dzialania MarCatora, zauwazone niedociagniecia:
	- jak jest hold i powroci sie z menue, to nie widac hold
	- warunki startowe
	- w menue wyswietla sie mm z delay
	- sprawdzic wartosc offsetu przy starcie

rozmowa dzisiaj z Englerem i Nieblingiem:
- uaktualnic tabele dla BR (w zakladce) xls
- zaznaczyc ktore rozkazy sa ANT (moze wlasna doku z lista tylko ant)
- [ ] wlozenie baterii - reset ustawien (ma wskazywac zero)
- [ ] opis menue (ew. symulacja)
- [x] preset init na 0
- [x] wylaczyc diody
- [ ] iso format dla daty



rozmowa Niebling 20.07.2023:
- toff time FA and default 8 mins
- tol eingabe: error: "Error - t-SPAn"
- delay time do wszytkiego: rowniez z kabel i radio
- moje pytanie czy zmienic autooff time przy polaczeniu kablem?








---
Pflichtenheft: Aktiv: ca. 80µA (ausgenommen: LEDs, Funk, HR und BR im Dynamikmodus) Standby: ca. 10µA

### Besprechung  (27.07.2023): 
- Aktuel:
	- spannung 3V

| component               | usage [uA] |
| ----------------------- |:----------:|
| LCD                     |     30     |
| read value and calc     |     15     |
| Touch standby           |     2      |
| Messsystem - idle       |     8      |
| Messsytem - measurement |     20     |
| **SUM**                 |   **75**   |

| state                 | usage [uA] |
|-----------------------|------------|
| active                | 80         |
| off                   | 13         |
| in menue              | 50         |
| taste betaetigt       | 105        |
| messung (64Hz)        | 165        |
| funk verbunden - idle | 150        |
| funk - ContData       | 1800       |
| funk - suchen         | 2300       |


- Batterie Anzeige: "BAt-Lo", wann? (in messschrabe es ist bei einschalten und wenn menu verlassen ist)
- Batterie Anzeige signalquelle: Messsystem oder spannungsverteiler (DC/DC leuft bis 1,7 V)
![[2023-07-27_12h37_26.png]]
- GPIO - liste und konfig (pinMapping.xlsx) (z.B. uart for radio chip pull up resistors)
- "Press Start"
- Error Preset Eingabe: entweder: "t-SpAn" oder" Hi Lo "
- Standart AutoOff wert 8 minuten
- editierung AutoOff:
	- waerend editierung 001, wen fest "1" ohne fuehrende "0"
	- "0" statt "---" wenn "0" als endloss eingestellt
- messsystem in meue deaktiviert (30uA sparung)
- radio start neu


radio u Gotfrieda
jaki jest pomiar pradu


---
03.08.2023 Fragen:
1. timeout from menue? (autooff)
2. TasterVerzuegerung entprellzeit) soll wie ist gemeint zu funktioniern? doppelbetaetigung?
	Tate delay nur in:
	- Data Senden, Preset, reset und analog nullen
	- Tasten betaetigung, ANT anforderung, DKU1 , Digimatic
3. BAt-Lo Anzeige:
	1. messung
	2. wann: ein und ausschalten, menue verlassen, wenn medung kommt


---
- ANT optimierung und Fehler
- battery
- delay fertigen (DKU1 und FUNK und DIGI)
- 