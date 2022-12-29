# Millimess 2000W digimatic schnittstelle pruefung
<img src="M2000W/M2000W.png" height="400px"><br>
## 1. Messaufbau:
### 1.1. Millimess **2000W** Entwicklungsmuster
### 1.2. Digimatic Kabel: DK-D1, Art.: 4102606
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="M2000W/M2000W_setup.png" width="400px"><br>
<br><br>
## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***
![image](img/digi_def.png)
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](M2000W/M2000W_meas.png)
### 3.1. Zeitaufnahme mit Zycklische-Anforderung:
- 1000ms:
  ![image](M2000W/1000ms.png)
- 500ms
  ![image](M2000W/500ms.png)
- 250ms:
  ![image](M2000W/250ms.png)
- 200ms:
  ![image](M2000W/200ms.png)
- 150ms:
  ![image](M2000W/150ms.png)
- 100ms:
  ![image](M2000W/100ms.png)
- 90ms:
  ![image](M2000W/90ms.png)
- 80ms:
  ![image](M2000W/80ms.png)

## 4. Ergebnis:
|Zeit|Typ|Min|Max|Ist|
|:-:|:-:|:-:|:-:|:-:|
|T1|-|2 ms|40 ms|4 ms|
|T2|21 us|-|-|19 us|
|T3|100 us|-|-|106 us|
|T4|100 us|-|-|104 us|
|T6|-|-|77 ms| 100 ms|
|T7|-|19 ms|57 ms|16 ms|
