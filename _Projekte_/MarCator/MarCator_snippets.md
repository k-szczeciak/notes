wylaczenie LCD na poczatku do testow pradu:
```c
////    LCD_aus;
//    TA0CCTL0 &= ~CCIE;
//    EnterLPM;
```

```c
// testing unions and floating poinzs
//    float pi = (float)3.1415926;
//    union {
//        float f;
//        int u;
//    } f2u = { .f = pi };
//
//    char texttest[40];
//    sprintf(texttest, "pi : %f : 0x %x PRIx32", pi, f2u.u);
//    if (f2u.f > 10.0f)return;
```