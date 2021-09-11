---
title: "checker"
subtitle: "CSAW 2021 CTF"
author: GoProSlowYo
date: "2021-09-10"
subject: "checker Writeup"
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

# checker

Writeup by: [GoProSlowYo](https://github.com/GoProSlowYo) solved by [Perryman](https://github.com/ghost)

Team: [OnlyFeet](https://ctftime.org/team/144644)

Writeup URL: [GitHub](https://infosecstreams.github.io/csaw21/checker/)

----

```text
What's up with all the zeros and ones? Where are my letters and numbers? (This is a reversing challenge.)
```

----

## Initial Research

This one is extremely straightforward and they literally tell us: `(This is a reversing challenge.)`.

For this challenge you can work backwards through the provided python code and function calls to end up with the flag ultimately.

## Decode then `encode`

The main function calls an `encode` function on the `flag`:

`encoded = encode(flag)`.

If we look at the encode function we see it's setting `d = 24` then it's calling `x = up(input)`, `x = right(x,d)`, `x = down(x)`, `x = left(x,d)` and then returns `x`.

```python
def encode(plain):
    d = 24
    x = up(plain)
    x = right(x,d)
    x = down(x)
    x = left(x,d)
    return x
```

We need to take the encoded string and run backwards through main and each function.

----

## Victory

Submit the flag and claim the points:

**flag{r3vers!nG_w@rm_Up}**
