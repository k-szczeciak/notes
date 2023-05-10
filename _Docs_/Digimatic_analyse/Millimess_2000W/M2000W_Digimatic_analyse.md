[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](M2000W_Digimatic_analyse.pdf)
# Millimess 2000W digimatic schnittstelle Analyse
<img src="device.png" height="200px"><br>
## 1. Messaufbau:
### 1.1. Millimess **2000W** Entwicklungsmuster
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
![image](_Docs_/Digimatic_analyse/Millimess_2000W/meas.png)
### 3.1. Zeitaufnahme mit Zyklische-Anforderung:
- 1000ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/1000ms.png)
- 500ms
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/500ms.png)
- 250ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/250ms.png)
- 200ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/200ms.png)
- 150ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/150ms.png)
- 100ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/100ms.png)
- 90ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/90ms.png)
- 80ms:
  ![image](_Docs_/Digimatic_analyse/Millimess_2000W/80ms.png)

## 4. Ergebnis:
| Zeit  |  Typ   |  Min  |  Max  |  Ist   |
| :---: | :----: | :---: | :---: | :----: |
|  T1   |   -    | 2 ms  | 40 ms |  4 ms  |
|  T2   | 21 µs  |   -   |   -   | 19 µs  |
|  T3   | 100 µs |   -   |   -   | 106 µs |
|  T4   | 100 µs |   -   |   -   | 104 µs |
|  T6   |   -    |   -   | 77 ms | 100 ms |
|  T7   |   -    | 19 ms | 57 ms | 16 ms  |

Clock ist nicht immer gleich