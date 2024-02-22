
Funkcjonalnosc
- [x] po resecie FA ma sie pojawic nawa i numer wersji
- [ ] opcja HR (needed HW), optymalizacja pomiaru, filter i czestosc sprawdzania bateri
- [ ] opcja 844
- [ ] funkcaje na init_para, fa-para i reset-para, ew on-off-para:
	- 1: po wdraniu programu (tablela init)
	- 2: po wlozeniu  baterii (funkcja - brakuje)
	- 3: po aktywowaniu FA-SET (funkcja Init...()) odpalenie articleEval() by ustawic zmienne lub!!! zrobic liste jak w c1202 z wart std???
	- 4: przy starcie sprawdzanie czy wartosci takie jak Einheit jest ok, np nie 0 ( dla Einheit - jest na starcie) - testy testy testy
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
 _____ _      _     _   _____             _ _                _          
|  ___(_) ___| | __| | |  ___|__  ___  __| | |__   __ _  ___| | __  _   
| |_  | |/ _ \ |/ _` | | |_ / _ \/ _ \/ _` | '_ \ / _` |/ __| |/ / (_)  
|  _| | |  __/ | (_| | |  _|  __/  __/ (_| | |_) | (_| | (__|   <   _   
|_|   |_|\___|_|\__,_| |_|  \___|\___|\__,_|_.__/ \__,_|\___|_|\_\ (_)
```

- rozmowa z Krzyskiem Tluczkiem (15.02.2024):
	- pierwszy pomiar BR ???
	- wyjasnic LED-y kolory ( nie konsekwencja, podwojne dzialanie - moze zaburzac doznania)
	- "No Fcn" - za czesto bez opisu
	- powinno dzialac "IO" zawsze jako homescreen 
	- przenoszenie pressetu MIN MAX przy kalibracji Min w odniesieniu do Max
	- Start stop jezeli hold z pedalu
	- Tol aktywna - brak mozliwosci zalaczenia resetu
- dodatkowo mail od niego:
	- Jeżeli tolerancje są związane z opcją Preset faktycznie powinien być zablokowany klawisz ABS, gdyż wtedy, aby wprowadzić 0 musiałby wyłączać Preset i tolerancje.                                                                                                                                                                               
	- Idąc poza domem zapomniałem po której stronie świeci się czerwona a po której żółta dioda. Okazuje się, że w przypadku, gdy wyłączone są granice kontrolne – ustawienie 00 istnieje jeszcze większa nielogiczność niż Tobie zgłosiłem. Gdy przekroczona zostanie górna granica tolerancji świeci się dioda czerwona po lewej stronie, a właśnie wtedy wyświetla się strzałka w prawym górnym rogu wyświetlacza, gdy przekroczona jest dolna granica tolerancji świeci się żółta dioda po prawej stronie wyświetlacza, a na wyświetlaczu pojawia się strzałka przekroczenia w lewym dolnym rogu wyświetlacza. Więc nie ma w tym żadnej logiki, gdyż powinno być na odwrót, chociaż ja nadal twierdzę, że w obu przypadkach powinna się świecić tylko dioda czerwona, która jednoznacznie określa przekroczenie granic tolerancji, a jeżeli ktoś chce wiedzieć która ma taką informację na wyświetlaczu w postaci strzałki. 
	- Oprócz tego co Tobie zgłaszałem wcześniej – gruby problem z przenoszeniem wartości kalibracji w min na max i na odwrót na razie nie mam się do czego przyczepić więcej.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
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




- czy nie zastosowac filtra w std???
