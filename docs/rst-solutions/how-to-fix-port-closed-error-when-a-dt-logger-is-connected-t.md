---
title: How to fix “Port Closed” error when a DT Logger is connected to DT Logger Host
category: DATA LOGGERS
modified: Mon, 26 Aug, 2024 at  9:43 AM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000264669-how-to-fix-port-closed-error-when-a-dt-logger-is-connected-to-dt-logger-host
article_id: 63000264669
---

# How to fix “Port Closed” error when a DT Logger is connected to DT Logger Host

Scenario: normally when the DT Logger is connect to the PC running DT Logger Host software, upon launching it will try to connect to the logger using current communication settings. Once connected, the port and status indicators turn green and the Status screen should display logger information.

However, there are cases it will not do and the following error "Port Closed " shows up.

Solution: The connection status is displayed on status bar. If the connection fails (status indicators are red or yellow, or status screen shows no status data), take note of the message and number displayed, then find the corresponding description in the below guide.

If the host computer doesn't have serial port, the USB to serial adapter can be used to connect to DT2011 single channel data logger.

Note: Most USB to serial adapters need drivers to be installed. Consult your adapter manual for detailed instructions.

Microsoft Windows system assigns serial communication port to the USB to serial port adapter. To check the port number:

·Click on Start and search Device Manager

·Click on Open under Device Manager.

·Expand the Ports (COM &amp; LPT) branch

·Take note of the COM port number assigned to the USB adapter.

For example, Control Panel view, see the screenshot below.

USB to Serial Port Adapter entry in control panel

In the above example, port #15 was assigned to USB Serial Port.

The problem could be the communication port is being used by some other application. For example, the Bluetooth is opened and using the USB COM Port 10 &amp; 11.

Solution: Close other windows applications that might be using serial port assigned to the Logger.

In the case of Bluetooth application, close the Bluetooth application by selecting Off in the Bluetooth settings.

Restart the DT Logger Host software to reconnect the DT Logger and the Status will show Connected to the DT Logger if the port is not used by other applications.

Problem 2: Connecting to the logger message continuously displayed.

Solution: Verify that the communication cable is connected and connections are tight. Replace logger batteries with fresh set.

Problem 3: State Errors, Reading Errors, Memory Read Errors.

Solution: Check the battery status on the Status screen on DT Logger Host; replace if necessary. Check cable for damage. Replace communication cable if in doubt.

The following table lists the status bar messages with descriptions.

Status Message

Description

Communication port open

Communication port is open

Unable to open communication port

Some other application is using this port

Connecting to the logger

DT Logger Host is trying to connect to the logger

Connection not established

DT Logger Host was unable to connect to the logger

Connection established to the logger

DT Logger Host was able to connect to the logger

Reading logger settings

All logger settings are copied to the DT Logger Host for display

Error during settings read

Error occurred during settings read

Idle

Idle time between status or data reads

New logger detected

Logger exchanged with another logger; DT Logger Host reset

Logger settings successfully read

All logger settings were successfully transferred to DT Logger Host

Error reading logger settings

Error occurred during reading logger settings

Connection Error

Connection attempts timed out

Reading logger memory

Logger memory contents is being copied to the DT Logger Host

Writing logger settings

All displayed settings are being transferred to the logger

Error during settings write

Error during settings write

Scenario:

Sol

ution:

Solution:

Problem 2:

Solution:

Problem 3:

Solution:
