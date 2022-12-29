# MarCator 1075R digimatic schnittstelle pruefung
<img src="MC_1075R/MC_1075R.png" width="200px"><br>
## 1. Messaufbau:
### 1.1. MarCator **1075R** (Art.: 4336010, sn.: 22070356), 
### 1.2. Digimatic Kabel: Digimatic, Art No. 4102411
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
<img src="MC_1075R/MC_1075R_setup.png" width="600px"><br>
<br><br>
## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***
![image](img/digi_def.png)
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](MC_1075R/MC_1075R_meas.png)
### 3.1. Zeitaufnahme mit Multi-Anforderung:
- 1000ms:
  ![image](MC_1075R/1000ms.png)
- 500ms
  ![image](MC_1075R/500ms.png)
- 250ms:
  ![image](MC_1075R/250ms.png)
- 200ms:
  ![image](MC_1075R/200ms.png)
- 150ms (Antwortsperiode: 150ms):
  ![image](MC_1075R/150ms.png)
  ![image](MC_1075R/150ms_zoom.png)
- 120ms (Antwortsperiode: 240ms):
  ![image](MC_1075R/120ms.png)
  ![image](MC_1075R/120ms_zoom.png)
## 4. Ergebnis:
|Zeit|Typ|Min|Max|Ist|
|:-:|:-:|:-:|:-:|:-:|
|T1|-|2 ms|40 ms|166 ms|
|T2|21 us|-|-|112 us|
|T3|100 us|-|-|104 us|
|T4|100 us|-|-|136 us|
|T6|-|-|77 ms| 150 ms|
|T7|-|19 ms|57 ms|183 ms|
Datei sind plausiebel.
Antwortzeit für Tastendruck ist auch ohne Verzögerung.