- [x]  create a branch
- [ ] update docs and update module
- [ ] read values
- [ ] display values - new menue

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