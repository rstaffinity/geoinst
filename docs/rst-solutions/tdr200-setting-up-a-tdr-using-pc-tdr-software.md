---
title: TDR200 – Setting up a TDR using PC-TDR software
category: DATA LOGGERS
modified: Tue, 20 Aug, 2024 at  1:33 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000283904-tdr200-setting-up-a-tdr-using-pc-tdr-software
article_id: 63000283904
---

# TDR200 – Setting up a TDR using PC-TDR software

When using PC-TDR software to connect to a TDR via a TDR200 interface. Start the software and connect the TDR200 using the Micro-USB cable to the USB port on the computer. Under View, select Set Default Layout to use the full screen.

To add a add a new configuration and TDR, from the drop-down menu above, click New.

Click on the TDR200 box to set the com port through which the TDR will be connected. The operator will be prompted to choose the com port and install the drivers.

When the TDR200 is connected to the computer with the micro-USB communication cable, the device will be powered.is connected. Check the ‘Device Manager’ com ports to identify the port that the TDR is connected to. The TDR200 should show up as a TDR200 in device manager, but it may not identify the same in the com port options in the PC-TDR software. In the example below, the port identified as a DT series data logger, but the port number is the important thing. If the TDR200 does not show up in the device manager, then the drivers have not been installed correctly.

Under Ports, the TDR200 is connected to port 29.

The SDM address is only changed when multiple SDMX850 or SDMX50 multiplexors are used when connected to a single Campbell Scientific data logger.

When adding devices, use the green + button and choose ‘Coaxial’.

Once the TDR has been configured, assign a Probe Name. All TDRs should have a be configured using the values listed below.

Save the TDR after setting it up under the same probe name.

Once the TDR properties are set, highlight and put a check mark in the check box on the left side of the screen for the TDR and click the refresh button.

The graph will be displayed, and the left bar will say measurement succeeded.

When saving the data files, the graph screen shots should be saved and data can be saved by Exporting the data.

Export Readings with check box to ‘append selected’.

Vp = 0.88;

Averages = 4;

Points = 2000;

Cable length = the length of cable above the surface of the borehole to the data logger;

Window Length = Length of cable grouted in the borehole.

Probe Length = 0.3;

Probe Offset = 0;

Probe Kp = 0.

[Image: A screenshot of a computer

Description automatically generated]

[Image: A screenshot of a computer

Description automatically generated]

[Image: A screenshot of a computer error

Description automatically generated]

[Image: A screenshot of a computer error

Description automatically generated]

[Image: A screenshot of a computer

Description automatically generated]

[Image: A white background with black and white clouds

Description automatically generated]

[Image: A screenshot of a computer

Description automatically generated]

[Image: A screenshot of a computer

Description automatically generated]

[Image: A screen shot of a computer

Description automatically generated]
