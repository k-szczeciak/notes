## Unable to send data when Radio was not fully paired

### Issue description:
When in menue Radio pairing process was preselected but not preceeded.  
![[2023-10-03_12h41_37.png]]
Switching to next or previous menue and leaving menue, hence pairing process is possible. As result, sending data with einther touch button or button on cable isnot possible when DK-U1 calbe is connected.

### Solution:
Effect was due to internal flag: `Einst.RFMode` which was set to 2 before pairing (which is next step, by button press), which means `Radio On` and leaving menue in this state was possible. As a result data send with DK-U1 cable was blocked.

As a remedy status flag `Einst.RFMode = 2` was set only when connection was espablished. Conditions for initiating pairing is check when by button status `T5Status` (state machine in radio configuration loop) instead of `Einst.RFMode == 2`


FW file:
`DigMMess_04.hex`

