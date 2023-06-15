| No | Name            | FA Valule | Init Value | Description                                                                              |
|----|-----------------|-----------|------------|------------------------------------------------------------------------------------------|
| 1  | Variante        | no value  | 2          | Geräte-Variante: 1086R(i) oder 1087R(i) --> wird nicht verändert!                        |
| 2  | Einheit         | 1         | 1          | Maßeinheit  1: mm    2: inch                                                             |
| 3  | FixAufl         | no value  | 0          | Fixe Auflösung der Ziffernanzeige  --> wird nicht verändert!                             |
| 4  | Aufloesung      | 3         | 3          | Auflösung der Ziffernanzeige (3: 000.0005 mm oder 00.00002 inch)                         |
| 5  | SkTeilung       | 3         | 3          | Skalenteilung 1..8 (entspricht der Auflösung)                                            |
| 6  | Richtung        | 0         | 0          | Zählrichtung (hineingehend -> +)                                                         |
| 7  | FilterIx        | 2         | 2          | Filtereinstellung 0..4 -> Ringbuffergröße 1..16 Werte (Default: 4 Werte)                 |
| 8  | MessModus       | 2         | 2          | 1: Absolut-, 2: Relativ- oder 3: Preset-Modus                                            |
| 9  | MaxModus        | 0         | 0          | Normal-, Max-, Min-, Max-Min-Modus                                                       |
| 10 | TolModus        | 0         | 0          | Normal-, Toleranz-Modus                                                                  |
| 11 | TolWG[0]        | 0         | 0          | Toleranz-Warngrenzen 0: ohne WG   10, 20, 30: WG 10%..30%                                |
| 12 | TolWG[1]        | 0         | 0          | Toleranz-Warngrenzen 0: ohne WG   10, 20, 30: WG 10%..30%                                |
| 13 | TolWG[2]        | 0         | 0          | Toleranz-Warngrenzen 0: ohne WG   10, 20, 30: WG 10%..30%                                |
| 14 | TolAnz2000      | 0         | 0          | Anzeigeart der Tol-Überschr. bei 2000:  0: mit Pfeil  1: mit Digitalanz.                 |
| 15 | TaDelay         | 1         | 1          | Tastenverzögerung für Data, Reset, Preset ...                                            |
| 16 | TouchSens       | 0         | 0          | Touchempfindlichkeit 0: ohne Handschuh, 1: mit Handschuh                                 |
| 17 | GeraeteNr       | 0         | 0          | Geräte-Nr. für Funkverbindung                                                            |
| 18 | RFMode          | 1         | 0          | Funk-Modus: 0: kein Funk vorhanden: 1: Funk ausgeschaltet; 2: Funk eingeschaltet         |
| 19 | RFFreqIx        | 0         | 0          | Index für RFFreq-Array                                                                   |
| 20 | RFEcoMode       | 0         | 0          | Funk-Eco-Mode: 0: aus (Msg-Freq. 4Hz)   1: ein (Msg-Freq. 2Hz)                           |
| 21 | NoInch          | no value  | 0          | 1: ohne Inch-Einstell-Menü      --> wird nicht verändert!                                |
| 22 | Lock            | 0         | 0          | Tastensperre aus                                                                         |
| 23 | Digimatic       | 0         | 0          | Digimatic: 0: deaktiviert 1: Format 1 mit 6 Stellen  2: Format 2 mit 8 Stellen aktiviert |
| 24 | TeileNr[10]     | no value  | [0]        | Teile-Nr.                       --> wird nicht verändert!                                |
| 25 | SerienNr[10]    | no value  | [0]        | Serien-Nr.                      --> wird nicht verändert!                                |
| 26 | KalDatum[8]     | no value  | [0]        | Datum der letzten Kalibrierung  --> wird nicht verändert!                                |
| 27 | NextKalDatum[8] | no value  | [0]        | Datum der nächsten Kalibrierung --> wird nicht verändert!                                |
| 28 | AnzFaktor       | 1.0       | 1.0        | Faktor für angezeigten Wert                                                              |
| 29 | KorrFaktor      | no value  | 1.0        | Faktor für Maßstabskorrektur    --> wird nicht verändert!                                |
| 30 | MR_Offset       | 0         | 0          | Offset für Messrichtungswechsel in 10 nm                                                 |
| 31 | AnaResetAnzWert | 0         | 0          | Anzeigewert bei Reset Analoganzeige in 10 nm                                             |
| 32 | PresetWert      | 0         | 0          | aktueller Presetwert in 10 nm                                                            |
| 33 | PresetWertOld   | 0         | 0          | Preset Value saved for Standard mode                                                     |
| 34 | Preset[0]       | 100000    | 100000     | eingegebene Presetwerte in 10 nm                                                         |
| 35 | Preset[1]       | 100000    | 100000     | in 10 nm                                                                                 |
| 36 | Preset[2]       | 100000    | 100000     | in 10 nm                                                                                 |
| 37 | ObereTol[0]     | 60000     | 60000      | obere Toleranzgrenze    in 10 nm                                                         |
| 38 | ObereTol[1]     | 60000     | 60000      | obere Toleranzgrenze    in 10 nm                                                         |
| 39 | ObereTol[2]     | 60000     | 60000      | obere Toleranzgrenze    in 10 nm                                                         |
| 40 | UntereTol[0]    | -60000    | -60000     | untere Toleranzgrenze   in 10 nm                                                         |
| 41 | UntereTol[1]    | -60000    | -60000     | untere Toleranzgrenze   in 10 nm                                                         |
| 42 | UntereTol[2]    | -60000    | -60000     | untere Toleranzgrenze   in 10 nm                                                         |
| 43 | ObereTolWG[0]   | 60000     | 60000      | obere Tol-Warngrenze    in 10 nm                                                         |
| 44 | ObereTolWG[1]   | 60000     | 60000      | obere Tol-Warngrenze    in 10 nm                                                         |
| 45 | ObereTolWG[2]   | 60000     | 60000      | obere Tol-Warngrenze    in 10 nm                                                         |
| 46 | UntereTolWG[0]  | -60000    | -60000     | untere Tol-Warngrenze   in 10 nm                                                         |
| 47 | UntereTolWG[1]  | -60000    | -60000     | untere Tol-Warngrenze   in 10 nm                                                         |
| 48 | UntereTolWG[2]  | -60000    | -60000     | untere Tol-Warngrenze   in 10 nm                                                         |
| 49 | AutoOffTime     | 0         | 0          | Auto-Off Zeit in Min. (0..999 Minuten, 0: Auto-Off deaktiviert)                          |
| 50 | KundenPW        | no value  | 0          | Kunden-Passwort (default: 0)                                                             |
| 51 | RFTestMenu      | 0         | 0          | 1: mit Funk-Test-Menü                                                                    |
| 52 | TolAussen[0]    | 0         | 0          | Toleranz-InnenAussen-Messung 0: Innen, 1: Außen                                          |
| 53 | TolAussen[1]    | 0         | 0          | Toleranz-InnenAussen-Messung 0: Innen, 1: Außen                                          |
| 54 | TolAussen[2]    | 0         | 0          | Toleranz-InnenAussen-Messung 0: Innen, 1: Außen                                          |
| 55 | FctLock[0]      | 0         | 0          | Funktionssperre                                                                          |
| 56 | FctLock[1]      | 0         | 0          |                                                                                          |
| 57 | FctLock[2]      | 0         | 0          |                                                                                          |
| 58 | FctLock[3]      | 0         | 0          |                                                                                          |
| 59 | Clean           | 0         | 0          | CLEAN-Funktion                                                                           |
| 60 | PrIx            | 0         | 0          | Index für Preset-Array                                                                   |


