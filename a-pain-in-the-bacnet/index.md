---
title: "A Pain in the BAC(net)"
subtitle: "CSAW 2021 CTF"
author: SinDaRemedy
date: "2021-09-10"
subject: "A Pain in the BAC(net) Writeup"
keywords: \[CSAW21, CSAW, CTF, InfoSec\]
lang: "en"
titlepage: true
titlepage-text-color: "FFFFFF"
titlepage-color: "0c0d0e"
titlepage-rule-color: "8ac53e"
titlepage-rule-height: 0
logo: "./logo.png"
logo-width: 3in
toc: true
toc-own-page: true
---

# A Pain in the BAC(net)

Writeup by: [SinDaRemedy](https://github.com/SinDaRemedy)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/a-pain-in-the-bacnet/)

----

```text
Attached is a packet capture taken from a building management network. One of the analog sensors reported values way outside of its normal operating range. Can you determine the object name of this analog sensor? Flag Format: flag{Name-of-sensor}. For example if the object name of this analog sensor was "Sensor_Temp1", the flag would be flag{Sensor_Temp1}. (Note: because there are a limited number of sensors, we're only giving you two guesses for this challenge, so please check your input carefully.)

Author: CISA
```

## Initial Research

Looking at the name of the challenge you immediately notice that the author is referring to Building Automation Control Networks(BACnet).  Additionally, when you look at the attachment you see that is a pcap that could be analyzed with WireShark.

After reading the question see that there are two main items you need to search/filter for.

- The object-name of the analog sensor.
- Abnormal reported values

Upon opening the pcap in Wireshark you see there are 3017 packets.

![](./Bacnet_wireshark1.png)

Then I began to look through the packets that had the object name "analog-input, (0)".  I noticed looking through the ADPU section of the capture that the packets could be filtered by obect identifier  "analog-input".

Once filtering by the analog-input identifier I started to notice that there was also a present-value identifier. In the ADPU you can see that it is a property identifier you can filter by. Filtering by both now displays 320 packets to sort through.

![](./bacnet_wireshark2.png)

I sorted the packets by info so the analog inputs would be in order and opened up the ADPU and present and started to scan for abnormalities in values. Most of the values were between 1 and 4 digits except for the present value in 4 of the packets in analog input 7.

Now that I spotted the abnormality in the value I started to search for the name of the sensors by object name. After sorting by the info column again you go to the analog-input 7 and can look at the ADPU drop-down to see the object name.

![](./bacnet_wireshark3.png)

## Victory

The flag was in the format of "flag{Sensor_#}", so from here you just submit the flag and claim the points.

**flag{Sensor_12345}**
