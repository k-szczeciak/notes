radio:

| Cmd | enum      | descr                                                        |     |
| --- | --------- | ------------------------------------------------------------ | --- |
| ?   | F_DATA;   | send data                                                    |     |
| 0   | F_RST;    | reset                                                        |     |
| P   | F_PRE;    | preset: activate, read and set, deactivate                   |     |
| A   | F_ABS;    | absolute mode                                                |     |
| V   | F_VER_F;  | version                                                      |     |
| I   | F_ID_F;   | device id                                                    |     |
| S   | F_S_X;    | serial number                                                |     |
| T   | F_T_X;    | article number                                               |     |
| O   | F_OFF;    | switching off                                                |     |
| U   | F_UN_F;   | active unit request                                          |     |
| M   | F_MM;     | set up mm                                                    |     |
| N   | F_IN;     | set up inch                                                  |     |
| L   | F_LCK;    | lock                                                         |     |
| F   | F_FA;     | Factory Settings                                             |     |
| K   | F_KEY;    | Key lock function                                            |     |
| C   | F_CAL;    | Calibration date in ISO 8601 format                          |     |
| D   | F_CALN;   | next calibration date in ISO 8601 format                     |     |
| X   | F_TOL;    | tol activate or deactivate                                   |     |
| Y   | F_OTOL_X; | tol upper value                                              |     |
| Z   | F_UTOL_X; | tol lower value                                              |     |
| W   | F_TOLW;   | setting Warning and in boubnd and outbound warning           |     |
| R   | F_RES;    | resolution setting                                           |     |
| B   | F_MOD;    | Mode - need to be adjusted for device type                   |     |
| G   | F_FAK;    | Factor setting / checking                                    |     |
| H   | F_DIR;    | measurement direction change (direction in ANTmessage[5] +/- |     |
| J   | F_ST;     | start and stop - only for br type                            |     |
| l   | F_LEDT;   | leds flash time                                              |     |
| s   | F_SREV;   | reverse analog scale                                         |     |

general:
- rozdzielenie albo radio albo kabel

Radio new/rework:
- 's' - scale reverse setting
- new: bat voltage
- zapilementowac 'C'
- zaiplementowac 'D'
- poprawic 'B'
- wysylanie danych z przycisku
- mode min max spr
- ??? fix res
- ??? dipl variant
later:
- (p parameter setting )
- dane led (get set)
- (service mode)

Cable new:
- PRA x active preset
- PRA?
- FIL? - get averagiing filter 0..4 - not here
- LCK?
- DEL1, DEL0, DEL? - delay 
- SEN0, SEN1, SEN? - touch sensistivity
- CLN0, CLN1, CLN? - clean display

Later:
- devtype
- unit restr
- radioNo
- brand
- name
- czytanie parmaetrow wszystkich

remove:
- S_HR_T
- S_HR_ML
- S_HR_W

cable fix:
- CDT1
- DIF
- bat voltage

zapimplementowane:
LCD_MEM - get displ memory
S_SET_T - set keys
SRV - service mode: for battery display 
FREQ - refresh display
REBOOT

brakuje:
- get led status
- set led
- poprawic LCD aby przesylane byly zmiany natychmiast


OGOLNIE:
CSV, JSON, YAML i inne
GET method jak url z &-em


filter setting???