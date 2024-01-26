- [ ] interface do symulacji zewnetrzny, np vcom
- [ ] def values - recap (MRange - used for testing is 1000)
- [ ] speed up test - Test flow
- [ ] dokonczyc symulacje switchy

in code:  replace:
```
#define U200G           0x03 // should be split ... todo
#define U200F           0x01
//Zero Point
#define ZeroP100        U200G // U200G
#define ZeroP20         U200F // U200F
#define ZeroP5          0x00 // none
```
add functions for setting switches to be easy adopted by simulation
struct:
- number ( position in )
- designation