---
title: How to setup a DT2011B Data Logger with a VW piezometer
category: DATA LOGGERS
modified: Thu, 8 Jul, 2021 at  3:48 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000264705-how-to-setup-a-dt2011b-data-logger-with-a-vw-piezometer
article_id: 63000264705
---

# How to setup a DT2011B Data Logger with a VW piezometer

Scenario: Customer needs to setup a RST DT2011B Data Logger with a RST VW Piezometer

Solution: Follow the steps in the guide below to do the job.

When connecting the VW piezometer wires to the data logger, the wires should be connected to the proper terminal positions on the terminal block.

SH – Shield wire

C2 – Black wire

C1 – Red wire

T2 – Green wire

T1 – White wire

There is a Youtube video available https://www.youtube.com/watch?v=a5hHQaN1NkI that demonstrates the process.

Connect to the DT2011B Data Logger with DT Logger Host Software. On the Connections tab, choose Options&gt;Advanced to set the battery type and initialize the battery. This should also be done when the battery is changed. Check the Use Resistance Scaling box. Make sure to remove the battery tab from the data logger before leaving the site as the data logger will run off the power supplied by the USB cable until it is disconnected.

If desired, change the header to the serial number of the piezometer that is connected or to the prefered description.

If desired, click in the Display Format button to choose the decimal digits.

To check the current readings, go to the Monitor tab and wait for it to update.

To set the data logger collection interval, go to the Logger tab.

When logging onto the data logger, the Status screen is the first to appear. It will display programmed information and show the current state of the data logger and battery information. To download the data from the data logger, click on the Collect Data button. The data is stored in the directory designated in the Connections tab, this can be changed by the operator.

Press Collect Data button to get data from the DT Logger memory, then either Append or Overwrite data to existing data records in the PC data files.

Press on View Recent file to view recently downloaded data in Data Viewer.

Use Normal (1200Hz-1550Hz) sweep settings.

Check Engineering Units and choose the Linear or Polynomial Method (chosen by the operators preference) these values are on the Calibration Record for the piezometer. The C value is calculated using the initial B Unit, Temperature and Barometric readings taken before the piezometer is installed.

Check the Temperature Correction box and input the values from the calibration record for the piezometer.

Choose the Units Conversion box and choose your prefered units, Input Units are the designated units noted on the Calibration Record (kPa or MPa), but Output Units can be chosen by the operator.

Set the preferred interval

Choose the start time for the data logger to collect the first reading. (it is a good idea to take some preliminary readings at 1 minute intervals to verify it is working correctly. Sync to Interval will start the data logger at midnight. The operator can choose a specified Start Time or Start Now.

The clock can be synced to the computer or manually set.

Memory Options will allow the data logger to overwrite older data or stop when it is full.

For any changes to be programmed, the operator must press the Apply Settings button.

Scenario:

Solution:

Make sure to remove the battery tab from the data logger before leaving the site as the data logger will run off the power supplied by the USB cable until it is disconnected.

[Image: Diagram

Description automatically generated]

[Image: Graphical user interface, text, application, email

Description automatically generated]

[Image: A screenshot of a cell phone

Description automatically generated]

[Image: A picture containing screenshot

Description automatically generated]
