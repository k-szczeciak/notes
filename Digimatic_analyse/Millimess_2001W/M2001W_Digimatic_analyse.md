[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](M2001W_Digimatic_analyse.pdf)
# Millimess 2001W digimatic schnittstelle Analyse
<img src="device.png" height="300px"><br>
## 1. Messaufbau:
### 1.1. Millimess **2001W** Entwicklungsmuster
### 1.2. Digimatic Kabel: DK-D1, Art.: 4102606
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="setup.png" width="550px"><br>
<div style="page-break-after: always;"></div><br>

## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***<br>
<img src="digi_def_6.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](meas.png)
### 3.1. Zeitaufnahme mit Zyklische-Anforderung:
- 1000ms:
  ![image](1000ms.png)
- 500ms
  ![image](500ms.png)
- 250ms:
  ![image](250ms.png)
- 200ms:
  ![image](200ms.png)
- 150ms:
  ![image](150ms.png)
- 100ms:
  ![image](100ms.png)
- 90ms:
  ![image](90ms.png)
- 80ms:
  ![image](80ms.png)

## 4. Ergebnis:
| Zeit  |  Typ   |  Min  |  Max  |     Ist      |
| :---: | :----: | :---: | :---: | :----------: |
|  T1   |   -    | 2 ms  | 40 ms |    10 ms     |
|  T2   | 21 µs  |   -   |   -   |    19 µs     |
|  T3   | 100 µs |   -   |   -   | 106 (184) µs |
|  T4   | 100 µs |   -   |   -   |    104 µs    |
|  T6   |   -    |   -   | 77 ms |    100 ms    |
|  T7   |   -    | 19 ms | 57 ms |    22 ms     |

Clock ist nicht immer gleich (106/184 µs)