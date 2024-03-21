V0.25: (21.03.2024)
- parametrs
	- normalized
	- automatic generated
	- adjsuted for states [[parameters]]
- HR timing optimization in menue
- Removed Setting with sensor in menue
- fixed refresh rate in Menue across all models (battery saving)
- HR - startup value after battery on (low pass filter adjustment)
- TOLW corrected
- Setting up Radio in menue Corrected:
	- return to OFF if left in initializatio state
	- error 255 removal
- CDT1 - coniuous measurment - corrected and adjusted for timing:
	- 20 Hz in 1086, 1087 HR (after filter), BR in measurment (64 / 3 = 21Hz)
- RES1 for HR mode corrected
- "OL" in Cable and Radio sending ERR0 command or 'E' '0' respectively
- added new commands for cable communication:
	- PRA(x) and PRA?
	- LCK?
	- DEL
	- SEN
	- new Prameter handling routine
- New command fro radio: 's' for inverted analaog scale
- changind Preset with cable will show confirmation "Prx"
- LED-T time 0 correction (no flash)
- Version in cable and radio corrected "VER?"
- New battery value reply: now reply to "BAT?" is voltage: BAT 0.000 V (last read value)
- new Service mode added for battery menue activation
- Battery menue activation with command "SRV 0" and in menue First lock menue , button 1 long press
- no sensor detection, new message: "no SEnS"
- manual display test added: when no sensor detected and pressed button 5 after power on
- "MOD?" adjusted:
	- for BR: "Start", "Stop" and "RUN" states added
	- DIF added for 1087
- Reversed scale enhanced:
	- blinking at ends
	- instand change after button pressed (PRE and RST), TOL with delay only when to button delay time active
- FA lock function bemoved when battey reset
- battery measurement (ppt dokument):

current measurement:
	- std 86: 72 in act 74 in menue 11 off
	- hr: 170 in act, 76 inmenue, 11 off


V0.24: (01.03.2024)
"some more fixes: HR, refresh rate, service mode, Hold and cable icons"
- Service mode for activating messages
- Menue refresh rate in to be constant - prevent to high current consumption in menue
- Removed Cable Icon in menue
- fixed: HR refreshrate
- 1086 - STD: 75, 12uA, HR: 150/12uA, in menue Alle 70uA
- "HOLD" symbol in Menu Radio settings: Active when Radio is Off

V0.23:
- Menue LED-t and Scale - Lock with DKU1
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
- fix: Editing PRIII - will not jump directly to Measurement
- Animation enhaancement for Scale in menue - timer based independent on refreshrate
- one battery measurement for all variants bsaed on voltage divider
- Analog scale:
	- fix: MIN needle display not visible
	- blinking always when 2 indicators ar in the same place with Tolerance, possible both bling Tolerances
	- reconstruction of model
	- clean up and functions refactoring
- battery power on cleanup and refactor:
	- all parameters evaluation , i.e. Resolution evaluation based on Art No moved to functions
	- comments cleanup


ToDo:
- bugfixes and updates:
	- err 255 
	- Battery Voltage over DKU1
	- HR- start value - filter starts
- digimatic inch
- 844 EWR:
	- hysteresis (preset)
	- adjustment values
	- test hysteresis with inch
	- menue hysteris remove
	- mapping buttons for editing
	- variable settings with measurement system depending on art (diff length)
- CDT1 - 
- TOLW 2 digits evaluation not one only
- in Menue LCD flickering
- slower refresh in menue for current consumption
- uMaxum - waiting for decisions:
	- names




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