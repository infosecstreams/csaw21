---
title: "Contact Us"
subtitle: "CSAW 2021 CTF"
author: OreoByte
date: "2021-09-10"
subject: "Contact Us Writeup"
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

# Contact Us

Writeup by: [OreoByte](https://github.com/OreoByte)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/contact-us/)

---

```text
Veronica sent a message to her client via their website's Contact Us page. Can you find the message?

Author: moat, Pacific Northwest National Laboratory
```

## Using Wireshark Decrypt The SSL Traffic

Using the given files `sslkeyfile.txt` and `ContactUs.pcap` we can start to decrypt the pcap.

Navigate through `Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename`, click browse and select the `sslkeyfile.txt` file.

![Decrypt TLS in Wireshark](./decrypt.png)\

Find the decrypted flag in the packet capture.

![Search for the Flag](./search.png)\

---

## Using Tshark

You can do the same thing but with `tshark`:

1. Decrypt Pcap into a new file
    * `tshark -r ContactUs.pcap -V -x -o tls.keylog_file:key.log  > results`

1. grep to win for the flag
    * `grep 'flag{' results`

![Tshark](./tshark.png)\

---

## Victory

Submit the flag and claim the points:

`flag{m@r$hm3ll0w$}`
