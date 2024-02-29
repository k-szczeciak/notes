
V0.23:
- autooff timing corrected
- autooff switched off when cable connected
- ANT - Seiarl no and Art No in BCD format corrected
- ANT - version format corrected
- Hold logo after autooff when
- all messages with the same timing 1 sec
- Irregular Blinking at value edition in menue
- "mm" symbol in menue applied in correspodning places
- LED-t 0 time added with blinking at warning
- Enhance automatic resolution switching (maxResolution):
	- in menue when switching unit, between preset
	- applies to preset and tolerance values, currently selected
	- extended to inch - more thersholds
	- in measurment
	- in resolution selection, highest possible
	- scaling back mus be done manual
	- resolution request evaluation
- Inch max value limit with extended Error message:
	- max for inch 393.7007
- Inch editing correction
- mm rounding down when boundaries values given and displayed in menue and measurements
- OL for over Value in display
- removed battery measurements - to be placed in service mode
- "F" symbol evalued for consistensy and proper display in Display test
- Battery icon evaluation  - now visible in displaytest
- "Ghosting" marker removal
- Factor setting 0.0 error with exit to main menue and previous value return
- Marker blinking at Tolerance when Hold - fixed
- corrected analog display
- battery on restart values corrected:
	- radio automatic reconnection possible
	- eco mode, Sensitivity, direction, button delay, .. 


ToDo:
- bugfixes:
- digimatic inch
- 




V0.22
EWR corrected

V0.21 EWR update

V0.20:
- scale 2
- setting values with probe
- uMaxum new Art


V11 (14.08.2023)
- pressing Data Btn search/reconnect
- turning on - search/reconnect
- corrected in menue reconnection and new connection: (additional timeout flags for no reply confirmation and connection time out)
	- correct icon in menue showed
	- reconnection possible after timeout when number is given
- poprawa przelacania stanow i statusow dla radia:
	- high current consumption in some sates
- corrected current connsumption in modes:
	- offset after first on - off (20 uA)
	- offset when radio on and disabled (20uA) when blink slow, not in search mode, curren will remain +20uA duer to active connection
- corrected port config in switching on and off
- switching off when searching and pairng peak current resolved after voltage drop measuring
- powering on voltage drop resolved by delay time for stabilisation
- timeout in menue is active