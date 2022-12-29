# Digimatic Schnittstelle analyse

Datum: 29.12.2022
Schnittstelle: Digimatic
Interface: kabel DK-D1, ..., ...


## Getestete Geraete:
1. [Mikromar 40EWR](Micromar_40EWR/40EWR_Digimatic_analyse.md) 
2. [Micromar 40EWR-L](Micromar_40EWR-L/40EWR-L_Digimatic_analyse.md) ([open pdf](Micromar_40EWR-L/40EWR-L_Digimatic_analyse.pdf))
3. [25EWR (18EWR/E)](24EWR/../25EWR/25ERW_Digimatic_analyse.md)
4. MarCator 1075R
5. [MarCator 108x](MarCator_108x/MC_108x_Digimatic_analyse.md) ([open pdf](MarCator_108x/MC_108x_Digimatic_analyse.pdf))
6. MarCator Touch (Prototyp)
7. Millimess Touch 2001W
8. Millimess Touch 2000W
9. C1200
10. C1202

## Ergebnis, 6-stellige Digimatic Uebertragung
| **Geraet**                | img     | T1 [ms] | T2 [ms] | T3 [ms] | T4 [us] | T6 [us] | T7 [us] | doku          |
| ------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------------ |
| min                       |         | 2       | -       | -       | -       | -       | -       |              |
| typ                       |         | -       | 21      | 100     | 100     | 77      | 57      |              |
| max                       |         | 40      | -       | -       | -       | -       | -       |              |
| **Micromar 40EWR**        | ![i][5] | 0,6     | 21      | 105     | 110     | 1200    | 13      | [doku][11] |
| **Micromar 40EWR-L**      | ![i][6] | 0,8     | 21      | 104     | 108     | 1200    | 13      | [doku][12] |
| **25EWR (18EWR/E)**       | ![i][1] | 200     | 112     | 104     | 136     | 450     | 216     |     |
| **MarCator 1075R**        | ![i][2] | 166     | 112     | 104     | 136     | 150     | 183     | stabil       |
| **MarCator 108x**         | ![i][3] | 165     | 112     | 104     | 119     | 150     | 181     | stabil       |
| **MarCator Proto**        | ![i][4] | 20      | 19      | 106     | 105     | 90      | 32      | stabil       |


| **C1200**                 | ![i][7] | 35      | 71      | 105     | 97      | 70      | 49      | stabil       |
| **Millimess Touch 2001W** | ![i][8] | 10      | 19      | 106     | 104     | 100     | 22      | stabil       |
| **Millimess Touch 2000W** | ![i][9] | 4       | 19      | 106     | 104     | 100     | 16      | stabil       |


## Ergebnis, 8-stellige Digimatic Uebertragung
| **Geraet** | img      | T1 [ms] | T2 [ms] | T3 [ms] | T4 [ms] | T6 [ms] | T7 [ms] |
| ---------- | -------- | ------- | ------- | ------- | ------- | ------- | ------- |
| **min**    |          | 0       | 0,1     | 0,1     | 0,1     | -       | -       |
| **typ**    |          | -       | -       | -       | -       | -       | -       |
| **max**    |          | 200     | 0,3     | 0,3     | 0,3     | -       | -       |
| **C1202**  | ![i][10] | 0,005   | 0,006   | 0,07    | 0,06    | 10      | 7,4     |


[1]: Micromar_40EWR/device_r.png
[2]: Micromar_40EWR-L/device_r.png
[3]: Micromar_40EWR/device_r.png
[4]: Micromar_40EWR/device_r.png
[5]: MarCator_108x/device_r.png
[6]: Micromar_40EWR/device_r.png
[7]: Micromar_40EWR/device_r.png
[8]: Micromar_40EWR/device_r.png
[9]: Micromar_40EWR/device_r.png
[10]: Micromar_40EWR/device_r.png

[11]: Micromar_40EWR/40EWR_Digimatic_analyse.pdf
[12]: Micromar_40EWR-L/40EWR-L_Digimatic_analyse.pdf

todo:
- [ ] dokumnety przenisc
- [ ] wykres
- [ ] linki
- [ ] ikony
- [ ] ktory 8-cyfrowy
- [ ] dodac excela
- [ ] doadac jak produkowac dokumenty