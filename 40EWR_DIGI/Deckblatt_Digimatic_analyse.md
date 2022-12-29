# Digimatic Schnittstelle analyse

Datum: 29.12.2022
Schnittstelle: Digimatic
Interface: kabel DK-D1, ..., ...


## Getestete Geraete:
1. [Mikromar 40EWR](Micromar_40EWR/40EWR_Digimatic_analyse.md) ([open pdf](Micromar_40EWR/40EWR_Digimatic_analyse.pdf))
2. Micromar 40EWR-L [Dokument](Micromar_40EWR-L/40EWR-L_Digimatic_analyse.md)
3. 25EWR (18EWR/E)
4. MarCator 1075R
5. MarCator 108x [Dokument](MarCator_108x/MC_108x_Digimatic_analyse.md)
6. MarCator Touch (Prototyp)
7. Millimess Touch 2001W
8. Millimess Touch 2000W
9. C1200
10. C1202

## Ergebnis, 6-stellige Digimatic Uebertragung
| **Geraet**                | T1 [ms] | T2 [ms] | T3 [ms] | T4 [us] | T6 [us] | T7 [us] | bemerkung                |
|---------------------------|---------|---------|---------|---------|---------|---------|--------------------------|
| min                       | 2       | -       | -       | -       | -       | -       |                          |
| typ                       | -       | 21      | 100     | 100     | 77      | 57      |                          |
| max                       | 40      | -       | -       | -       | -       | -       |                          |
| **25EWR (18EWR/E)**       | 200     | 112     | 104     | 136     | 450     | 216     | stabil                   |
| **MarCator 1075R**        | 166     | 112     | 104     | 136     | 150     | 183     | stabil                   |
| **MarCator 108x**         | 165     | 112     | 104     | 119     | 150     | 181     | stabil                   |
| **MarCator Proto**        | 20      | 19      | 106     | 105     | 90      | 32      | stabil                   |
| **Micromar 40EWR**        | 0,6     | 21      | 105     | 110     | 1200    | 13      | unter 1 sekunde unstabil |
| **Micromar 40EWR-L**      | 0,8     | 21      | 104     | 108     | 1200    | 13      | unter 1 sekunde unstabil |
| **C1200**                 | 35      | 71      | 105     | 97      | 70      | 49      |                          |
| **Millimess Touch 2001W** | 10      | 19      | 106     | 104     | 100     | 22      |                          |
| **Millimess Touch 2000W** | 4       | 19      | 106     | 104     | 100     | 16      |                          |


## Ergebnis, 8-stellige Digimatic Uebertragung
| **Geraet** | T1 [ms] | T2 [ms] | T3 [ms] | T4 [ms] | T6 [ms] | T7 [ms] |
|------------|---------|---------|---------|---------|---------|---------|
| **min**    | 0       | 0,1     | 0,1     | 0,1     | -       | -       |
| **typ**    | -       | -       | -       | -       | -       | -       |
| **max**    | 200     | 0,3     | 0,3     | 0,3     | -       | -       |
| **C1202**  | 0,005   | 0,006   | 0,07    | 0,06    | 10      | 7,4     |