
Changes in FW v0.5:

- 48507 - LED flash time in Tolerance mode editing (with DK-U1 and ANT communication)
	 - time Settings: 1, 2 or 3 seconds
	 - when switching Green LED simulates flash time length
	 - when Cable connected with supply, LEDs will glow in tolerance Active permanently
![[2023-11-06_10h26_51.png]]
- 48508 - Measurement direction setting using DK-U1 and ANT:
	- DK- U1 (cable connection) : **CHA+** (direction inwards), **CHA-** (direction outwards)
	- ANT (radio connection):  Byte4: 'H', Byte5: '+' (direction inwards), **'-'** direction outwards

- 48509 - Order in Menue: first preset then tolerance
![[2023-11-06_10h31_20.png]]
- 48565 - (Toleranzfeld in analoger Skale einstellbar) Switching tolerance scaling in analoge scale for larger range 
![[2023-11-06_10h36_03.png]]
- splash screen "Hello" with name and FW version on start and Factory reset
- ![[2023-11-06_10h25_35.png]]