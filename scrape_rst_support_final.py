#!/usr/bin/env python3
"""
Batch scrape RST Instruments support articles - FIXED VERSION
- Proper title extraction from <h2> (handles HTML entities)
- Clean slug generation 
- Generates nav entries for mkdocs.yml
"""
import os, sys, json, re, time
from pathlib import Path
import urllib.request

SRC_DIR = Path(r"C:\Users\Henry\Documents\Github Repos\geoinst\docs\rst-solutions")
SRC_DIR.mkdir(parents=True, exist_ok=True)

ARTICLES = [
    {"id": "63000289174", "title": "Adding Devices in GeoExplorerIQ Using the Affinity Mobile App (Recommended)", "url": "https://support.rstinstruments.com/support/solutions/articles/63000289174-adding-devices-in-geoexploreriq-using-the-affinity-mobile-app-recommended-", "category": "GEOExplorerIQ Device Mgmt"},
    {"id": "63000288958", "title": "Device configuration and set up", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288958-device-configuration-and-set-up", "category": "GEOExplorerIQ Device Mgmt"},
    {"id": "63000288640", "title": "Adding a Gateway Directly in GeoExplorerIQ", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288640-adding-a-gateway-directly-in-geoexploreriq", "category": "GEOExplorerIQ Device Mgmt"},
    {"id": "63000288601", "title": "How to accept invitation and access GeoExplorerIQ", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288601-how-to-accept-invitation-and-access-geoexploreriq", "category": "GEOExplorerIQ Device Mgmt"},
    {"id": "63000288964", "title": "How to Add Users to the Platform", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288964-how-to-add-users-to-the-platform", "category": "GEOExplorerIQ User Management"},
    {"id": "63000288965", "title": "Adding a User to Site Groups", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288965-adding-a-user-to-site-groups", "category": "GEOExplorerIQ User Management"},
    {"id": "63000288903", "title": "GeoExplorer Overview", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288903-geoexplorer-overview", "category": "GEOExplorerIQ Visualization"},
    {"id": "63000288904", "title": "Sub Surface Analysis", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288904-sub-surface-analysis", "category": "GEOExplorerIQ Visualization"},
    {"id": "63000288911", "title": "Sub-Surface Analysis Workflow", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288911-sub-surface-analysis-workflow", "category": "GEOExplorerIQ Visualization"},
    {"id": "63000288962", "title": "Charts - Plotting Time Series", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288962-charts-plotting-time-series", "category": "GEOExplorerIQ Visualization"},
    {"id": "63000288873", "title": "GEOExplorerIQ Release Notes - May 2026", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288873-geoexploreriq-release-notes-may-2026", "category": "GEOExplorerIQ Release Notes"},
    {"id": "63000288969", "title": "GEOExplorerIQ Data Types", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288969-geoexploreriq-data-types", "category": "Data Types / Calculations"},
    {"id": "63000288968", "title": "Displacement & Velocity Calculations", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288968-displacement-velocity-calculations", "category": "Data Types / Calculations"},
    {"id": "63000288966", "title": "Trend Line Description & Calculations", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288966-trend-line-description-calculations", "category": "Data Types / Calculations"},
    {"id": "63000288967", "title": "Create Triggers", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288967-create-triggers", "category": "GEOExplorerIQ Alarms & Events Management"},
    {"id": "63000288970", "title": "How to Review Events", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288970-how-to-review-events", "category": "GEOExplorerIQ Alarms & Events Management"},
    {"id": "63000288972", "title": "Creating a Static Report", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288972-creating-a-static-report", "category": "GEOExplorerIQ Reporting"},
    {"id": "63000283903", "title": "How to connect a ShapeArray SAA Sensor to NavSTAR/ GeoExplorer", "url": "https://support.rstinstruments.com/support/solutions/articles/63000283903-how-to-connect-a-shapearray-saa-sensor-to-navstar-geoexplorer", "category": "NavStar"},
    {"id": "63000267644", "title": "How to pair an older inclinometer reel with a newer Field PC", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267644-how-to-pair-an-older-inclinometer-reel-with-a-newer-field-pc", "category": "MEMS DIGITAL IN-PLACE INCLINOMETER SYSTEM"},
    {"id": "63000267826", "title": "How to convert Borehole File to output .rpp files in the RST Field PC.", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267826-how-to-convert-borehole-file-to-output-rpp-files-in-the-rst-field-pc-", "category": "MEMS DIGITAL IN-PLACE INCLINOMETER SYSTEM"},
    {"id": "63000272895", "title": "Neat Grout vs. Bentonite Grout", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272895-neat-grout-vs-bentonite-grout", "category": "Other Frequently Asked Questions"},
    {"id": "63000249523", "title": "VW2106 - Programming Piezometer Locations using RST Readout Host", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249523-vw2106-programming-piezometer-locations-using-rst-readout-host", "category": "VW2106: READOUTS"},
    {"id": "63000249538", "title": "VW2106 - Discharging the low power capacitor when a VW2106 will not turn on", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249538-vw2106-discharging-the-low-power-capacitor-when-a-vw2106-will-not-turn-on", "category": "VW2106: READOUTS"},
    {"id": "63000249540", "title": "VW2106 - Choosing the proper connection port", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249540-vw2106-choosing-the-proper-connection-port", "category": "VW2106: READOUTS"},
    {"id": "63000272088", "title": "Espanol - Decarga del condensador de baja potencia", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272088-espanol-decarga-del-condensador-de-baja-potencia", "category": "VW2106: READOUTS"},
    {"id": "63000267721", "title": "How to use VW2106 Read Out to set up VW Load Cells", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267721-how-to-use-vw2106-read-out-to-set-up-vw-load-cells", "category": "VW2106: READOUTS"},
    {"id": "63000268349", "title": "How to enable the feature Read Top Segment last for SAA Sensor", "url": "https://support.rstinstruments.com/support/solutions/articles/63000268349-how-to-enable-the-feature-read-top-segment-last-for-saa-sensor", "category": "SHAPEARRAY SAAV"},
    {"id": "63000277443", "title": "How to find SAAV resources?", "url": "https://support.rstinstruments.com/support/solutions/articles/63000277443-how-to-find-saav-resources-", "category": "SHAPEARRAY SAAV"},
    {"id": "63000252803", "title": "Programming a load cell calibration into a SG350 Readout", "url": "https://support.rstinstruments.com/support/solutions/articles/63000252803-programming-a-load-cell-calibration-into-a-sg350-readout", "category": "SG350: BRIDGE TRANSDUCER READOUT"},
    {"id": "63000267782", "title": "How to transfer Site Files Between RST Readouts", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267782-how-to-transfer-site-files-between-rst-readouts", "category": "SG350: BRIDGE TRANSDUCER READOUT"},
    {"id": "63000264627", "title": "How to Set up a wireless communication between a DT series Data Logger with a L900 RSTAR Node and FlexDAQ with L900 RSTAR RTU using DT Logger Host Software.", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264627-how-to-set-up-a-wireless-communication-between-a-dt-series-data-logger-with-a-l900-rstar-node-and-fle", "category": "FLEXDAQ DATA LOGGERS"},
    {"id": "63000264628", "title": "How to setup CR6 with LoggerNet (applicable to other CR series loggers)", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264628-how-to-setup-cr6-with-loggernet-applicable-to-other-cr-series-loggers-", "category": "FLEXDAQ DATA LOGGERS"},
    {"id": "63000272773", "title": "How to update table definitions to fix common issue with data collection", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272773-how-to-update-table-definitions-to-fix-common-issue-with-data-collection", "category": "FLEXDAQ DATA LOGGERS"},
    {"id": "63000272775", "title": "How to update firmware of RTU to fix data error issues", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272775-how-to-update-firmware-of-rtu-to-fix-data-error-issues", "category": "FLEXDAQ DATA LOGGERS"},
    {"id": "63000264647", "title": "How to setup FlexDAQs to connect with a base station", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264647-how-to-setup-flexdaqs-to-connect-with-a-base-station", "category": "FLEXDAQ DATA LOGGERS"},
    {"id": "63000281543", "title": "How to connect a DT2055B Data Logger to VW Multi-Point Borehole Extensometers (MPBX)", "url": "https://support.rstinstruments.com/support/solutions/articles/63000281543-how-to-connect-a-dt2055b-data-logger-to-vw-multi-point-borehole-extensometers-mpbx-", "category": "EXTENSOMETERS"},
    {"id": "63000249541", "title": "VW Piezometer kPa/MPa Calculation Spreadsheet", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249541-vw-piezometer-kpa-mpa-calculation-spreadsheet", "category": "PIEZOMETERS"},
    {"id": "63000261684", "title": "Pneumatic Piezometer - Working principle", "url": "https://support.rstinstruments.com/support/solutions/articles/63000261684-pneumatic-piezometer-working-principle", "category": "PIEZOMETERS"},
    {"id": "63000261686", "title": "Saturation Procedure for VW2100MM - Micro-Miniature VW Piezometers", "url": "https://support.rstinstruments.com/support/solutions/articles/63000261686-saturation-procedure-for-vw2100mm-micro-miniature-vw-piezometers", "category": "PIEZOMETERS"},
    {"id": "63000264702", "title": "How to connect a RST Multi-point Piezometer String VMP to RST DT Logger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264702-how-to-connect-a-rst-multi-point-piezometer-string-vmp-to-rst-dt-logger", "category": "PIEZOMETERS"},
    {"id": "63000267419", "title": "How do Pneumatic Piezometer works?", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267419-how-do-pneumatic-piezometer-works-", "category": "PIEZOMETERS"},
    {"id": "63000267580", "title": "How to Quick-Start Digital Portable Tiltmeter", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267580-how-to-quick-start-digital-portable-tiltmeter", "category": "IN-PLACE TILTMETER / SUBMERSIBLE TILTMETER (MEMS)"},
    {"id": "63000262585", "title": "How to purge air out of a D'Aerator", "url": "https://support.rstinstruments.com/support/solutions/articles/63000262585-how-to-purge-air-out-of-a-d-aerator", "category": "VIBRATING WIRE LIQUID SETTLEMENT SYSTEM"},
    {"id": "63000267216", "title": "How to test a tape and reset a reed switch of RST Magnetic Settlement System", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267216-how-to-test-a-tape-and-reset-a-reed-switch-of-rst-magnetic-settlement-system", "category": "VIBRATING WIRE LIQUID SETTLEMENT SYSTEM"},
    {"id": "63000267781", "title": "How to program the timer on a D'Aerator", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267781-how-to-program-the-timer-on-a-d-aerator", "category": "VIBRATING WIRE LIQUID SETTLEMENT SYSTEM"},
    {"id": "63000273145", "title": "How to Set up a Crack Meter and Joint Meters in DT2011B Data Logger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000273145-how-to-set-up-a-crack-meter-and-joint-meters-in-dt2011b-data-logger", "category": "CRACK METERS & JOINT METERS"},
    {"id": "63000264706", "title": "How to setup a DT2011B Data Logger with a VW Strain Gauge Sensor", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264706-how-to-setup-a-dt2011b-data-logger-with-a-vw-strain-gauge-sensor", "category": "STRAIN GAUGES & STRAIN METERS"},
    {"id": "63000264707", "title": "How to connect Thermistor String with DT2040 Data Logger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264707-how-to-connect-thermistor-string-with-dt2040-data-logger", "category": "THERMISTORS"},
    {"id": "63000267911", "title": "How to make ganged common connections for Thermistor String in DT2040 Data Logger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267911-how-to-make-ganged-common-connections-for-thermistor-string-in-dt2040-data-logger", "category": "THERMISTORS"},
    {"id": "63000267709", "title": "How to reset Instantel Micromate", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267709-how-to-reset-instantel-micromate", "category": "VIBRATION AND OVERPRESSURE INSTANTEL"},
    {"id": "63000280983", "title": "How to use YAT to read RTU information", "url": "https://support.rstinstruments.com/support/solutions/articles/63000280983-how-to-use-yat-to-read-rtu-information", "category": "RSTAR L900 WIRELESS DATA ACQUISITION"},
    {"id": "63000264668", "title": "How to connect DTLink Loggers to DT Link Wireless Hub", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264668-how-to-connect-dtlink-loggers-to-dt-link-wireless-hub", "category": "DT LINK WIRELESS DATA COLLECTION"},
    {"id": "63000267640", "title": "How to connect DT Loggers to DTLink Wireless Hub using DT Loggers Host Software", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267640-how-to-connect-dt-loggers-to-dtlink-wireless-hub-using-dt-loggers-host-software", "category": "DT LINK WIRELESS DATA COLLECTION"},
    {"id": "63000272010", "title": "How to Upgrade a DT Logger to a DT Link Enable Logger and setup wireless communication between DT Loggers and DT Link Hub", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272010-how-to-upgrade-a-dt-logger-to-a-dt-link-enable-logger-and-setup-wireless-communication-between-dt-log", "category": "DT LINK WIRELESS DATA COLLECTION"},
    {"id": "63000272890", "title": "DTLink - Radio mismatch warning after decryption", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272890-dtlink-radio-mismatch-warning-after-decryption", "category": "DT LINK WIRELESS DATA COLLECTION"},
    {"id": "63000272892", "title": "Setting up Multiple DTLink Hubs for use with the same DTLink data loggers", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272892-setting-up-multiple-dtlink-hubs-for-use-with-the-same-dtlink-data-loggers", "category": "DT LINK WIRELESS DATA COLLECTION"},
    {"id": "63000275464", "title": "How to Login a Site from Affinity Field App and from Terra Insights Cloud", "url": "https://support.rstinstruments.com/support/solutions/articles/63000275464-how-to-login-a-site-from-affinity-field-app-and-from-terra-insights-cloud", "category": "RSTAR AFFINITY DATA LOGGER"},
    {"id": "63000275465", "title": "How to Claim an Affinity Data Logger to a site using Affinity Field App", "url": "https://support.rstinstruments.com/support/solutions/articles/63000275465-how-to-claim-an-affinity-data-logger-to-a-site-using-affinity-field-app", "category": "RSTAR AFFINITY DATA LOGGER"},
    {"id": "63000275466", "title": "How to add an instrument in an Affinity Data Logger using Affinity Field App", "url": "https://support.rstinstruments.com/support/solutions/articles/63000275466-how-to-add-an-instrument-in-an-affinity-data-logger-using-affinity-field-app", "category": "RSTAR AFFINITY DATA LOGGER"},
    {"id": "63000275467", "title": "How to download data from Affinity Data Logger to Affinity Field App and Sync data to Terra Insights Dashboard", "url": "https://support.rstinstruments.com/support/solutions/articles/63000275467-how-to-download-data-from-affinity-data-logger-to-affinity-field-app-and-sync-data-to-terra-insights-", "category": "RSTAR AFFINITY DATA LOGGER"},
    {"id": "63000280423", "title": "Installation Guide of RSTAR Affinity Logger - Instrument Wiring", "url": "https://support.rstinstruments.com/support/solutions/articles/63000280423-installation-guide-of-rstar-affinity-logger-instrument-wiring", "category": "RSTAR AFFINITY DATA LOGGER"},
    {"id": "63000249557", "title": "DT2011B VWP Default kPa Calculation Spreadsheet", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249557-dt2011b-vwp-default-kpa-calculation-spreadsheet", "category": "DATA LOGGERS"},
    {"id": "63000249558", "title": "DT2011B VWP Default MPa Calculation Spreadsheet", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249558-dt2011b-vwp-default-mpa-calculation-spreadsheet", "category": "DATA LOGGERS"},
    {"id": "63000264669", "title": "How to fix Port Closed error when a DT Logger is connected to DT Logger Host", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264669-how-to-fix-port-closed-error-when-a-dt-logger-is-connected-to-dt-logger-host", "category": "DATA LOGGERS"},
    {"id": "63000272856", "title": "DT Loggers (DT2011B, DT2055B, DT2040, etc.) setting consideration on application with Vibrating Wire Crack Meters.", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272856--dt-loggers-dt2011b-dt2055b-dt2040-etc-setting-consideration-on-application-with-vibrating-wire", "category": "DATA LOGGERS"},
    {"id": "63000264705", "title": "How to setup a DT2011B Data Logger with a VW piezometer", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264705-how-to-setup-a-dt2011b-data-logger-with-a-vw-piezometer", "category": "DATA LOGGERS"},
    {"id": "63000288631", "title": "Here is the user guide to use Affinity Field Utility App", "url": "https://support.rstinstruments.com/support/solutions/articles/63000288631-here-is-the-user-guide-to-use-affinity-field-utility-app", "category": "RSTAR AFFINITY DIGITAL SUITE"},
    {"id": "63000267469", "title": "How to adjust boreholes after Adding or Removing inclinometer casing", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267469-how-to-adjust-boreholes-after-adding-or-removing-inclinometer-casing", "category": "INCLINALYSIS DIGITAL INCLINOMETER SOFTWARE"},
    {"id": "63000268986", "title": "How to convert CSV data files to RPP data files for use with DigiPro software", "url": "https://support.rstinstruments.com/support/solutions/articles/63000268986-how-to-convert-csv-data-files-to-rpp-data-files-for-use-with-digipro-software", "category": "INCLINALYSIS DIGITAL INCLINOMETER SOFTWARE"},
    {"id": "63000272894", "title": "How to transfer CP3 Digital Inclinometer Data vis USB to a computer", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272894-how-to-transfer-cp3-digital-inclinometer-data-vis-usb-to-a-computer", "category": "INCLINALYSIS DIGITAL INCLINOMETER SOFTWARE"},
    {"id": "63000273144", "title": "Inclinalysis - Changing Values on the X Axis", "url": "https://support.rstinstruments.com/support/solutions/articles/63000273144-inclinalysis-changing-values-on-the-x-axis", "category": "INCLINALYSIS DIGITAL INCLINOMETER SOFTWARE"},
    {"id": "63000268985", "title": "Android Digital Inclinometer App Hot Sheet", "url": "https://support.rstinstruments.com/support/solutions/articles/63000268985-android-digital-inclinometer-app-hot-sheet", "category": "DIGITAL INCLINOMETER APP"},
    {"id": "63000264675", "title": "How to copy files from RST FieldPC2 to PC via USB Cable, a memory stick or Bluetooth", "url": "https://support.rstinstruments.com/support/solutions/articles/63000264675-how-to-copy-files-from-rst-fieldpc2-to-pc-via-usb-cable-a-memory-stick-or-bluetooth", "category": "DIGITAL INCLINOMETER SOFTWARE FOR FIELD PC READOUTS"},
    {"id": "63000267827", "title": "How to convert Data File in a RST Field PC from .csv to .rpp for use in DigiPro software.", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267827-how-to-convert-data-file-in-a-rst-field-pc-from-csv-to-rpp-for-use-in-digipro-software-", "category": "DIGITAL INCLINOMETER SOFTWARE FOR FIELD PC READOUTS"},
    {"id": "63000268987", "title": "How to modify RST Field PC CSV borehole base files to output RPP format files for use with DigiPro software", "url": "https://support.rstinstruments.com/support/solutions/articles/63000268987-how-to-modify-rst-field-pc-csv-borehole-base-files-to-output-rpp-format-files-for-use-with-digipro-so", "category": "DIGITAL INCLINOMETER SOFTWARE FOR FIELD PC READOUTS"},
    {"id": "63000144059", "title": "Setting up a Piezometer in DT Logger Host for a DT2011B Data Logger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000144059-setting-up-a-piezometer-in-dt-logger-host-for-a-dt2011b-data-logger", "category": "DATA LOGGERS"},
    {"id": "63000249508", "title": "DT Logger Host - Communication Troubleshooting (Status 0, 2 and 3 Warnings)", "url": "https://support.rstinstruments.com/support/solutions/articles/63000249508-dt-logger-host-communication-troubleshooting-status-0-2-and-3-warnings-", "category": "DATA LOGGERS"},
    {"id": "63000267722", "title": "How to resolve Memory Pointers Range Error", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267722-how-to-resolve-memory-pointers-range-error", "category": "DATA LOGGERS"},
    {"id": "63000267778", "title": "How to update firmware for RST DT Data Logger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267778-how-to-update-firmware-for-rst-dt-data-logger", "category": "DATA LOGGERS"},
    {"id": "63000272922", "title": "DT Logger Host - Communications Troubleshooting (Status 0, 2 and 3 Warnings)", "url": "https://support.rstinstruments.com/support/solutions/articles/63000272922-dt-logger-host-communications-troubleshooting-status-0-2-and-3-warnings-", "category": "DATA LOGGERS"},
    {"id": "63000280894", "title": "Digital Tilmeter Connection Issue", "url": "https://support.rstinstruments.com/support/solutions/articles/63000280894-digital-tilmeter-connection-issue", "category": "IN-PLACE TILTMETER / SUBMERSIBLE TILTMETER (MEMS)"},
    {"id": "63000267498", "title": "How to change batteries in a new style RST Inclinometer Reel", "url": "https://support.rstinstruments.com/support/solutions/articles/63000267498-how-to-change-batteries-in-a-new-style-rst-inclinometer-reel", "category": "MEMS DIGITAL IN-PLACE INCLINOMETER SYSTEM"},
    {"id": "63000273146", "title": "How to setup a TDR Sensor and TDR200 Datalogger", "url": "https://support.rstinstruments.com/support/solutions/articles/63000273146-how-to-setup-a-tdr-sensor-and-tdr200-datalogger", "category": "DATA LOGGERS"},
    {"id": "63000273225", "title": "Documento de configuracion de TDR", "url": "https://support.rstinstruments.com/support/solutions/articles/63000273225-documento-de-configuracion-de-tdr", "category": "DATA LOGGERS"},
    {"id": "63000273248", "title": "TDR200 Setup Document", "url": "https://support.rstinstruments.com/support/solutions/articles/63000273248-tdr200-setup-document", "category": "DATA LOGGERS"},
    {"id": "63000283904", "title": "TDR200 Setting up a TDR using PC-TDR software", "url": "https://support.rstinstruments.com/support/solutions/articles/63000283904-tdr200-setting-up-a-tdr-using-pc-tdr-software", "category": "DATA LOGGERS"},
]


def make_slug(title):
    """Create a clean slug from title only."""
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return slug[:60].rstrip('-')


def fetch_article(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode('utf-8', errors='replace')
    except Exception as e:
        return None, str(e)

    # Extract title from h2 (including &nbsp; etc)
    h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
    if h2_match:
        title = re.sub(r'<[^>]+>', '', h2_match.group(1))
        title = re.sub(r'&nbsp;', ' ', title)
        title = re.sub(r'\s+', ' ', title).strip()
    else:
        title = ''

    # Get modified date
    mod_match = re.search(r'Modified on:\s*([^<]+)', html)
    modified = mod_match.group(1).strip() if mod_match else ''

    # Extract article content
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if not article_match:
        return None, "No article tag found"

    article_html = article_match.group(0)
    text_parts = []

    # Extract all paragraph and list text
    for tag in ['p', 'li', 'h1', 'h2', 'h3', 'h4', 'strong']:
        for match in re.finditer(f'<{tag}[^>]*>(.*?)</{tag}>', article_html, re.DOTALL):
            text = re.sub(r'<[^>]+>', '', match.group(1))
            text = re.sub(r'&nbsp;', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if text and len(text) > 2:
                text_parts.append(text)

    # Extract image alt text
    img_matches = re.findall(r'<img[^>]+alt=["\']([^"\']*)["\'][^>]*>', article_html)
    for alt in img_matches:
        if alt and alt.strip():
            text_parts.append(f"[Image: {alt.strip()}]")

    content = '\n\n'.join(text_parts)
    return {
        'title': title,
        'modified': modified,
        'content': content,
    }, None


def make_slug(title):
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return slug[:60].rstrip('-')


def main():
    print(f"Scraping {len(ARTICLES)} articles...")
    results = []
    nav_entries = []
    for i, art in enumerate(ARTICLES):
        print(f"[{i+1}/{len(ARTICLES)}] {art['title'][:60]}...")
        result, err = fetch_article(art['url'])
        if err:
            print(f"  ERROR: {err}")
            continue
        if not result['title']:
            print(f"  WARNING: Empty title extracted, using original: {art['title']}")
            result['title'] = art['title']
        result['category'] = art['category']
        result['article_id'] = art['id']
        results.append(result)
        nav_entries.append({result['title']: f"rst-solutions/{make_slug(result['title'])}"})
        time.sleep(0.5)

    # Save index
    idx_path = SRC_DIR / "_index.json"
    idx_path.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"Saved index: {idx_path} ({len(results)} articles)")

    # Generate individual markdown files
    for r in results:
        slug = make_slug(r['title'])
        md = SRC_DIR / f"{slug}.md"
        md.write_text(
            f"---\ntitle: {r['title']}\ncategory: {r['category']}\nmodified: {r['modified']}\nsource_url: {ARTICLES[results.index(r)]['url']}\narticle_id: {r['article_id']}\n---\n\n# {r['title']}\n\n{r['content']}\n",
            encoding='utf-8'
        )

    # Write nav entries for mkdocs.yml
    nav_file = Path(r"C:\Users\Henry\Documents\Github Repos\geoinst\rst-solutions-nav.yml")
    nav_yaml = "  - RST Solutions:\n      - Official Support Articles: rst-solutions/index.md\n"
    for r in results:
        slug = make_slug(r['title'])
        nav_yaml += f"      - {r['title']}: rst-solutions/{slug}.md\n"
    nav_file.write_text(nav_yaml, encoding='utf-8')
    print(f"Generated {len(results)} markdown files + nav entries in {SRC_DIR}")

if __name__ == '__main__':
    main()