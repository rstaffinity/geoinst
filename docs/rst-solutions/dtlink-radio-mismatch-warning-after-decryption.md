---
title: DTLink - Radio mismatch warning after decryption
category: DT LINK WIRELESS DATA COLLECTION
modified: Mon, 27 Jun, 2022 at  1:07 PM
source_url: https://support.rstinstruments.com/support/solutions/articles/63000272890-dtlink-radio-mismatch-warning-after-decryption
article_id: 63000272890
---

# DTLink - Radio mismatch warning after decryption

DTLink Hubs have high bandwidth (200k) modules installed.

Assuming that DTLink module (200k) is installed properly in the logger socket of the data logger, (matching outline, not shifted). In the data logger wireless settings, 200k high bandwidth module will need to be selected. Rather than the RSTAR low bandwidth module which is about 9kbps.

Steps are below:

The XBEE Radio should be a HJP900 200k USA/Canada radio.

The DTLink hub address and Network ID should match the DTLink Hub.

This might not work because the data logger is actively logging or their may be other issues.

The best way to check it is to connect to the logger using hyperterminal (or another Terminal program such as YAT - free download on the internet), (921600 baud, 8N1) and send the following commands:

XINIT -1

You should get the following response from “XINIT -1” if the module is configured

Otherwise you will get

If response is a) send the command:

XINIT 2400 201 115200

If response is b) send the command:

XINIT 2400 201 9600

You should get the response

,+++,OK,OK

AT AP 1,0,OK

AT BD 7,0,OK

AT WR,0,OK

AT CN,0,OK

Send the following commands

AT 2 1 //Initialized module settings

AT WR //Write ID to permanent memory.

AT ID #### //Replace #### with correct network ID matching hub network id

AT WR //Write new ID to permanent memory

XBEE 9 //Reset to XBEE module and reload memory parameters

XINIT -1,+++,,+++,OK,115200,AT AP,1

XINIT -1,+++,9600,,….

[Image: Graphical user interface, application

Description automatically generated]

[Image: Graphical user interface, text

Description automatically generated]
