---
title: DT Loggers (DT2011B, DT2055B, DT2040, etc.) setting consideration on application with Vibrating Wire Crack Meters.
category: DATA LOGGERS
modified: Fri, 24 Jun, 2022 at  3:19 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000272856--dt-loggers-dt2011b-dt2055b-dt2040-etc-setting-consideration-on-application-with-vibrating-wire
article_id: 63000272856
---

# DT Loggers (DT2011B, DT2055B, DT2040, etc.) setting consideration on application with Vibrating Wire Crack Meters.

When setting up the DT Loggers (DT2011B, DT2055B, DT2040, etc.) to read and display the Engineering Unit of Crack Meter value, e.g., in mm, there is an important detail to take into consideration, the absolute value of the Linear Calibration Factor. It must be entered with a negative (-) value instead of the positive value (+) as with other application.

Below is the detailed explanation.

Vibrating Wire Crack Meter Calibration Record

Default formula in DT2055B data loggers:

Difference between the formula in VW Crack Meter Calibration Record and Default formula in DT2055B data loggers.

To correct this difference and get positive number we need to multiply by -1 the CF on DT Loggers (DT2011B, DT2055B, DT2040, etc.) then the formula will be the same as the Vibrating wire Crack Meter Calibration Record.

Vibrating Wire Crack Meter Calibration Record

Default formula in DT2055B data loggers:
