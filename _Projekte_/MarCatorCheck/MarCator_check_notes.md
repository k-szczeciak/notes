

MarCator Check todo:
- [x] przeniesc checkboxa pod sn - i nie pokazyac dla innych typow
- [x] dodac parametr do ini
- [ ] dodanie listy do testow (qr cody)
- [ ] sprawdzic dla innych zegarow jak to dziala (czy nadal poprawnie)
- [ ] porownac z tym co bylo - static code analysis
- [ ] czas zwloki na ustalenie pomiarow - poexperymentowac ??? - lepsze pomiary
- [ ] ~~sprawdzanie na koncyu czy dane sie zgadzaja (sn i an)
- [x] zaslanienie dla nie MC touch
- [ ] dopisac??? czy nowe
- [x] ukryc checkbox dla innych
- [ ] poczatek, spada czasami - moze porozmawaic z Jensem

other:
marcator not ready - zdarza sie czasami
??? zamienic repead-y


!!!

- potwierdzenie ze sie zrobilo kalibracje
- sprawdzanie cz jest juz numer An, jezeli jest to nie bedzie programowane ???



MCC finished:
- procedure for new MC (touch):
	- communication duplex
	- evaluation after "(Touch)" string
- antasten (Touch) for MC:
	- zeroing value before movement
	- finding beginning from bottom
	- ride to 0,2 mm
	- zeroing
	- move to test procedure as for previous MC-s
	- Timeout for procedure 2x messages
- added "Autoconfig" checkbox for configuration
	- autohide if not relevant (not for other than Touch MC's)
	- with Hint
	- saved in INI-file
- device configuration before calibration:
	- dialog for confirmation of configuration - abort possible
	- dialog after abord to proceed calibraction w/o configuration
	- sending Serial number
	- sending Article number
	- dialog that configuration has beeb 

Q:
- czy po nie udanym pomiarz wycofac ???
- Jakie nastawy do poszczegolnych programow