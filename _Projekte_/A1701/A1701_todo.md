- [ ] interface do symulacji zewnetrzny, np vcom
- [ ] def values - recap (MRange - used for testing is 1000)
- [ ] speed up test - Test flow
- [ ] przetestowac Wavelight czy dziala poprawnie
- [ ] dokonczyc symulacje switchy

in code:  replace:
switch for absolute position instead of relative 
```
#define U200G           0x03 // should be split ... todo
#define U200F           0x01
//Zero Point
#define ZeroP100        U200G // U200G
#define ZeroP20         U200F // U200F
#define ZeroP5          0x00 // none

proposal:
#define U200G           0x00
#define ZeroP100        U200G + U200F
```
add functions for setting switches to be easy adopted by simulation
one table with settings for dev and separate with values for simulation or:
- using "config" variable for simulation with multiplier and bitmap mask

??? struct for simulation only:
- number ( position in )
- designation- name 