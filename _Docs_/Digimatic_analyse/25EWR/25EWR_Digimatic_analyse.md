[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](25EWR_Digimatic_analyse.pdf)
# 25EWR digimatic schnittstelle Analyse
<img src="device.png" height="300px"><br>
## 1. Messaufbau:
### 1.1. **18EWR/E** 500mm (Art.: 4112713, sn.: 12040130), 
### 1.2. Digimatic Kabel: Digimatic, Art No. 4102411
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="setup.png" width="600px"><br>
<div style="page-break-after: always;"></div><br>

## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***<br>
<img src="digi_def_6.png" width="600px">
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](_Docs_/Digimatic_analyse/25EWR/meas.png)
### 3.2. Zeitaufnahme mit Multi-Anforderung:
- 1000ms:
  ![image](_Docs_/Digimatic_analyse/25EWR/1000ms.png)
- 500ms
  ![image](_Docs_/Digimatic_analyse/25EWR/500ms.png)
- 450ms
  ![image](450ms.png)
- 400ms
  ![image](_Docs_/Digimatic_analyse/25EWR/400ms.png)
- 300ms
  ![image](300ms.png)
- 250ms:
  ![image](_Docs_/Digimatic_analyse/25EWR/250ms.png)
- 200ms:
  ![image](_Docs_/Digimatic_analyse/25EWR/200ms.png)

## 4. Ergebnis:
| Zeit  |  Typ   |  Min  |  Max  |  Ist   |
| :---: | :----: | :---: | :---: | :----: |
|  T1   |   -    | 2 ms  | 40 ms | 200 ms |
|  T2   | 21 µs  |   -   |   -   | 112 µs |
|  T3   | 100 µs |   -   |   -   | 104 µs |
|  T4   | 100 µs |   -   |   -   | 136 µs |
|  T6   |   -    |   -   | 77 ms | 450 ms |
|  T7   |   -    | 19 ms | 57 ms | 216 ms |
Datei sind plausiebel.