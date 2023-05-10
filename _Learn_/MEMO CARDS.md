cards:
- RTOS https://wiki.segger.com/embOS, https://www.segger.com/doc/UM01001_embOS.html, https://www.segger.com/products/rtos/embos/, https://slashdot.org/software/real-time-operating-systems-rtos/
	- pros and cons: https://medium.com/@lanceharvieruntime/the-pros-and-cons-of-rtos-vs-bare-metal-which-will-you-choose-756e33ba6df7
	- 
- litle endian: ARM LSB - MSB, od prawej do lewej - odwrotnie niz zapis, big endian ethernet MSB - LSB
	- big endian: (MSB)02 ff (LSB): Byte0: 0x00, Byte1: 0xff - ethernet, power PC, Moto 68000 ( big numebr first) (Mortorola)
	- little endian: (MSB)02 ff (LSB): Byte0: 0xff, Byte1: 0x00 - ARM, x86, AMD, (german counting, little number first) HW simplier to design due to type size 8 16 32 64 (Intel)
- c code for direct memory address access: ` *((volatile unsigned int*)0x12345678) `
- volatile
- Modbus protokol komuniaczjnz (RTU, ASCII, TCP)
- hex dump in cmd for viewing flies in hex format Bare metal courses: (https://www.youtube.com/watch?v=7lcY5tcP_ow)
- cat a.hex - view a hexfile
- copy as a path name - file in mac or win holding cmd or alt
- passing function as param:  https://stackoverflow.com/questions/9410/how-do-you-pass-a-function-as-a-parameter-in-c
```c
void func ( void (*f)(int) );
```

- SOLID: 
