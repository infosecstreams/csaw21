# Crack Me Solution

```
Can you crack this? Your hash: A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c. Your salt: the encryption method of the hash. (So if the hash is of the word example, you would submit flag{example} to score points.)
```

## ID the hash type

`hashid A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c`
OR
`https://www.tunnelsup.com/hash-analyzer/`

## cracking the salted hash with hashcat and the salt in the right location

```
hashcat -D 2,3 -m 1420 <hash>:<salt> /usr/share/wordlists/rockyou.txt
hashcat -D 2,3 -m 1420 A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256 /usr/share/wordlists/rockyou.txt
```

```
└─$ hashcat -D 2,3 -m 1420 A60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256 /usr/share/wordlists/rockyou.txt  --show
a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256:cathouse
```

## final flag `flag{cathouse}`
