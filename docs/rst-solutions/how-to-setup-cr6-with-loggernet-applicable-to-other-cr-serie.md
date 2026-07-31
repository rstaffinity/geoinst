---
title: How to setup CR6 with LoggerNet (applicable to other CR series loggers)
category: FLEXDAQ DATA LOGGERS
modified: Thu, 21 Mar, 2024 at 11:14 AM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000264628-how-to-setup-cr6-with-loggernet-applicable-to-other-cr-series-loggers-
article_id: 63000264628
---

# How to setup CR6 with LoggerNet (applicable to other CR series loggers)

Scenario: Customer needs to setup a Campbell Scientific CR6 Logger in a LoggerNet to control the FlexDAQ Unit.

Solution: Follow the steps in the guide below to do the job.

A FlexDAQ incorporates a Campbell Scientific Data Logger (CR6, CR300, etc.), and a combination of external devices such as, telemetry, power, DTLoggers and sensors.

All FlexDAQ’s are built to customer’s specifications; therefore, not all devices in this manual will apply. Refer to sales order and/or checklist for complete specification of the FlexDAQ.

LoggerNET is support software package that controls the Campbell Scientific Data Logger which supports programming, communication and data retrieval between a logger and PC.

Note: LoggerNet may come with FlexDAQ – Check Sales Order

After Installation – Click Help → Check For Updates

Follow instructions.

Ensure Device Configuration Utility is up to date:

Go to the below link and update to latest Device Configuration Utility

https://www.campbellsci.com/devconfig

Alternative method:

Update CRBasic Editor Compiler

Install latest CR6 OS version v.10.02 (or newer)

Required Equipment:

Open LoggerNet application, Click and run the Device Config Utility application

Another Way to Set Up CR6:

Navigate to Set Up and click on Standard View button.

Click on Add Root and Select ComPort, under Select a device to add to… Select PakBusPort (PakBus Logger)… Select CR6Series and Close. Select the right ComPort Connection from the dropdown menu.

Choose a station to connect to in the left menu; Once selected, click the Connect button, , in the upper left. Depending on the type of logger the series name may vary.

The LoggerNet Connect application. The different stations are found in the left menu.

Once connected, data can be collected, station time set, send new programs, etc.

Make sure to set the station date and time is correct, if not already set. This will sync the time to the computer that it is connected.

Once finished, disconnect from the station.

Note: The datalogger must be setup before setting up scheduled data collection.

In the Schedule tab, perform the following steps:

For example, the following setup will collect (download) the data from the datalogger every 12 hours at midnight and noon, retrying 3 times every 10 minutes if the initial data collection fails:

It is recommended to check whether the data is getting collected as desired after a couple of intervals have passed.

The default Scan Interval for the RSTAR network is 6 hour (default interval varies from order to order from one of the 5 intervals, see below).

Changing the RSTAR reading interval

An example of the Ports and Flags pop-up interface.

An example of what the Ports and Flags pop-up interface will look like after adding the interval variables.

To change the interval, deselect the currently highlighted interval by clicking the lit green indicator. Once off, click the green indicator for the desired interval. During the next scan interval (1min), all of the loggers in the RSTAR network will be set to the new interval.

ANOTHER WAY TO CHANGE THE INTERVAL:

Click on the desired interval, e.g. rstarMin_10 for every 10 minutes, type in true and it will collect every 10 minutes.

Open LoggerNet

Navigate to Device Configuration Utility

Open Device Configuration Utility

Click Help → Check For Updates

Go to https://www.campbellsci.com/cr6

Click Downloads

Micro-USB (CR6)

Laptop / Desktop

Ethernet cable (OPTIONAL)

Select CR6 by selecting the correct Datalogger type under the Datalogger dropdown menu to the left or type CR6 in Search bar

If a PakBus Encryption Key is included (CRXXXX_Passwords.pdf), enter the PakBus Encryption Key, provided in the USB Flash drive.

Follow the instructions in the setup window to install any drivers necessary, if required.

Launch LoggerNet and open the Setup Application, .

In the Entire Network window on the right, select the desired datalogger:

Check the Scheduled Collection Enabled box

In the Base section, the Date may be left alone or change it to when start of collection started you can leave the Date at a default 01-Jan-90. Set the Time to the base (start) time. The base time is the reference time for the collection interval.

Set the Collection Interval to the desired collection interval (frequency).

Set the Primary Retry Interval to the desired interval at which the collection will be retried in case the first attempt fails.

Set the Number of Primary Retries to the desired value.

It’s recommended that the Secondary Retry Interval Enabled box is checked off.

Click Apply in the Entire Network panel.

From LoggerNet’s launcher window, open the Connect, , application found under the Main menu section.

Connect to the station of interest.

Once connected click the Ports &amp; Flags button in the ribbon menu.

Select an empty cell and click the Add button. (see Figure 10 for interface) The interface may vary slightly depending on type of logger program.

Select Public in the Tables column, and then add rstarMin_10 through to rstarHR_12 from within the Fields column by clicking Paste. (Figure 11: Selecting RSTAR Intervals &amp; Figure 12 display interface after adding intervals) The interface may vary slightly depending on the type of logger program.

Selecting RSTAR Intervals

LoggerNet Station Setup

RSTAR Reading Interval

Install LoggerNet – Check if update is available

Setup the CR6

Connect CR6 to LoggerNet:

Setting up Scheduled Data Collection in LoggerNet

From LoggerNet main menu, launch Connect, , application

Scenario:

Solution:

Required Equipment:

LoggerNet Station Setup

Another Way to Set Up CR6:

Select a device to add to…

Make sure to set the station date and time is correct, if not already set. This will sync the time to the computer that it is connected.

Setting up Scheduled Data Collection in LoggerNet

ANOTHER WAY TO CHANGE THE INTERVAL:
