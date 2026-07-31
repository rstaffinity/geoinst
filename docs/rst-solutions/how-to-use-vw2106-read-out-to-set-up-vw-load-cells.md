---
title: How to use VW2106 Read Out to set up VW Load Cells
category: VW2106: READOUTS
modified: Fri, 29 Oct, 2021 at  8:34 AM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000267721-how-to-use-vw2106-read-out-to-set-up-vw-load-cells
article_id: 63000267721
---

# How to use VW2106 Read Out to set up VW Load Cells

Start RST Readout Host Software (available on RST website under software downloads).

Turn on the VW2106 and connect to the computer with the Mini USB to USB cable.

Right click on the screen to add a new location.

You can create locations in the readout for both the Polynomial (if it was calibrated with a Polynomial) and the Linear calibration constants (Most common).

To program a location using the Polynomial Conversion, give it a name:

If there are 3 gauges in the load cell, choose 3 on the pull down and click ENG Units. If more, then choose the number. There will be between 3 and 6 gauges (see the calibration record). The standard VW Sweep is B and the Standard Thermistor is the 3K. Then click the Eng Calibration button to go to screen two.

The next screen will pop up. There are two conversion methods, Linear and Polynomial. If the load cell was calibrated with 3 polynomial values, choose Polynomial Conversion. (The most common is the Linear Calibration factor). Type in the A, B and C values from the bottom of the calibration record. Choose Force and choose Force choose the Output readings you want (default is kips).

Choose OK on this screen to go back to screen 1, it will have updated the Output Units.

To program a location using Linear Conversion, right click on the screen again and create a new location for the Linear values. The Linear Conversion will come up by default, choose the number of gauges in the load cell (3 to 6), click Eng Units and Eng Calibration.

Input the B value from the bottom of the calibration record in (Calibration Factor G) and the A value from the calibration record in (Zero Reading Ro), as they appear on the calibration record. In Units Conversion, choose Force, the Input Units (usually Kips) and the Output units of choice (Kips, kN, etc).

Click OK and OK again on the first screen. Your locations are ready to upload.

Click Upload Sites and watch the communication bar as it writes the data to the VW2106.

Once complete, unplug the Mini USB and pless enter on the VW2106 a couple times. Scroll down to ‘Monitor Settings’ and press the enter button.

Choose ‘Import From Location’ and select the appropriate location for your use by pressing the arrow key .

Connect your load cell but do not zero the readings if you are using the linear as it reads about -15.7 Kips at zero, it will get more accurate as force is applied. It is an 800 Kip Load cell so the first 10% is never very accurate. If you need more accurate readings at lower forces, it is better to choose a more appropriate rated load cell.

[Image: A screenshot of a cell phone

Description automatically generated]
