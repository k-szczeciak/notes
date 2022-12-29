# 40EWR-L digimatic schnittstelle pruefung - korrektur
![image](img/IMG_3612.JPG)
## 1. Messaufbau:
### 1.1. 40EWR-L, 25-50mm (art.: 4157021, sn.: 22100002)
### 1.2. Digimatic Kabel: DK-D1
### 1.3. Messung/Empfänger: Saleae logic Pro 8
### 1.4. Signalkonditionierung: 3VDC an DATA, CLOCK und REQUEST
![image](img/IMG_3609.JPG)
<br><br>
## 2. Interface Beschreibung
***(Datenblatt: Ba_3723295_DK-U-D_de_en_fr_es_it_zh_0322-1.pdf):***
![image](img/digi_def.png)
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
## 3. Messungen:
### 3.1. Zeitaufnahme:
![image](img/40EWR_meas_cor.png)
### 3.1. Zeitaufnahme mit Multi-Anforderung:
![image](img/40EWR_multi.png)
<br><br>
## 4. Ergebnis:
Zeiten T1, T6 und T7 sind auser Toleranz
|Zeit|Typ|Min|Max|Ist|
|:-:|:-:|:-:|:-:|:-:|
|T1|-|**2 ms**|**40 ms**|**0,8 ms**|
|T2|21 us|-|-|21,0 us|
|T3|100 us|-|-|103,9 us|
|T4|100 us|-|-|107,9 us|
|T6|-|-|**77 ms**|**~800 ms**|
|T7|-|**19 ms**|**57 ms**|**12,8 ms**|

Sonst datei sind plausiebel.
Antwortzeit für Tastendruck ist auch ohne Verzögerung.