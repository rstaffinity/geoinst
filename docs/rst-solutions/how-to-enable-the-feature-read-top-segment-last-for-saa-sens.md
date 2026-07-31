---
title: How to enable the feature “Read Top Segment last” for SAA Sensor
category: SHAPEARRAY SAAV
modified: Mon, 10 Apr, 2023 at  4:13 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000268349-how-to-enable-the-feature-read-top-segment-last-for-saa-sensor
article_id: 63000268349
---

# How to enable the feature “Read Top Segment last” for SAA Sensor

Scenario:

The SAA Sensor Top Segment data is not correctly recorded when collected manually via DT Logger Host Software.

It has been noticed that recorded data collected directly from the RTSAAs indicate SAATop voltage greater than 1700 V, current above 55000 mA, and temperatures greater than 130 ⁰C which is not reflective of the conditions.

Solution:

Enable the feature “Read Top Segment last” for SAA Sensor following the steps below.

First, check the DT Logger Host Version to see the version.

You need version 4.14 or higher of the DT Logger Host for the following settings to work.

The latest Firmware is 4.16, and you can update the firmware using the RST firmware updater here: https://rstinstruments.com/wp-content/uploads/Mobile-Firmware-Update-1.23-1.zip

Go to Connections tab, click Options, then Advanced, click on Adjustments button. Please refer to screenshot below for proper settings.

Make sure to click OK button and wait for update process to finish. Please check “Read Top Segment Last” and set Delay Before Scan to 0.5 seconds.

Scenario:

The SAA Sensor Top Segment data is not correctly recorded when collected manually via DT Logger Host Software.

It has been noticed that recorded data collected directly from the RTSAAs indicate SAATop voltage greater than 1700 V, current above 55000 mA, and temperatures greater than 130 ⁰C which is not reflective of the conditions.

Solution:

Enable the feature “Read Top Segment last” for SAA Sensor following the steps below.

The latest Firmware is 4.16, and you can update the firmware using the RST firmware updater here: https://rstinstruments.com/wp-content/uploads/Mobile-Firmware-Update-1.23-1.zip

[Image: image]
