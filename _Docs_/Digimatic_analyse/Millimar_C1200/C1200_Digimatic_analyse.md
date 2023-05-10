[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](C1200_Digimatic_analyse.pdf)
# Millimar C1200 digimatic schnittstelle Analyse
<img src="device.png" width="300px"><br>
## 1. Messaufbau:
### 1.1. Millimar **C1200** (Art.: 5212010, sn.: 61080018), 
### 1.2. Digimatic Kabel: Digimatic, Art No. 4346021
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="setup.png" width="400px"><br>
<div style="page-break-after: always;"></div><br>

## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***<br>

<img src="digi_def_6.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](_Docs_/Digimatic_analyse/Millimar_C1200/meas.png)
### 3.2. Zeitaufnahme mit Zyklische-Anforderung:
- 1000ms:
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/1000ms.png)
- 500ms
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/500ms.png)
- 250ms:
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/250ms.png)
- 200ms:
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/200ms.png)
- 150ms:
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/150ms.png)
- 100ms:
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/100ms.png)
- 80ms:
  ![image](_Docs_/Digimatic_analyse/Millimar_C1200/80ms.png)
- 70ms:
  ![image](70ms.png)
- 60ms:
  ![image](60ms.png)
## 4. Ergebnis:
| Zeit  |  Typ   |  Min  |  Max  |  Ist   |
| :---: | :----: | :---: | :---: | :----: |
|  T1   |   -    | 2 ms  | 40 ms | 35 ms  |
|  T2   | 21 µs  |   -   |   -   | 71 µs  |
|  T3   | 100 µs |   -   |   -   | 105 µs |
|  T4   | 100 µs |   -   |   -   | 97 µs  |
|  T6   |   -    |   -   | 77 ms | 70 ms  |
|  T7   |   -    | 19 ms | 57 ms | 49 ms  |