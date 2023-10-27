reszta pomyslow w notes, repo master i IncMod
do MT w kodzie i repo i na kartkach
todo:
- wykres:
	- skalowanie w x i y, autoskalowanie x
	- podglad wartosci chwilowej gdy nie aktywny pomiar jest
	- funkcje na wykresie (np srednia),
	- odzielone kreska pomiary
	- zrzut pomiarow do pliku (zwiekszyc ilosc punktow pomiarowych do 1200)
	- poprawic Digimatic: poczatek, stan wysoki na data oraz czasy i paralel mode
- pomiary:
	- czemu jest mnoznik i formula po przeliczaniu wartosci czyli x2 powoduje mnimalny skok o 2, moz eopcja
	- walsne jednosctki np st celsjusza
	- pomiary z qr-codem: do strony lub appki
	- wyzwalanie
- poprawic predkosc, obliczyc jaka jest max wydjnosc
- !!! przejsc na RTOS-a, refactoring layers
- symulacja
- ladowanie programow, cos jak AT (sprawdzic co jest uzywane)


pomysly:
- elastomania
- [River Raid](https://github.com/johnidm/asm-atari-2600)
- QR code do danzch urzadzenia
- skanowanie pomiarow QR code bez programu z uzyciem QR
- MT - kafelki do sterowania ustawieniami, akcjami, np: ustawienie pomiaru ze zdjeciem, star pomiaru, wyslanie danych. 
	- to samo z na interfejsie webowym
- MSG z QR codami
- rozszerzenie MT o np zegary i pomiary synchroniczne
- MT pomiar wykresow csva sciagnac
https://www.youtube.com/watch?v=JThMOVkgvUU
- CDT1 - przesylanie ciagle
- sapaer
- display composer
- msg z qr i image (bmp - najpierw podeslane przez dku1)
- RTOS, tasks: e.g. embOS
	- read value
	- display value
	- communication  dku1
- extentions - budowanie wlasnych extentions moze skladnia customowa albo micropython
	- albo kompilowane
	- albo pythonowe, importowanie micropythona do projektu




ChatGPT to display over MT


wyswietlanie komunikatow z netu np temp innych urzadzen

python do programowania

emWin performance:
https://www.segger.com/products/user-interface/emwin/technology/emwin-performance/
![[2021-08-30_10h24_14.png]]

embed in MT and web 3d model viewer:
https://gct.co/de/connector/mem2080


- [ ] okno informacyjne gdy zmiana modulu
- [ ] screenshot w chwili dynamicznej zrobic 