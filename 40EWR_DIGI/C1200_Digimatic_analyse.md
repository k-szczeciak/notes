# Millimar C1200 digimatic schnittstelle pruefung
<img src="C1200/C1200.png" width="300px"><br>
## 1. Messaufbau:
### 1.1. Millimar **C1200** (Art.: 5212010, sn.: 61080018), 
### 1.2. Digimatic Kabel: Digimatic, Art No. 4346021
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="C1200/C1200_setup.png" width="400px"><br>
<br><br>
## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***
![image](img/digi_def.png)
<div style="page-break-after: always;"></div><br>

## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](C1200/C1200_meas.png)
### 3.2. Zeitaufnahme mit Zycklische-Anforderung:
- 1000ms:
  ![image](C1200/1000ms.png)
- 500ms
  ![image](C1200/500ms.png)
- 250ms:
  ![image](C1200/250ms.png)
- 200ms:
  ![image](C1200/200ms.png)
- 150ms:
  ![image](C1200/150ms.png)
- 100ms:
  ![image](C1200/100ms.png)
- 80ms:
  ![image](C1200/80ms.png)
- 70ms:
  ![image](C1200/70ms.png)
- 60ms:
  ![image](C1200/60ms.png)
## 4. Ergebnis:
|Zeit|Typ|Min|Max|Ist|
|:-:|:-:|:-:|:-:|:-:|
|T1|-|2 ms|40 ms|35 ms|
|T2|21 us|-|-|71 us|
|T3|100 us|-|-|105 us|
|T4|100 us|-|-|97 us|
|T6|-|-|77 ms| 70 ms|
|T7|-|19 ms|57 ms|49 ms|