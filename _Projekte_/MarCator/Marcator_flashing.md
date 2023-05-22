# 1. Programming interfaces:

![[open_cover_mark_r.png]]
# 2. Programming tools:
2.1. MSP430 programmer: MSP-FETFlash

![[programmer_r.png]]
2.2. MSP430 Flashing cable: Tag-connector MSP430:
![[Tag-connect-msp_r.png]]
2.3. ISP1507 flashing tool: Segger J-link:
![[segger-j-link_r.png]]
2.4. ISP1507 flashing cable with adapter:
![[Tag-connect-nrf_r.png]]
---
# 3. Programming software:
3.1. FET-Pro430 `\\essfs01\Abteilungen\Entwicklung\Elektronik\Software\Programming\FET-Pro430-3v43-Setup`
![[FET-Pro430.png]]
3.2. nRFgo Studio `\\essfs01\Abteilungen\Entwicklung\Elektronik\Software\nrfgostudio_win-64_1.21.2_installer.msi`
![[nRFgo-studio.png]]
---
# 4. Firmware
4.1. Main chip FW:  `\\essfs01\Abteilungen\Benutzergruppen\Firmware_Software\Firmware\MarCator Touch 1087BR\Main`
4.2. Touch Chip FW: `\\essfs01\Abteilungen\Benutzergruppen\Firmware_Software\Firmware\MarCator Touch 1087BR\Touch`
4.3. Radio Chip FW: `\\essfs01\Abteilungen\Benutzergruppen\Firmware_Software\Firmware\MarCator Touch 1087BR\Radio`

---
# 5. Flashing Main chip:
5.1. Connect MSP-FETFlash (2.1) with cable (2.2).
5.2. Open FET-Pro430 (3.1.)
![[FET-Pro430.png]]
5.3. Select FW file: `DigMC_05.hex` (4.1.)
5.4. Select Microcontroller type: `MSP430FR6989`
5.5. Press `AUTO PROG.`:
![[main_flash_prep.png]]
![[main_flash_prep_fin.png]]

---
# 6. Flashing Touch chip:
6.1. Connect MSP-FETFlash (2.1) with cable (2.2).
6.2. Open FET-Pro430 (3.1.)
![[FET-Pro430.png]]
6.3. Select FW file: `Touch_MarCator_01.hex` (4.2.)
6.4. Select Microcontroller type: `MSP430FR2633`
6.5. Press `AUTO PROG.`:
![[touch_flash_prep.png]]
![[touch_flash_prep_fin.png]]

---
# 7. Flashing Radio chip
7.1. Connect MSP-FETFlash (2.1) with cable (2.2). with main chip and keep connected (for power supply only)
![[FETPro430_power.png]]
7.2. Connect Segger J-Link (2.3) with cable (2.4).
![[radio_chip_connection.png]]
7.3. Open nRF-Studio go (3.2.)
![[nrfstudio.png]]
7.3. Select nRF5x Programming
7.4. Select `Program application` and application FW: nrf52832_xxaa_2000wi.hex (4.3.). Press Programm:

6.4. Select Microcontroller type: `MSP430FR2633`
6.5. Press `AUTO PROG.`: