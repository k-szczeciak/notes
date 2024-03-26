- [x]  create a branch
- [x] update docs and update module
- [ ] curve detection:
	- [ ] ??? remove curve - then edition is possible
	- [ ] no editing of the parameters is possible
	- [ ] ??? activation and deactivation is possible  but no edition of parameters is possible
	- [ ] 
- [ ] read values
- [ ] perform calculations
- [ ] display values - new menue

Q:
- reference point is active? should it be done before calibration


``` engler, thomas: 22.01.2024:
Hallo Herr Kamper,

Stefan war heute Morgen bei mir und wir sind den Prozess anhand ihrer Beschreibung praktisch durchgegangen. Durch die extrem geringen Abweichungen schon ohne Korrektur (die verwendete 865 ist sehr genau in der Übertragung) können m. M. nach nur die Kollegen aus Providence beurteilen, ob es ausreichend funktioniert. Für das Programm haben wir noch 2 sinnvolle Ergänzungen identifiziert:

1. um die einzelnen Positionen besser anfahren zu können, sollte der Wert immer relativ angezeigt werden, also am ersten Korrekturpunkt Null setzten
2. active correction box und Reference sollten immer gleiche Zustände haben, unabhängig ob in der Korrektur oder im Überprüfen gearbeitet wird
3. es wird ein Installationsfile mit den FDTI Treibern benötigt

Punkt 1 macht Stefan nach seinem Urlaub, 2 u. 3 noch heute und lädt das File zu Ihnen hoch.

Die Anleitung ist super. Nur kleine Ergänzungen von meiner Seite:

1. hier würde ich die Versionsnummern der Firm / Software mit aufschreiben ab welcher Version es funktionieren sollte:

![](file:///C:/Users/SZCZEC~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

Beispiel von heute:

Version VPP 1.1.8

N1700  1.02-9

DLL 1.02-12

2. 4.1 Record the Correction Points – Calibrate: hier würde ich auf die Möglichkeit vorher über „Clear calibrate“ alte Werte zu löschen. Mich hat es etwas verwirrt das die Felder schon gefüllt waren bvor die Korrektur begonnen hat.

3. After recording the last correction point, please save the data to the N 1702 VPP module by
4. pressing the button save, afterwards you can activate check the “Activate Correction” checkbox. Das Gelbe scheint nicht zu passen.

5. 4.2 Verify the Calibration: Hier würde ich zur Sicherheit auch noch mal darauf verweisen, dass die Taster referenziert sein müssen.

Dann bitte zusammen mit dem Installationsfile über Herrn Stockburger oder Herrn Sonsalla nach Providence schicken.

Danke
```

```
anbei der aktualisierte Befehlssatz und eine erste Version der neuen Firmware V1.1.8 (MarNet_1_18).

Folgendes wurde implementiert:

- Befehl ‚C‘ mit Parameter 18 für Speicherung der Periode  (Mit dieser Periode wurde die Korrektur aufgenommen)
- Befehl ‚C‘ mit Parameter 19 für Korrektur (in)aktiv, Korrektur mit Bezug zum Referenzpunkt, Interpolationsfaktor für Korrektur
- Befehl ‚C‘ mit Parameter 17 für Korrekturpunkte bestehend aus Sollwert und Abweichung
- Alle Parameter werden im Info-Segment A nichtflüchtig gespeichert
```


```
Hier noch ein Auszug aus der Firmware von 817CLT für die lineare Interpolation im Anhang.

  
Mit freundlichen Grüßen | Best regards,  
**  
Nico Kamper  
**R&D Precision Gages  
Mahr GmbH  
Phone: +49 (551) 7073-99692

**Von:** Kamper, Nico <[Nico.Kamper@mahr.com](mailto:Nico.Kamper@mahr.com)>  
**Gesendet:** Donnerstag, 14. Dezember 2023 13:34  
**An:** Stefan Ocker <[stefan@ocker.de](mailto:stefan@ocker.de)>; Szczeciak, Krzysztof <[Krzysztof.Szczeciak@mahr.com](mailto:Krzysztof.Szczeciak@mahr.com)>  
**Cc:** Engler, Thomas <[Thomas.Engler@mahr.com](mailto:Thomas.Engler@mahr.com)>  
**Betreff:** AW: Millmar N1702 VPP - Abschätzung Implementierung Korrekturpunkte

Hallo zusammen,

nachfolgend das Protokoll unserer letzten Besprechung.

- N1700 Software:

- Nutzung der Costumer Calibration
- Anzahl der Punkte bis max. 11 und nur Kanal 1 (keine Unterschied zwischen Kunden und Werkskorrektur, nur ein Speicherbereich)
- Protokoll wird für **Sollwert** und **Abweichung** Werte lesen und schreiben wird ergänzt bis Ende der Woche und ggf. Periode oder Interpolation
- Eingabe der Korrekturpunkte nur in N1700 Software:

- Über das Menü Customer Calibration => Button Calibrate
- Anzeige der Korrekturpunkte in Liste (ggf. zuvor vorhandene) und Start der Aufnahme eines Punktes über Button "Start"
- Eingabe des Sollwertes über Tastertur in mm oder inch
- Eingabeformat in aktuell eingestellter Auflösung (Interpolation/Periode)
- Liste von Sollwerten kann auf dem PC gespeichert oder geladen werden (ggf. nachrüsten)

- Wenn der Kunde die Korrektur einschaltet

- Es wird ein Bit genutzt, um die Korrektur zu aktiveren (ähnlich induktiv Kunden bzw. Werkskorrektur)
- Setup sperren, bzw. Inhalt ausgrauen und ggf. Meldung bringen (Modus Korrektur, Werte nicht verändern)
- Korrektur einschaltbar, nur wenn Korrektur vorhanden ist

- Wenn der Kunde die Korrektur ausschaltet

- Werte bleiben erhalten (falls neu eingeschaltet wird)

- Code von 817CLT wird herausgegeben

- C1202:

- Erkennung, ob Korrektur aktiviert ist
- Werte lesen und verrechnen (nur Kanal 1)
- Wenn Korrektur aktiv => Einstellungen sperren und ggf. Hinweis
- Korrektur aktivierbar und deaktivierbar machen (beim aktivieren ggf. Meldung bringen)

- Nur aktivierbar, wenn Werte verfügbar
```