- [ ] battery Anzeige: "BAt-Lo":
	- [ ] przy wlaczaniu
	- [ ] jezeli watorsc spadnie
	- [ ] przy wylaczaniu
	- [ ] zrodlo ???
	- [ ] pomiar napiecia
- [ ] edycja wlasciwego presetu
- [ ] entprellzeit
- [ ] laczenie  sie ANT
- [ ] podluzszym czasie prad w stanie aktywnym jest +10 uA, (85 zamiast 75), dlaczego
- [ ] zmiezyc napiecie Vcc
- [ ] zmierzyc napiecie na wyjsciu z pomiaru napiecia baterii
- [ ] przy recznym wylaczaniu > 5mA
- [ ] dokkonczyc obsluge ANT
- [ ] iso format dla daty CAL: rrrr-mm-dd
- [ ] zbudowac pomiar ciagly pradu z bocznikujacym i wzmacniaczem - zrobic opis przebiegu
- [x] Autooff w menue
- [ ] timedelay for ANT, DKU1 and Digimatic (data send, setting preset, reset, )

| R=U/I |       |     |
|-------|-------|-----|
|       |       |     |
| R     | 100   | Ohm |
| I     | 20    | uA  |
| U     | 2000  | uV  |
|       | 2     | mV  |
|       | 0,002 | V   |
| opamp | 1000  |     |
| Uampl | 2     |


pomiar pradu:
https://circuitdigest.com/calculators/op-amp-gain-calculator

- [ ] zoptymalizowac messsystem pod wzgledem zuzycia pradu
- [ ] po wylaczeniu radia zostaje 90 uA ???
- [ ] pomiarzyc we wszystkich sytuacjach pomiar pradu na komponentach
- [ ] ustawienie dokladnego czasu przesylu cnt

- [ ] factory settings: tez funk nr - sprawdzic czy jest resetowany
- [ ] sprawdzic czy ustawieniami portu da sie zmniejszyc prad w stanie wylaczonym (np P4 REN config)
- [x] ograniczenie pradu dynamicznie w roznych trybach pracy (np pocztatek)
![[2023-08-14_13h24_59.png]]
done, new:
![[2023-08-14_15h22_36.png]]
!!! nie zawsze dziala idealnie ponowne polaczenie po wylaczneniu jak nie bylo polaczone - dziala hold zamiast...
maybe:
- [ ] symulacja






---
---
- [ ] problem z ponownym polaczeniem przez przycisk w sytuacji gdy wylaczone zosatalo w czasie seak
- [ ] brakujace rozkazy ANT
- [ ] pomiar napiecia przy pradzie - problem resetu - spardzenie dokladniejsze
- [ ] Bat-Lo - 1d
- [ ] pomiar napiecia baterii z dzielnika napiecia
- [ ] cal date wg normy
- [ ] optymalizacja zuzycia pradu w roznych trybach
- [ ] kodkoncyzc DK-U1 jesli chodzi o numery art i ograniczenia
- [ ] tryby continous dla dku1 i ant
- [ ] posprawdzac opcje z numerami itd, jak sa kodowane numery - funk - sprawdzic czy wszystko jest dobrze
- [ ] opcja 844 i std



- lcd mem send
- sim klawisze
do czego sluzy 'ANZ_RF_TEST'

!!! dlaczego nie poprawnie na moim lapi excel wyswietla wartosci
sprawdzic jak jest powiazanie kanal, numer, ...