[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](40EWR_Digimatic_analyse.pdf)
# Micromar 40EWR digimatic schnittstelle analyse
<img src="device.png" width="300px"><br>
## 1. Messaufbau:
### 1.1. 40EWR, 75-100mm (art.: 4157003, kein Seriennummer)
### 1.2. Digimatic Kabel: DK-D1
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="setup.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***<br>
<img src="digi_def_6.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](_Docs_/Digimatic_analyse/Micromar_40EWR/meas.png)
### 3.2. Zeitaufnahme mit Mehrfach-Anforderung:
![image](_Docs_/Digimatic_analyse/Micromar_40EWR/multi.png)
<div style="page-break-after: always;"></div><br>

## 4. Ergebnis:
Zeiten T1, T6 und T7 sind auser toleranz.
| Zeit  |  Typ   |  Min  |  Max  |   Ist    |
| :---: | :----: | :---: | :---: | :------: |
|  T1   |   -    | 2 ms  | 40 ms | 0,57 ms  |
|  T2   | 21 µs  |   -   |   -   | 21,25 µs |
|  T3   | 100 µs |   -   |   -   | 105,3 µs |
|  T4   | 100 µs |   -   |   -   | 110,4 µs |
|  T6   |   -    |   -   | 77 ms | 1200 ms  |
|  T7   |   -    | 19 ms | 57 ms | 12,64 ms |

Sonst datei sind plausiebel.
Antwortzeit für Tastendruck ist auch ohne Verzögerung.