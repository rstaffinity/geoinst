---
title: How to connect a DT2055B Data Logger to VW Multi-Point Borehole Extensometers (MPBX)
category: EXTENSOMETERS
modified: Tue, 6 Feb, 2024 at  9:11 AM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000281543-how-to-connect-a-dt2055b-data-logger-to-vw-multi-point-borehole-extensometers-mpbx-
article_id: 63000281543
---

# How to connect a DT2055B Data Logger to VW Multi-Point Borehole Extensometers (MPBX)

This document is intended to be a supplement to the DT Logger Host software manual as it assumes users have a basic understanding of setting up DT series data loggers with DT Logger Host software. The manual is available for download from the RST Instruments website at https://rstinstruments.com/product/dt-logger-host-software/

The DT2055B Data Logger has 5 ports on the circuit board so a maximum of 5 VW PMBX connections can be made. Each port can be used to connect the two sensors, one in the 1A/1B terminal connections, and one in the 2A/2B terminal connections.

Fig.1. DT2055B data logger after installation and testing

Normally, one element of the VW MPBX Extensometer will have 4 wires, 2 wires for the VW Sensor and 2 wires for the Thermistor (with an additional wire for cable shield screen).

Fig.2. MPBX extensometers with 3 elements

Once the VW Sensors and thermistors are connected in order on the circuit board, the sensors can be setup on the Sensor tab in DT Logger Host. The wires are placed in an order that help to manage the PMBX. When all the sensors have been added, five sensors will be displayed at a time.

Once all the sensors are connected in order on the circuit board, the sensors can be setup on the Sensor tab in DT Logger Host.

Fig. 3. DT2055B Logger Sensors Page

Change the names of the tabs to reference the preferred nomenclature for the VW Sensor and thermistor. The subsequent sensors can be added by clicking ‘New Copy’ and then change the tab name. Make sure to click ‘Upload to Logger’ to save the settings to the data logger memory.

For stand alone DT2050B Logger (without RSTAR enabled), the logging interval could be set in the Logging Tab.

Fig. 4. DT2055B Logger Logging Tab

To watch real-time readings, click on the Monitor tab. Up to 5 sensors can be displayed at a time. The title on the tab for each sensor will be displayed and the units box can be unchecked to show the raw resistance readings.

Fig.5. DT2055B Logger Monitor Page

Choosing the Status tab will allow the operator to see the status of the data logger and to download the data.

Fig. 6. DT2055B Data Logger Status Page

The Connections tab is used to setup the data logger for the type of connection (DTLink Wireless, RSTAR Wireless or USB).

Fig. 7. DT2055B Data Logger Connections Page

If you need support on VW MPBX extensometer installation, please contact RST Support at [email&#160;protected] or phone 1-604-540-1100.
