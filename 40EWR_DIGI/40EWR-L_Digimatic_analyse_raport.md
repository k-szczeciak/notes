# 40EWR-L digimatic schnittstelle pruefung
![image](img/IMG_3612.JPG)
## 1. Messaufbau:
### 1.1. 40EWR-L (art.: 4157021, sn.: 22100002)
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
![image](img/40EWR_meas.png)
### 3.1. Zeitaufnahme mit Multi-Anforderung:
![image](img/40EWR_multi.png)
<br><br>
## 4. Ergebnis:
Zeiten in Bezug zum Datenblatt sind in Normen außer 2 (3) punkten:
### 4.1. CLOCK-signal startet bevor DATA (T2_1 ist -3,66 ms)
![image](img/40EWR_CLOCK.png)
### 4.2. Wenn REQUEST ist schneller als ca. 816 ms wird keine Datei geschickt (T6).
![image](img/40EWR_MULTI_REQ.png)
### 4.3. T7 ist bisschenkurz aber kleine abweichung.  
![image](img/ergebnis.png)