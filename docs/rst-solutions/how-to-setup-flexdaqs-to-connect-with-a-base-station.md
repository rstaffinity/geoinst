---
title: How to setup FlexDAQs to connect with a base station
category: FLEXDAQ DATA LOGGERS
modified: Thu, 8 Jul, 2021 at  3:43 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000264647-how-to-setup-flexdaqs-to-connect-with-a-base-station
article_id: 63000264647
---

# How to setup FlexDAQs to connect with a base station

Scenario: customer needs to connect a FlexDAQ via radio communication to a Base station, which is a system comprising of a NL200 Network Link Interface, a RF407 Radio Module, a Power Module, Battery, etc. with an Ethernet gateway to connect to the LAN in office.

Solution: follow the steps in the guide below to do this job.

First, connect the PC running LoggerNet Software to CR6 Logger by a micro–USB Cable.

You can verify that your settings are correct by selecting the datalogger in the Network Map, selecting the Clock tab, and pressing Check Clocks. If your settings are correct, you should see the current clock of your server and datalogger.

Note: Both the computer, in which the LoggerNet is running and the Base Station must be on the same network, i.e., in the same subnet of IP address, for them to be able to connect and communicate.

In the LoggerNet Setup screen, press Add Root and Choose IPPort. Input the NL200 IP address and port number as shown below.

Add a PakBus Port.

Add a PakBus Router (pbRouter). Input the PakBus address of the NL200. Its default address is 678.

Add the datalogger and input the PakBus address of the datalogger. Pakbus Encryption Key is printed on the sticker inside the FlexDAQ Box.

Click Apply to save the changes.

Scenario:

Solution:

Pakbus Encryption Key is printed on the sticker inside the FlexDAQ Box.

Apply

Check Clocks

Note:
