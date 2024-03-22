gen issues:
- nie wybudzanie
- polaczenie radia
- pierwszy pomiar br
- sprawdzenie duzych liczb w HR-module

- [ ] struktura do zmiennych koniecznie
- [ ] BR, oraz MIN MAX i inne blokady z befehl z DKU1 i inne takze ANT
- [ ] przeglad fnkcji do stringow - pogrupowac i z refaktorowac 

Todo temp 2024-02-26:
- [x] poprawic scale: dla 1 i 0 sprawdzenie wszystkich  wskazania, porozmawiac nt temat z PM
- [x] -> dodac LEDt fo sperren oraz scale (FktFilter)
- [x] -> nie chce sie ponownie laczyc po wlozeniu baterii - bat on values
- [x] -> odswierzanie w menue aby ograniczyc prad (obnizyc czestotliwosc w menue), to ponizej tez sie powinno poprawic, albo 
- [x] -> poprawa digimatic - inch
- [x] -> menue - powrot z channel do off???
- [x] -> z kabla Err 255
- [x] wprowadzanbie incha dla duzych wartosci wadliwe
- [x] ograniczenie wprowadzania incha do 399.999 - zamiast tego obliczanie wartosci i meldunek ze wskazaniem za duzej wartosci
- [ ] "OL" dla wartosci przekraczjacych 9999.999 lub dla incha
- [ ] change - Bat-messung - tryb serwisowy (tez dodac pozostale rzeczy np statrtup):
	- [ ] nowe funkcje te co dodalem: caly nowy interface
	- [ ] boot sequence
	- [ ] doatep do funkcji w menue? lub home order - totalna kontrola
	- [ ] dodac np sterowanie klawiszami, do symulacji lub edycji 
- [ ] change -LED-y zolty permanentnie 
- [ ] ustawianie wartosci w inchu - zgodnie z ustawiona resolution, ostatnia cyfra
- [ ] zaokraglanie w dol dla incha tez bo jak jest ustawiona inna resolution to jest problem bo za duza wartosc
- [ ] przerobic zaokraglanie
- [ ] logika RF z Millimesa - w menue - razem z tym powrotem z CH do radio
- [ ] wlaczanie 86 ze zwloka, 2-etpowo
- [ ] poprawic widok hold w menue funk
- [ ] dodac znacznik BAT check do tx i sprawdzac kiedy jest testowane
- [ ] spra RESFx dla HR i innych ??
- [ ] sprawdzic CLEAN?
- [ ] ANT i led time - powinno blinkac moze prz przesylaniu ???
- [ ] ANT - jak sie wejdzie w menue i wysle komuniact to przerywa polaczenie
- [ ] ANT - czasami problem z laczeniem, trzeba wtedy zmienic numer

dodane 2024-02-29:
- [ ] battery measuremnt:
	- [x] do wszystkich modeli 
	- [ ] pomiar co 10 minut
	- [ ] flaga nie resetowalna
	- [ ] pomiar 3 razy aby uniknac bledow
	- [ ] brak pomiaru jezeli ledy , touch lub radio sa aktywne
	- [ ] napiecie 2,7V

dodane: 2024-03-14
- rozmowa projektowa:
	- usunac ustawianie przy pomocy tastera - patentschutz
	- analog scale naciskanie RST i PRE - przeskakiwanie wartosci
	- Battry: detekcja No bat: jezeli napiecie ponizej 1 V gdy np polaczone przez kabel - wtedy reset flagi to na wypadek wyciagniecia i zmiany bateri
	- blad zaokraglania dla wartosci max w mm - OL widoczne tylko
	- monitorowanie wartosci wprowadzanej z kabla
	- scale 2 - wskazowka ma blinkac tez na skrajach czyli 0 w maxie oraz max 
	- Blokada wszystkiego nawet FA - ale po wyciagnieciu bateri i wlozeniu mozliwe jest FA
	- 

next:
od PM-a
- wylaczyc LEDy w menue
- timery do splash screen (kopia timera z scaleAnimation()) oraz Battery timer
- Hold ma byc w menue dla radio kiedy jest off (pokazanie ze klawisz srodkowy ma byc HOLD)
- "no fcn" jak sie naciska ABS a juz jest w trybie abs
	- policzyc, oszacowac ile godzin
	- Zapytac PM-a jaki zas ma byc na ponmiar i jaki charakter orazz jak oszacowac zuzycie energii wdla BR-a
- oszacowac /. obliczyc ilosc godzin pracy w roznych trybach (Jupyter lab)
- zmiana kierunku w czasie pomiaru w BR-ze zatrzymanie pomiaru
- symbol kabla z maenue ma zniknac - tylko tam gdzie jest USB lub digi
- symbol funk w menue - tylko w funk
- jezeli kabel i funk to tylko funk - odciecie
- poprawic scale 1 min
- poprawic scale 2 z blinken dla wartosci chwilowych rowniez
- 
- jednoczesne przesylanie funk i dku1
- jakies Tech dlugi z np needle (niepotrzebne funkcje i eksperymenty) - razem z tymi ghostami [[2024-02-03]] i [[2024-02-04]]:
	- animacja w scale - nadmiarowe funkcje, polaczenie istniejacych, ...
- przejzec - zoptymalizowac dzialanie tych funkcji
- sprawdzic jaki prad dla nowej skali analogowej 
- inne ogolne symbole w menue
- ledy w menue bat w HR - za krotko - pewnie czest odswierznia - zmienic na timer, podonie tez splashscreen jest za szybki
- podobnie animacja w HR-e dla scale
- "Error" -> "No SenSo" when measurement system is not detected
- przebufdowac ` else if (!strncmp((char *)DuplexRXD, "PRE", 3))    Ev = msgArgumentEval((char *)DuplexRXD, 3, &msgPar, S_PRE_F);` w bedien - najlepiej wszystkie funkcje na jakis standard
- [x] sprawa pomiaru CDT - ciaglego
- komunikaty jednoczesne po kablu plus wyswietlacz
- sprawdzic edycje incha w kontekscie 10 metrow - preset i tolerancja
- punkty z ostatniego spotkania: np: - nazwa do uMaxum w marcator check i inne. sprawdzic dB radia itp - do dku1
- autooff in menue, recovery, czasami nie wrac z uspienia, to od nico, powrot z pomiarow. jaki stan itd - testy
- przeanalizowac wszystkie sytuacje dla ((0))
- statusy on off , ale RUN musi zostac, lub zmodyfikowac MarCator Check
- Display test dorobic 
- przejscie z menue - przeset do ekranu glownego - moze byc ladniejsze
- preset dluga zwloka przy nacisnienie ponownym preset i analogu scale 2
- zmiana nazwy dla uMaxum
- prady i optymalizacja
- rozszezenie trybu serwisowego o np konfiguracje - jak robilem w AT, lub osobny tryb AT
- wskazanie led w menue gdy kabel podlaczony
- zamienic struktury: DisplVarStruct na enumeratory
- dodac wysylanie: JSONa lub liste z komendami i parametrami - parametry juz sa, dodac tylko strukture
- usunac parametry, poprawic devGroup, HR params
- [x] wylaczyc radio z menue jak art nie odpowiadia takiemu - bo nie widomo jaki numer ma miec radio, czyli nr radia = 0 to brak w menue
- [ ] popracowac nad wylaczaniem mess syetem w menue - przy przelaczaniu wystepuja chwilowo nie wlasciwe, pomyslec nad optymalizacja
- [ ] poprawcowac nad przelaczaniem sie z mene do pomiarow
- [ ] Befehl - na sama analogowa skale zmiane
- [ ] blysniecie gdy poza tolerancja i prest nacisieny
- [ ] ??? pomiar napiecia baterii w menue gdy kabel podlaczony to podbija napiecie do 3.6V
- [ ] sprawdzic testy LED-ow wraz ze zdalnym sterowaniem i statusem
- [ ] tryb serwisowy poprawic - logo zalacznaie i pomiary i takie tam dalej inne


Q:
- OI jako home button nawet w menue???
	- in alfa
- czy nie powinien byc komunikat przy naciskani ABS jezeli jest juz w ABS
	- (no functyion)
- dodanie resetu do startu w BR-e ??? nie ma to wplywu na pomiar ??
- czy mozna zmieniac kierunek w BR-e w czasie pomiaru:
	- messung halten. muss preset neu setzen
- ~~co z tym przenoszeniem pomiaru tluczka pomyslec
- jaka jest ideaa LED-ow i spradzenie jak to ma moeisce z warngrenzen - pogadac z Niebingiem 
- leds - czy bez warngrenzen nie powinno byc na odwrot?
- -> co z tym Hold w menue ma byc prze jakims menue:
	- z d-off bei funk 
- zapytac gdzie das menue baterii???
- long press TOL when tol not active - no fcn???
- czy w scale 2 min lub max - wiper nie powinien prazechodsizc na druga strone?
- czy w 87 strzalka w analogu ma sie tez pokazac jak ta w 86
- moze wiper powinien blinkac, czy musi blinkiac w scale 2
- czy zmieniajac PRI -> PRII -> PRIII zmienia sie res max, ale cza ma sie zmieniac rowniez na minimalna rozdzielczosc ??? chyba nie
- Q - czy symbol podlaczonego kabla ma sie siecic caly czas?
	- in menue nur bei digimatic
	- bei funk wellen
- funk - daten kabel muss unterbrochen, nur strom versorgung
- poprawic Analog anzeige:
	- min nie pokazuje wartosci
	- dla reverse zawsze blinken

dodanie 2024-03-12
Q?
czy dodac KFAK do radio
czy dodamy filter do zwyklych??? - lub low freq


- later!!! remove: sendStrPrep(), substitute
- rename MESS_MODE_REL to MESS_MODE_ABS

---
- czy HOLD w menue Funk, ale gdy kabel podlaczony tez?

Q form Nico Test comparison:
RST - ERR3?
LED 3 - kabel - brak ???

pytania do PM:
- BR - measurement timeout should be fixed or floating (now is fixed)
- kazrza jaki czas i ile przyjac do kalkulacji 


inne:
jaka moc radia
jakie zuzycie baterii dl aLEDs
krzysiek podsumowanie
pomiar pradu i ew. optymalizacja
zmiana nazwy uMaxum - MarCator i Marcator check






z 2024-03-15:next:
- [x] rozdzielenie Radio od cable
- [x] Menue: dodac HOLD do menue DIGI
- [x] Menue: przechodzenie z w funk
- [x] 255 err po kablu ??? od nico - zalatwione przez usuniecie d ---- po przejsciu do kanalu
- [x] brak radia numeru - nie ma menue
- [x] komunikat ze brak radia  jezeli konfiguracja o tym mowi
- [x] korekta wprowadzania bledu duzej wartosci, zaookraglanie
- [ ] monitorowanie wartosci  duzych - teraz sprawdzic jak dzialaja
- [x] komunikaty takie same na wyswietlaczu jak z klawiszy - tylko Pr(x)
- [ ] usuniecie sterowania tasterem, wylaczenie tastera w menue, pozostawic refreshrate taki jak dla std 16Hz
- [ ] dodanie baterry no bat  i pozostale z bat wlacznie z przesylaniem komunikatu
- [ ] serwis dopracowac w tym z bat (BatStatus)
- [ ] digimatic inch
- [x] wysylanie "OL"
- [ ] komunikat jak ABS kiedy wlaczone PRE - "in ABS"
- [ ] komunikat w 86 jezeli 2 klawisz nacisniety: "No Tol"
- [x] poprawic TOLW(x) powinno byc jedno
- [ ] "Error" -> "No SenSo" when measurement system is not detected
- [x] blysniecie Led-t z  dla 0s
- [ ] menu Bat
- [ ] digimatic poprawic timingi aby osiagnac predkosc max jak dla c1202
spr prady: std hr br menue












