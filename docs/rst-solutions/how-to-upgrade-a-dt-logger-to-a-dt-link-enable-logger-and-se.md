---
title: How to Upgrade a DT Logger to a DT Link Enable Logger and setup wireless communication between DT Loggers and DT Link Hub
category: DT LINK WIRELESS DATA COLLECTION
modified: Fri, 13 May, 2022 at  4:15 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000272010-how-to-upgrade-a-dt-logger-to-a-dt-link-enable-logger-and-setup-wireless-communication-between-dt-log
article_id: 63000272010
---

# How to Upgrade a DT Logger to a DT Link Enable Logger and setup wireless communication between DT Loggers and DT Link Hub

Synopsys: When customer have a normal DT Logger and would like to upgrade it to have DT Link feature.

Following the steps below to do the upgrade and set up the wireless communication between DT Loggers and DT Link Hub

Install the DT Link Module (XBee module in the DT Logger as shown below.

Connect the antenna cable from the Xbee Module to the antenna on the DT Logger Housing.

Connect DT Loggers to DTLink Wireless Hub using DT Loggers Host Software

Connect the DTLink Logger and DTLink Wireless Hub to the PC running DT Logger Host Software via USB Cables and open the DT Logger Host Software.

In Connections Tab, select DTLink Settings and press Enable Edit button, enter coq in Password.

Enter the DTLink Hub Address, Network ID and DTLink Logger Address in the dialog boxes. Press on Update Logger button to update devices.

It will show Update successful at the end of the process.

Click on Advanced Settings and Module Lock button.

Press the Get Code button to get a code to unlock the Xbee Module. Without module encryption, data download is blocked.

Copy code from adjacent window and send it to us. Keep the dialog open and a RST personnel will generate and email unlock key to you.

Enter the Code you receive from RST in the Box below the Code generated and Press Write Key button.

The DT Logger will save the Key in its memory and now the DT Logger will be able to communicate with the DT Link Hub.

If for some reason, there is an error shown up as below, just click OK to get back to the main menu.

Double-click top text in Connections tab, Options-&gt;Advanced:

Use “Flash” for password, click Yes to clear all memory data.

Then, the DT Logger will reboot and the DT Link is now enable on the DT Logger.

Connect the DT Link Hub to the PC and Press on Query DTLink button to check if the communication has been established successfully.

Press on Discover to automatically detect the DTLink Logger and it will show up on Wireless Logger List.

To manually enter the logger, press on Modify List button

Then Add new, enter the DTLink Logger details as shown below.

Press OK and the DTLink Wireless Hub will be connected to the DTLink Logger.

To read the DTLink Logger, select the DTLink Logger from the list of loggers and press Connect.

The status tab will show the details of the DTLink Logger being connected.

Press Collect Data button to get data from the DT Logger memory, then either Append or Overwrite data to existing data records in the PC data files.

Press on View Recent file to view recently downloaded data in Data Viewer.

Synopsys: When customer have a normal DT Logger and would like to upgrade it to have DT Link feature.

Connect DT Loggers to DTLink Wireless Hub using DT Loggers Host Software

[Image: A picture containing text, electronics

Description automatically generated]

[Image: A picture containing text

Description automatically generated]

[Image: Graphical user interface, text

Description automatically generated]

[Image: Graphical user interface, application

Description automatically generated]

[Image: Graphical user interface, text, application

Description automatically generated]

[Image: Graphical user interface, text, application

Description automatically generated]

[Image: Graphical user interface, application

Description automatically generated]
