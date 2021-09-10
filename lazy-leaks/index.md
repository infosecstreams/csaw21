---
title: "Lazy Leaks"
subtitle: "CSAW 2021 CTF"
author: SinDaRemedy
date: "2021-09-10"
subject: "Lazy-Leaks Write-Up"
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

# Lazy Leaks

Writeup by: [SinDaRemedy](https://github.com/sindaremedy)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/lazy-leaks/)

----

```text
Someone at a company was supposedly using an unsecured communication channel. A dump of company communications was created to find any sensitive info leaks. See if you can find anything suspicious or concerning.
```

## You Get a String! And You Get a String!

Downloading the [`Lazy_Leaks.pcapng`](./Lazy_Leaks.pcapng) file searched the file for strings then grepped for flag in the string.

```bash
$ strings Lazy_Leaks.pcapng | grep flag
1)flag{T00_L@ZY_4_$3CUR1TY}
```

## Victory

Submit the flag and claim the points:

**flag{T00_L@ZY_4_$3CUR1TY}**