tluczek kontaklt z nim:
- wytlumaczenie z maxami
- aby napisal swoje wnioski
opis jak urazyc hr-plot

next week: [[2024-02-26]]
tluczek
testy, testy automatyczne
parametery 
czyszczenie






Napiecia miezone u Jensa:
soll -    ist
3.4v - 3.30v
3.2v - 3.14v
3.0v - 2.94v
2.8v - 2.77v
2.6v - 2.58v
2.4v - 2.36v
2.2v - 2.22v






















---
### poprzednie, dlugoterminowe (do weryfikacji)
Funkcjonalnosc
- [x] po resecie FA ma sie pojawic nawa i numer wersji
- [ ] opcja HR (needed HW), optymalizacja pomiaru, filter i czestosc sprawdzania bateri
- [ ] opcja 844
- [ ] funkcaje na init_para, fa-para i reset-para, ew on-off-para:
	- 1: po wdraniu programu (tablela init)
	- 2: po wlozeniu  baterii (funkcja - brakuje)
	- 3: po aktywowaniu FA-SET (funkcja Init...()) odpalenie articleEval() by ustawic zmienne lub!!! zrobic liste jak w c1202 z wart std???
	- 4: przy starcie sprawdzanie czy wartosci takie jak Einheit jest ok, np nie 0 ( dla Einheit - jest na starcie) - testy testy testy
	- wygenerowanie tez enumeratprow do wszystkich parametrow - w menue mozliwosc wysylania komand???
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
- [ ] co z konfiguracja jak nie ma radia lub jest a konfiguracja nie wymaga
- [ ] jak zmiana wariantu - to reset do FA
- [ ] hold w schnitstelle - przydala by sie w koncu unifikacja
- [ ] zalaczanie ponowne z uspienia - czy jest taki sam stan 
- [ ] dodac logowanie i zmienne predkosci do np szybkich pomiarow
- [ ] sprawdzic autooff czy na wlasciwym HW dziala poprawnie
- [ ] 844  (histereze przeniesc z WandleWert() do GetAnzWert() tak aby dalo sie w trybie serwisowym widzic wlasciwa wartosc)
- [ ] refactor and documentation
- [ ] BR - ograniczenie ERR3 jezeli w czasie pomiarow, aby sie nie dalo ustawic np presetu w czasie pomiaru
- [ ] ?? display test ??
- [ ] HR-battery test
- [ ] on/off:
	- [ ] przypadkowe nacisniecie przy wlaczaniu - zwloka
	- [ ] auto off czy mozliwe jest aby sie nie zlaczylo
	- [ ] zalaczanie z interface-u DKU1
- [ ] czy w trakcie pomiaru mozna wylaczyc BR-a
- [ ] ANT - wysylanie danych (pomiaru) - potwierdzenie - zrodla - to co Nico pytal i opowiadal 
- [ ] auto wylaczenie i brak ponownego zalaczenia - sprawdzane top bylo w 
- [ ] przeniesc z WDT do maina, a tam zostawic counter lub tick
- [ ] potwierdzenie preset w menue po nastawie - refactor kodu
- [ ] usuniecie menue nastawy histerezy
- [ ] co z battery? jak ukryc?
- [ ] przejscie z preset - zwloka w skali
- [ ] refactor i usuniecie nie potrzebnych juz zmiennych
- [ ] dane diagnostyczne co z nimi
- [ ] przechodzenie z menue do pomiaru ma byc "ladne"
- [ ] meldunek ze brak radia nawet jesli ustawiono
- [ ] zerowanie wartosci przy wlozeniu baterii - doparam (podobnie jak przys fa-reset) - byla poluzowana srobka
- [ ] co z holdem po polaczneniu przez radio
- [ ] !!! jak polezy dlugo z bateria to wychodza jakies jaja przy kalibracji z uzyciem MarCator Check, albo moze tak wplywa na to wysylanie konfiguracji
- [ ] preset przy zmianie kierunku nie dziala i ikona F poprawic
- [ ] init para after calibration (article number)
- [ ] create struct or function state: eg cableCon = 1 
- [ ] pomyslec o true and false lib
- [ ] zrobic funkcje do  set preset, ser reset, set abs
- [ ] overflow wszedzie sprawdzic w wartosciach
- [ ] sprwdzic duze liczby w HR z filtrem
- [ ] sprawdzic edycje incha w kontekscie 10 metrow
- [ ] 

light:
sprawdzic delay przy przyciskach
poprawic powtarzajacy sie kod: 
```
if ( (Hold) && (Einst.devtype != devTypeVarStruct.BR) ){
	TextMeldung(ANZ_HOLD, 500, 0);
	break;
}else{
	if ( (Hold) && (!Einst.MaxModus) ){
		TextMeldung(ANZ_HOLD, 500, 0);
		break;
	}
}
```

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
- [ ] dokonczyc SrvCmd: bit 0 raw, bit 1 filtered, bit 2 anzeige, bit 4 bat volt dla HR, hist dla EWR (zrobic funkcje do tego: sentDiag(srvCmd, val1, val2, val3, val4)) - tylko na kablu - detekcja
- [ ] dodac czestosc odswierzania obrazu - tylko na kablu
- [ ] testowanie automatyczne schnitstelle
- [ ] konfiguracja poprzez jedna komede - zwrot: lista komend i mozliwosci (cos co jest w C1202)
- [ ] usuniecie zmiennych po usunieciu kabla: SRV, BAUD i FREQ
- [ ] setting radio number separetly
- [ ] standard function dla nastaw dla DKU1
- [ ] rozlaczenie ANT i DKU1 aby sie nie dalo
- [ ] command Home
- [ ] brakuje ustawiania skali (SkalierTeilungsWert czy jakos tak)

- [x] poprawic funk dir w MC (tak jak w MM)
- [ ] gdy hold jest aktywny to czy mozna wejsc do menue
- [ ] po VAR1 lub VAR2 - pokazac cyfry bo sie nie wysietla czyasami
- [ ] czy po factory reset reset czy inny zestaw parametrow
- [ ] Ub sie nie pojawia za 2 -gim razem
- [ ] wake up ustawic do duk1
- [ ] przypisac do S_ z T_ aby bylo takie samo - zrobic funkcje - general interfaces
- [ ] nowy mat number: reset wszystkich params do ustawien fabrycznych bez sn
- [ ] po wlaczeniu br w trybie sie nie odswierza sie cyfry - niebling czy to nim nax bylo czy tez br - sprawdzic weszedzie
- [ ] jakie radio ustawic defoltowe
- [ ] sterowanie po dku1 np wyjscie z menue jak w C1202
- [ ] service data: on off ale "RUN" must stay, lub wlaczenie diag wczesniej w MarCator Check, lub pierwszy raz po zmianie T_...



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
- [ ] doxygen with ascii art 
- [ ] wiki internal and or external with exmples, tutorials and downloads
- [ ] narzedzie do commitowania podobne jak dla A1701
- [ ] millimess: [[Millimess_todos]]
- [ ] Kennlinie dla MC, 5-10 punktow
- [ ] !!! Zebrac wszystkie toole jak do ustawiania wariantow w jedno miejsce
- [ ] zrobic do tolerancji w menue dluzdze strzalki wskazujace up i down
- [ ] przerobic DigitalWert() rounding na tabele i jjedna formule - miejsce
- [ ] !!!! wszedzie  jednostki w zmiennych - unifikacja jak w boschu !!! poszukac program do jednostek richtlinie
- [ ] porawic analog anzeige z niefajnych komponentow typu przeliczanie +21 - 21 - optymalizacja
- [x] Zostaje, ale zminilalizowany zamiast wielu funkcji dodatkowych zlikwidowac AnalogAnzeige()
- [ ] usunac zbedne argumenty z displMarker()


