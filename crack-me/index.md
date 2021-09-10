---
title: "CHALLENGE NAME"
subtitle: "CSAW 2021 CTF"
author: USERNAME
date: "2021-09-10"
subject: "CHALLENGE NAME Writeup"
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

# Crack Me

Writeup by: [OreoByte](https://github.com/OreoByte)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/crack-me/)

----

```text
Can you crack this? Your hash: A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c. Your salt: the encryption method of the hash. (So if the hash is of the word example, you would submit flag{example} to score points.)
```

Here's the [Hash](./hash)

## What Hash is This?

`hashid -m A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c`
OR
[Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/)

## Cracking a Salted Hash with Hashcat

```bash
# Command Usage: hashcat -m 1420 <hash>:<salt> /usr/share/wordlists/rockyou.txt
$ hashcat -m 1420 A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256 /usr/share/wordlists/rockyou.txt
```

```text
$ hashcat -m 1420 A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256 /usr/share/wordlists/rockyou.txt  --show
a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256:cathouse
```

## Victory

Submit the flag and claim the points:

**`flag{cathouse}`**
