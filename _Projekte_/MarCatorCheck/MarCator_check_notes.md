[[MarCatorCheck_meetings]]
[[MarCator_Prod_process.canvas|MarCator_Prod_process]]


Current Topics:
- INI-file with measurements, xls and ini
- Current procedure - pdf
- pinola drop at hold
- radio test
- setting artcle number
Next:
- tests
- securyty - double check Sn AN and config
- test result passed??
- radio test

Version 5.0:
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
	- dialog that configuration has been finished

Q:
- what Tolerance settings ?
- whether to check if AN an SN is set correctly???
- check if sn is empty before?
- enable auto config only when qr code was scanned???
- check if sn and an is correct











MarCator Check todo:
- [x] przeniesc checkboxa pod sn - i nie pokazyac dla innych typow
- [x] dodac parametr do ini
- [x] dodanie listy do testow (qr cody)
- [ ] sprawdzic dla innych zegarow jak to dziala (czy nadal poprawnie)
- [ ] porownac z tym co bylo - static code analysis
- [ ] czas zwloki na ustalenie pomiarow - poexperymentowac ??? - lepsze pomiary
- [ ] ~~sprawdzanie na koncyu czy dane sie zgadzaja (sn i an)
- [x] zaslanienie dla nie MC touch
- [ ] dopisac??? czy nowe
- [x] ukryc checkbox dla innych
- [ ] poczatek, spada czasami - moze porozmawaic z Jensem
- [ ] sprawdzanie czy pole nie jest puste i czy skanowanie mialo miejsce ???

other:
marcator not ready - happends
??? replace  repead-y with timer