?
??? czy switching off powinien byc niemozliwy gdy jest hold???

!!! interfejsy zrobic jako modul i w osobnym repo na gitlabie, nie trzeba wtedy nic uzgadniac !!!

!!! kabel dku1 rs232, drukarka termiczna np: ok 700-800 pln https://www.citizen-systems.com/en/products/printer/pos/ct-s310ii
interfejs - automatyka IO


przestrzen na dane dowolne np stringi, txt IP w C1202 numer i inne


FA reset
- baud
- SrvCmd

```
 ___    _                      
|_ _|__| | ___  __ _ ___   _   
 | |/ _` |/ _ \/ _` / __| (_)  
 | | (_| |  __/ (_| \__ \  _   
|___\__,_|\___|\__,_|___/ (_)
```
- [ ] variable refrashe rate for power eficency
- [ ] konfiguracja poprzez jedna komede - zwrot: lista komend i mozliwosci (cos co jest w C1202)
- [ ] doxygen
- [ ] dku1 variable freq - podobnie jak SRV befehl
- [ ] apka do androida
- [ ] kabel do usbc do androida otg (zasilanie)
- [ ] czy nie wysylac konfiguracji jako zestaw znakow jak parmaetr zamioast art no (kazda litera jako ustawienie) - to dalej do komunikacji - jak byla by najlepsza
- [ ] Abstraction layer [[MC-overview.canvas|MC-overview]]
- [ ] swipe gertures gora i dol po 3 przyciski do edycji cyfr np, przesuwania sie w menue
- [ ] przemyslec now rozkazy tak aby byly uniwersalne, proste i szybkie w impelmentacji - zrobic biblioteke i repo do tego tak aby mogl tez niko wspoldzielic
- [ ] status przesylac gdzie jest w menue???
- [ ] sterowanie dowolnym segmentem???
- [ ] status: automatyczny lub na zyczenie parametr
- [ ] states for display and other components like battery display when changing
- [ ]  dodac do MC - wywolanie z lista komend aby program mogl pobrac z urzadzenia ??? zamalo miejsca raczej - to moze do C1202 - dzieki temu bedzie zawsze aktualna lista komand.


params: factory settings po zaprogramowaniu nowego artykulu
```c
typedef struct{
    char val1;
    char val2;
}abc;

abc myabc = {.val1 = 1, .val2 = 2}
typedef enum {
    ONE = 0,
    TWO,
    THREE
}params;
params PAR;
PAR.ONE;
int get(char no);
int set(char no);
//uChar checkResBound(){
//
//}

// parameters as a struct with min and max
  
// three options for handling parameters:
// (1) resolution.increase(b); resolution.set(4); // check boundaries underhood: resolution.minmax(); resolution.check()
// (2) parameter.increase(resolution, 1); // check boundaries underhood
// (3) parameter(resolution, increase, 1); // as above
// parameterCheck(DYNAMIC_CHANGES); parameterCheck(STATIC_CHANGES); container for parameters rules where: DYNAMIC_CHANGES only when display update, STATIC_CHANGES - all parameters.
  
// (4) if (getPram(RESOLUTION) == 1) , where: #define RESOLUTION 1 or enum
// (5) param(RESOLUTION, [default|init]), param(par.RESOLUTOIN).get()
// (6) param.get(RESOLUTION)
// (7) param(RESOLUTION).get();
// iterate, check, correct, save, default
// auto generated as in c1202
  
// param(PAR.RESOLUTION, set, 4)
// param(PAR.RESOLUTION, get, 0)
// param(PAR.RESOLUTION, default, 0)
// param(PAR.RESOLUTION).get();
// param(PAR.RESOLUTION).set(4);
```

