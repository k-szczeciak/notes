[HOME](../Deckblatt_Digimatic_analyse.md)<--->[PDF](40EWR-L_Digimatic_analyse.pdf)
# 40EWR-L digimatic schnittstelle Analyse
<img src="device.png" width="400px"><br>
## 1. Messaufbau:
### 1.1. 40EWR-L, 25-50mm (art.: 4157021, sn.: 22100002)
### 1.2. Digimatic Kabel: DK-D1
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
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/meas.png)

### 3.2. Zeitaufnahme mit Zycklische-Anforderung:
- Digital und Analog:
    ![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/multi.png)
- Requesttakt: 2000ms
![image](2000ms.png)
- Requesttakt: 1200ms
![image](1200ms.png)
- Requesttakt: 1100ms
![image](1100ms.png)
- Requesttakt: 1000ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/1000ms.png)
- Requesttakt: 900ms
![image](900ms.png)
- Requesttakt: 800ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/800ms.png)
- Requesttakt: 700ms
![image](700ms.png)
- Requesttakt: 600ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/600ms.png)
- Requesttakt: 500ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/500ms.png)
- Requesttakt: 250ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/250ms.png)
- Requesttakt: 250ms Zoom
![image](250ms_zoom.png)
- Requesttakt: 150ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/150ms.png)
- Requesttakt: 150ms Zoom
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/150ms_zoom.png)
- Requesttakt: 100ms
![image](_Docs_/Digimatic_analyse/Micromar_40EWR-L/100ms.png)
- Requesttakt: 100ms Zoom
![image](100ms_zoom.png)

## 4. Ergebnis:
Zeiten T1, T6 und T7 sind auser Toleranz
| Zeit  |  Typ   |  Min  |  Max  |   Ist    |
| :---: | :----: | :---: | :---: | :------: |
|  T1   |   -    | 2 ms  | 40 ms |  0,8 ms  |
|  T2   | 21 µs  |   -   |   -   | 21,0 µs  |
|  T3   | 100 µs |   -   |   -   | 103,9 µs |
|  T4   | 100 µs |   -   |   -   | 107,9 µs |
|  T6   |   -    |   -   | 77 ms | 1200 ms  |
|  T7   |   -    | 19 ms | 57 ms | 12,8 ms  |

- 40EWR-L erst bei 1200ms stabil
- 40EWR-L, wenn Anforderungsrate ist schneller ( <250ms) antwort stabilisiert sich ca 700ms jede Antwort
- Sonst datei sind plausiebel.
- Antwortzeit für Tastendruck ist auch ohne Verzögerung.