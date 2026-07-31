---
title: DT Logger Host - Communications Troubleshooting – (Status 0, 2 and 3 Warnings)
category: DATA LOGGERS
modified: Tue, 28 Jun, 2022 at 11:21 AM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000272922-dt-logger-host-communications-troubleshooting-status-0-2-and-3-warnings-
article_id: 63000272922
---

# DT Logger Host - Communications Troubleshooting – (Status 0, 2 and 3 Warnings)

Sometimes when attempting to connect to a data logger, the start up process will get hung up on a Status 0, 2and 3 warnings and display ‘Port Closed, might be used by another application or Port closed; Check cable. Remove all other devices connected to a USB port and try connecting again.

If Status 0 is displayed, the cable is damaged or there is no connection to the data logger at all.

If Status 2 is displayed, it could be the computer Bluetooth being enabled and interfering with the comms to the USB Port or the USB Drivers were not installed properly when the DT Logger Host was installed.

If Status 3 is displayed, the data logger may have been setup to record data at a very fast rate and the data logger is prioritizing data collection over connecting to the computer. This is most common in DT2055B and DT2040 data loggers, but it can happen in other DT data loggers as well.

5. If you are unable to communicate with the data logger, check the Ports to make sure it is connected. This is the first port connection to check.

6. The second part to a port connection is the USB Serial Converter. Both the Port and the Serial Converter must be connected to communicate with the DT data logger. If the DT data logger is not shown under Universal Serial Bus controllers, then the USB drivers must be reinstalled from the link on the RST website.

https://rstinstruments.com/product/dt-logger-host-software/ - Select Downloads to get to the link.

7. If you are unable to connect to a data logger as soon as you connect, if there is a Status 3 message displayed at the bottom of the page, the specific data logger device driver is likely not starting properly. Click on the specific data logger to restart the device driver and click Reconnect, it should connect after being selected. If it does not connect, see special instructions in section 9.

8. If Status 0 or 1 is displayed an neither of these is not working, the RST USB Driver may need to be reinstalled or updated. Normally the USB drivers are installed when the DT Logger Host is installed or updated. If the drivers need to be installed, they are available on the website on the same page as the software.

https://rstinstruments.com/product/dt-logger-host-software/ - Select Downloads to get to the link.

9. If pressing the ‘Reconnect’ button does not allow connection when ‘Status 3’ is displayed as in the screenshot below, the connection issue can be resolved by removing the lid of the data logger and removing the main battery from the data logger and disconnecting the USB cable (as it supplies power to the data logger as well). Wait for 30 seconds and connect the USB cable and wait for it to connect. Once the connection has been re-established, install the battery and securely attach the lid of the data logger.

If there are still issues connecting to the data loggers, contact RST Support by creating a support ticket from Help Desk on the RST Instruments website, or call RST Instruments at 1-604-540-1100.

There are numerous support documents available on the help desk page if a support person is not available.

Update to the latest version of DT Logger Host software from the RST Website. https://www.rstinstruments.com/rst-software/software-dt2055B

Sometimes the connection can be established by simply disbling the bluetooth from the computer desktop. If that does not work, it can be done under the device manager.

Disable the Intel® Wireless Bluetooth® by opening, then right clicking and choosing disable.

Open DT Logger Host software and try to connect with the data logger.

[Image: Table

Description automatically generated]

[Image: Graphical user interface, application, table

Description automatically generated]

[Image: Graphical user interface, application

Description automatically generated]

[Image: Graphical user interface, application

Description automatically generated]

[Image: Graphical user interface, text, application, email

Description automatically generated]
