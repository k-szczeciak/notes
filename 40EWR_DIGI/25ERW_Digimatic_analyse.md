# 25EWR digimatic schnittstelle pruefung
<img src="25EWR/25EWR.png" width="300px"><br>
## 1. Messaufbau:
### 1.1. **18EWR/E** 500mm (Art.: 4112713, sn.: 12040130), 
### 1.2. Digimatic Kabel: Digimatic, Art No. 4102411
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="25EWR/25EWR_setup.png" width="600px"><br>
<br><br>
## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***
![image](img/digi_def.png)
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](25EWR/25EWR_meas.png)
### 3.1. Zeitaufnahme mit Multi-Anforderung:
- 1000ms:
  ![image](25EWR/1000ms.png)
- 500ms
  ![image](25EWR/500ms.png)
- 450ms
  ![image](25EWR/450ms.png)
- 400ms
  ![image](25EWR/400ms.png)
- 300ms
  ![image](25EWR/300ms.png)
- 250ms:
  ![image](25EWR/250ms.png)
- 200ms:
  ![image](25EWR/200ms.png)

## 4. Ergebnis:
|Zeit|Typ|Min|Max|Ist|
|:-:|:-:|:-:|:-:|:-:|
|T1|-|2 ms|40 ms|200 ms|
|T2|21 us|-|-|112 us|
|T3|100 us|-|-|104 us|
|T4|100 us|-|-|136 us|
|T6|-|-|77 ms| 450 ms|
|T7|-|19 ms|57 ms|216 ms|
Datei sind plausiebel.