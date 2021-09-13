---
title: "Tripping Breakers"
subtitle: "CSAW 2021 CTF"
author: USERNAME
date: "2021-09-10"
subject: "Tripping Breakers Writeup"
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

# Tripping Breakers

Writeup by: [USERNAME](https://github.com/USERNAME)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/tripping-breakers/)

----

```text
Attached is a forensics capture of an HMI (human machine interface) containing scheduled tasks, registry hives, and user profile of an operator account. There is a scheduled task that executed in April 2021 that tripped various breakers by sending DNP3 messages. We would like your help clarifying some information. What was the IP address of the substation_c, and how many total breakers were tripped by this scheduled task? Flag format: flag{IP-Address:# of breakers}. For example if substation_c's IP address was 192.168.1.2 and there were 45 total breakers tripped, the flag would be flag{192.168.1.2:45}.

Author: CISA
```

## Initial Research

Word.

```bash
$ echo 'thingz'
thingz
```

## Version Mismatches

Wordsz.

```text
some output
```

## Ancient History or Stegosarus Time

Moar Words

```shell
$ cat commands.txt
commands1
$ nmap 1.2.3.4
...
```

## Victory

Submit the flag and claim the points:

**flag{flag-goes-here}**
