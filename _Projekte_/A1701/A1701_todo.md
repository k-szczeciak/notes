Main todos:
- [ ] def values - recap (MRange - used for testing is 1000)
- [ ] speed up test - Test flow
- [ ] przetestowac Wavelight czy dziala poprawnie
- [ ] test HW copnfig options
- [ ] dokonczyc symulacje switchy i refactor (jak ponizej, as below)
- [ ] correct version display - split to red and green (red major (1 - 7))
optional todos
- [ ] interface do symulacji zewnetrzny, np vcom

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
// Output:Components
#define U205C           (1 << 9) // Half Range
#define U205D           (1 << 10) // offset 5V
#define U205F           (1 << 12) // offset 2x
// Output:
#define HalfRange       U205C
#define Offset5V        U205D
#define OffsetD         U205F

#define ZeroP100        U205G + U205F
#define ZeroP20         U205F
#define ZeroP5          0x00

/*...*/
#define MRange
ZeroP
Filter
// for Wavelight - Output range as a separate value - 0,1,2 (wavelight)

```
wykozystac funkcje "setSwitches()" i zamienic to co jest w scene.c

other option to be considered:
- add yet another functions for setting switches to be easy adopted by simulation - but there is one
- one table with settings for dev and separate with values for simulation or:
	- using "config" variable for simulation with multiplier and bitmap mask - thats the better way

- struct for simulation only (object like with scene object placement props): - or maybe just evaluate in "setSwitches()"
	- number ( position in )
	- designation- name 
	- group