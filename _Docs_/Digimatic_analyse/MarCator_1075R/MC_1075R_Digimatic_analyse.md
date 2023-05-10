[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](MC_1075R_Digimatic_analyse.pdf)
# MarCator 1075R digimatic schnittstelle Analyse
<img src="device.png" height="300px"><br>
## 1. Messaufbau:
### 1.1. MarCator **1075R** (Art.: 4336010, sn.: 22070356), 
### 1.2. Digimatic Kabel: Digimatic, Art No. 4102411
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="setup.png" width="600px">
<div style="page-break-after: always;"></div>

## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***<br>
<img src="digi_def_6.png" width="800px">
<div style="page-break-after: always;"></div>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](_Docs_/Digimatic_analyse/MarCator_1075R/meas.png)

### 3.2. Zeitaufnahme mit Multi-Anforderung:
- 1000ms:
  ![image](_Docs_/Digimatic_analyse/MarCator_1075R/1000ms.png)
- 500ms
  ![image](_Docs_/Digimatic_analyse/MarCator_1075R/500ms.png)
- 250ms:
  ![image](_Docs_/Digimatic_analyse/MarCator_1075R/250ms.png)
- 200ms:
  ![image](_Docs_/Digimatic_analyse/MarCator_1075R/200ms.png)
- 150ms (Antwortsperiode: 150ms):
  ![image](_Docs_/Digimatic_analyse/MarCator_1075R/150ms.png)
  ![image](_Docs_/Digimatic_analyse/MarCator_1075R/150ms_zoom.png)
- 120ms (Antwortsperiode: 240ms):
  ![image](120ms.png)
  ![image](120ms_zoom.png)
## 4. Ergebnis:
| Zeit  |  Typ   |  Min  |  Max  |  Ist   |
| :---: | :----: | :---: | :---: | :----: |
|  T1   |   -    | 2 ms  | 40 ms | 166 ms |
|  T2   | 21 µs  |   -   |   -   | 112 µs |
|  T3   | 100 µs |   -   |   -   | 104 µs |
|  T4   | 100 µs |   -   |   -   | 136 µs |
|  T6   |   -    |   -   | 77 ms | 150 ms |
|  T7   |   -    | 19 ms | 57 ms | 183 ms |

Datei sind plausiebel.
Antwortzeit für Tastendruck ist auch ohne Verzögerung.