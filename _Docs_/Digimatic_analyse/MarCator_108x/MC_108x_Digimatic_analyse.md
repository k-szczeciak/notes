[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](MC_108x_Digimatic_analyse.pdf)
# MarCator 108x Digimatic schnittstelle Analyse
<img src="device.png" width="300px"><br>

## 1. Messaufbau:
### 1.1. MarCator **1087R** (Art.: 4337665, sn.: 22050001), **1087BR** (Art.: 4337662, sn.: 22060031), **1086R** (Art.: 4337625, sn.: 22070042), **1086R** (Art.: 4337697, sn.: 22020002)
### 1.2. Digimatic Kabel: Digimatic, Art No. 4102411
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="setup.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***<br>
<img src="digi_def_6.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Einzelmessung:
![image](_Docs_/Digimatic_analyse/MarCator_108x/meas.png)<br>
### 3.2. Zyklischeanforderung:
- 1000ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/1000ms.png)
- 800ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/800ms.png)
- 600ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/600ms.png)
- 400ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/400ms.png)
- 200ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/200ms.png)
- 150ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/150ms.png)
  ![image](150ms_zoom_in.png)
- 100ms
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/100ms.png)
<br>
## 4. Ergebnis:
Alle Zeiten in toleranzen, T6 ist manuel betätigt.
| Zeit  |  Typ   |  Min  |  Max  |   Ist    |
| :---: | :----: | :---: | :---: | :------: |
|  T1   |   -    | 2 ms  | 40 ms |  165 ms  |
|  T2   | 21 µs  |   -   |   -   |  112 µs  |
|  T3   | 100 µs |   -   |   -   |  105 µs  |
|  T4   | 100 µs |   -   |   -   |  119 µs  |
|  T6   |   -    |   -   | 77 ms | 150 ms*) |
|  T7   |   -    | 19 ms | 57 ms |  181 ms  |

*) Wenn Zyklisch Gefragt. Zeit ist kürzer als bei Enzelanfrage.<br><br>
- Gesendete Datei sind plausibel.
- Zyklisch Anforderung bis 150ms stabil, keiene Datei ist verloren.
- Bei schnellere zyklische Aforderung z.B. 150ms, ist keine Antwort mehr:
  ![image](_Docs_/Digimatic_analyse/MarCator_108x/100ms.png)

- Anderes Efekt: CLOCK Frequenz ändert sich bisschen im Nachricht:
  ![image](meas_zoom.png)