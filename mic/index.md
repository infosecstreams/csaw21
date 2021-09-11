---
title: "mic"
subtitle: "CSAW 2021 CTF"
author: GoProSlowYo
date: "2021-09-10"
subject: "mic Writeup"
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

# mic

Writeup by: [GoProSlowYo](https://github.com/GoProSlowYo)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/mic/)

----

```text
My Epson InkJet printer is mysteriously printing blank pages. Is it trying to tell me something?
```

## Initial Research

The text seems to reference the printer "telling" us something. This 'something' is [`MIC`](https://en.wikipedia.org/wiki/Machine_Identification_Code)'s in the printer page.

> Tiny dots are embedded on printouts by modern printers. Markings like these were used to trace [NSA documents leaked to The Intercept by Reality Winner](http://www.bbc.com/future/story/20170607-why-printers-add-secret-tracking-dots)

![Yellow Dots: tiny yellow dots on the print-out representing the hidden code of an HP Color LaserJet 3700.](https://upload.wikimedia.org/wikipedia/commons/8/8e/HP_Color_Laserjet_3700_schutz_g.jpg)

## Getting the Flag from the Printed Pages

We wrote a quick one liner to dump the flag:

```shell
$ pdftoppm scan.pdf scan -png; for x in {01..34}; do echo -n $(python -c "print(chr($(deda_parse_print /home/kali/ctf/csaw21/mic/scan-$x.png | grep serial | cut -d '-' -f2 | sed 's/^0*//')))"); done
flag{watchoutforthepoisonedcoffee}
```

![Solve Animation](./solve.gif)\

## Victory

Submit the flag and claim the points:

**flag{watchoutforthepoisonedcoffee}**