[[c_unit_test]]

do T_ i S_
dodac slownik do komunikatow, np.:
"no Fcn": "ERR3" dla DKU1 i "E3" dla funk

ustawianie cyfr jak u nico przez przekrecanie

!!! dodac ustawianie z przemeszczenia sondy jak u niko z pokretlem !!!



pytania do PM-a:
- czy auto off w menue, i gdzie powrot
- czy automatyczne opuszczenie menue?
- co z kierunkiem w 844 dla histerezy

pytania do Nieblinga:
czy nowe wskazanie do wszystkich Z-tow czy tylko do uMaxuma III?
czy maxim bedzie lylko z "9" na koncu
pozniej 
co z batereria - wskazaniem
czy do menue dodac tez sterownaie przy pomocy sondy?


max wartosc suma 32 x 9999.999 900 = 32 x 10 000, 000 000 ( moze przekroczyc max wartosc long)

```
 _____         _                _    _ _   _____           _       
|_   _|__   __| | ___    _     / \  | | | |_   _|__   ___ | |___   
  | |/ _ \ / _` |/ _ \  (_)   / _ \ | | |   | |/ _ \ / _ \| / __|  
  | | (_) | (_| | (_) |  _   / ___ \| | |   | | (_) | (_) | \__ \  
 _|_|\___/ \__,_|\___/  (_)_/_/   \_\_|_|   |_|\___/ \___/|_|___/  
|  _ \  ___  ___  ___ _ __(_)_ __ | |_(_) ___  _ __   | | | |      
| | | |/ _ \/ __|/ __| '__| | '_ \| __| |/ _ \| '_ \  | | | |      
| |_| |  __/\__ \ (__| |  | | |_) | |_| | (_) | | | | |_|_|_|      
|____/ \___||___/\___|_|  |_| .__/ \__|_|\___/|_| |_| (_|_|_)      
                            |_|
```



```
 _____ _      _     _   _____             _ _                _          
|  ___(_) ___| | __| | |  ___|__  ___  __| | |__   __ _  ___| | __  _   
| |_  | |/ _ \ |/ _` | | |_ / _ \/ _ \/ _` | '_ \ / _` |/ __| |/ / (_)  
|  _| | |  __/ | (_| | |  _|  __/  __/ (_| | |_) | (_| | (__|   <   _   
|_|   |_|\___|_|\__,_| |_|  \___|\___|\__,_|_.__/ \__,_|\___|_|\_\ (_)
```

- rozmowa z Krzyskiem Tluczkiem (15.02.2024):
	- ???pierwszy pomiar BR ???
	- wyjasnic LED-y kolory (nie konsekwencja, podwojne dzialanie - moze zaburzac doznania)
	- "No Fcn" - za czesto bez opisu
	- powinno dzialac "IO" zawsze jako homescreen 
	- przenoszenie pressetu MIN MAX przy kalibracji Min w odniesieniu do Max: nastawy na innej powierzchni - szukanie miejsca
	- Start stop jezeli hold z pedalu - marcom, do duzych urzadzen (START/STOP)
	- Tol aktywna - brak mozliwosci zalaczenia resetu ???
- 
- dodatkowo mail od niego:
	- Jeżeli tolerancje są związane z opcją Preset faktycznie powinien być zablokowany klawisz ABS, gdyż wtedy, aby wprowadzić 0 musiałby wyłączać Preset i tolerancje.                                                                                                                                                                               
	- Idąc poza domem zapomniałem po której stronie świeci się czerwona a po której żółta dioda. Okazuje się, że w przypadku, gdy wyłączone są granice kontrolne – ustawienie 00 istnieje jeszcze większa nielogiczność niż Tobie zgłosiłem. Gdy przekroczona zostanie górna granica tolerancji świeci się dioda czerwona po lewej stronie, a właśnie wtedy wyświetla się strzałka w prawym górnym rogu wyświetlacza, gdy przekroczona jest dolna granica tolerancji świeci się żółta dioda po prawej stronie wyświetlacza, a na wyświetlaczu pojawia się strzałka przekroczenia w lewym dolnym rogu wyświetlacza. Więc nie ma w tym żadnej logiki, gdyż powinno być na odwrót, chociaż ja nadal twierdzę, że w obu przypadkach powinna się świecić tylko dioda czerwona, która jednoznacznie określa przekroczenie granic tolerancji, a jeżeli ktoś chce wiedzieć która ma taką informację na wyświetlaczu w postaci strzałki. 
	- Oprócz tego co Tobie zgłaszałem wcześniej – gruby problem z przenoszeniem wartości kalibracji w min na max i na odwrót na razie nie mam się do czego przyczepić więcej.                                                                                                                                                                           

Bartoszek:
didy 3 kolorowe
brak Max-Min w BR-e
przechodzenie na PRI -> PRII -> PRIII strzalka do gory
inkrementacja i dekrementacja  - pomyslec, progresja 
home button w menue
dodanie dodatkowych opisow
komunikat - brak radia pomimo art ???
eaton - zywotnosc testy - podobnie na suwmarki i odklejajace sie elementy
filtr - do normalnego czujnika, lub czestotliwosc probkowania z menue
ustawienia fabryczne bez kabla jezeli jest blokada na FA-set - kombinacja klawiszy np brak detekcji 
ekran pojemnosciowy - ????
pulsowanie analogu w stasunku do digital



---------------------------------------------------------------------------------------------------------------------------------------------
spotkanie 20.02.2024 z PM:
- cos bylo z hold ze sie nie pojawia przy wlaczeniu i lub wylaczeniu funk - wiadomo (przy autooff)
- tol-abs przelaczanie zostaje - ale posprawdzac z mojej strony (rowniez ((0)))
- czasy meldunkow takie same wszedzie - 1sek
- autooff kiedy byl aktywny hold - po wlaczeniu ponownie ma byc to samo - tu jest blad bo jest zatrzymane ale sie nie wyswietla
- "mm" w menue ma sie pojawiac poprawnie
- komunikaty maja sie pokazywac jezeli z dku1 rowniez na display-u
- brak autooff kiedy kabel podlaczony
- led t dodac do sperren
- kiedy kabal opdlaczony to autooff ma byc zawieszone
- DATA btn z digimatic ma dzialac


Od innego PM-a:
- preset od sebastiana przy zmianie kierunku zle wskazuje
- wysokie zuzycie pradu w menue przy tej nowej funkcji
- sprwdzic duze liczby w HR z filtrem

2024-02-22, Engler i PM:
	- MC -liczenie zuzycia pradu na ile czasu - oszacowac to
	- MC - uMaxum - zmiana nazwy i moze jeszcze cos, dopasowanie zmian i inne ale z tym poczekac do powrotu ze stanow 
	- MC - poprosic krzyska tluczka o dalsze wnioski i spisanie ich
	- MC - sprawdzic jak moc jest emitowana z radia - w instrukcji jest **4dB**

blink cyfr - poczekac na decyzje PM-a


- czy nie zastosowac filtra w std???

```
 ____  __  __   _     _                      
|  _ \|  \/  | (_) __| | ___  __ _ ___   _   
| |_) | |\/| | | |/ _` |/ _ \/ _` / __| (_)  
|  __/| |  | | | | (_| |  __/ (_| \__ \  _   
|_|   |_|  |_| |_|\__,_|\___|\__,_|___/ (_)
```

- YT - dluzsze szkoleniowe
- YT shorts
- adsense - algorytmy - jaki zastosowac Hooks??
- przegladanie tego aktywne i dodawanie co tydzien
- Activ Product public Roadmap
!!! zrobic samemu kilka shortsow: najpierw plan jakie tresci w punktach, np jeden short tygodniowo