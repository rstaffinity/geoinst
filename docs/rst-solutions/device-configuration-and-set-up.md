---
title: Device configuration and set up
category: GEOExplorerIQ Device Mgmt
modified: Tue, 30 Jun, 2026 at  1:01 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000288958-device-configuration-and-set-up
article_id: 63000288958
---

# Device configuration and set up

Accessing Device Management

To begin, navigate to the left-hand side of the homepage. Here, you will find the navigation menu. Click on the “Device Management” option. This action will direct you to the Systems page, where you can view all the hardware currently deployed on your site. This centralized view allows for easier monitoring and management of your devices.

The Systems page provides a comprehensive overview of your hardware, including:

- Gateways and Data Loggers: These devices are essential for collecting and transmitting data from sensors to the GeoExplorerIQ platform. They ensure that data is accurately captured and readily available for analysis, which is vital for maintaining data integrity.

- NavStar Hardware: This category includes devices that utilize GPS technology for precise location tracking. Understanding the status of NavStar hardware is crucial for ensuring accurate data collection, as location accuracy directly impacts the quality of your data.

- Instrumentation: This encompasses various sensors, such as piezometers and ShapeArrays, which are critical for monitoring environmental conditions and structural health. Proper management of these instruments ensures that you receive timely and accurate readings.

Once your devices are visible in GeoExplorerIQ, you can take advantage of several management features:

Modify Configuration Settings

Within the General section, you can change the instrument name and serial number, as well as add tags and descriptions for better organization.

Configuration pertains to the technical arrangement necessary for data processing, including elevations and datums. The data source configuration will depend on the sensor type.

The Location shows where a sensor is placed on the map in the system. Keeping this accurate helps ensure your data is shown correctly and is easy to understand.

Users can update sensor locations through the following interfaces:

Supported Devices

Most sensors support manual location updates.

However, the following devices are exceptions:

Sensors may operate under different location modes:

1. Automatic: The sensor location is provided automatically by

2. Fixed

Note: Users are responsible for ensuring that sensor locations remain accurate.

Data Source:

Data sources are set automatically based on the device type and usually don’t require any setup.

Affinity Devices

Other Devices

Calculations:

Affinity Devices

You can still add additional or custom calculations if needed

Non‑Affinity Devices

Configure

Under Configure, there are 4 available sections:

Chart, In this section, you can adjust the default date range, typically defined in days, to control the time period displayed in the charts.

In the sensor list, you can select which variables to display, including raw measurements and processed data, depending on your analysis needs.

Marker Settings, this section allows you to modify how the instrument appears on the map, such as changing the marker or icon style for better visualization.

Velocity Settings, In this section, you define how the velocity of the instrument data is calculated.

For example, you can analyze how quickly pore pressure is increasing or decreasing over time.

There are two main approaches:

Mobile App

GeoExplorerIQ

GNSS receivers

Prisms

The location is provided by the device itself (logger or external system)

You don’t need to enter it manually

The sensor has a set position

In most cases, you can still update it if needed

Already configured by default

No action required

Data is automatically available in GeoExplorerIQ

Data is sent directly to the system

GeoExplorerIQ retrieves and displays it automatically

A basic calculation is automatically created when the device is set up

No manual configuration is required

Data is ready to use in GeoExplorerIQ

No calculations are created by default

Calculations must be configured manually if required

Chart

Sensor List

Marker Settings

Velocity Settings

Period-based velocity: compares values over a defined time window

Rolling calculation: provides a smoother trend by continuously analyzing data over time

Accessing Device Management

Modify Configuration Settings

Supported Devices

Chart,

In the sensor list

Marker Settings,

Velocity Settings,
