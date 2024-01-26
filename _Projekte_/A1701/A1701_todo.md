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
// Range 
#define U200B           (1 << 0)
#define U200C           (1 << 1)
#define U200D           (1 << 2)
#define U200E           (1 << 3)
// Zero Point:
#define U200F           (1 << 4)
#define U200G           (1 << 5)
// Filter:
#define U200H           (1 << 6)
#define U200I           (1 << 7)
#define U205B           (1 << 8)
//Output
#define U205C           (1 << 9) // range
#define U205D           (1 << 10) // offset 5V
#define U205F           (1 << 12) // offset 2x
// Output:


#define ZeroP100        U200G + U200F
```
add functions for setting switches to be easy adopted by simulation
one table with settings for dev and separate with values for simulation or:
- using "config" variable for simulation with multiplier and bitmap mask

??? struct for simulation only:
- number ( position in )
- designation- name 