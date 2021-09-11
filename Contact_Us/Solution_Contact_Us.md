| Author | Challenge From | Challenge Type |
| OreoByte | forensics | Packet Capture Analysis |
 
# Challenge

`Veronica sent a message to her client via their website's Contact Us page. Can you find the message?`

# given files

`sslkeyfile.txt` and `ContactUs.pcap`

# Using Wireshark Decrypt The SSL Traffic

## Change the key so `wireshark can read it`

`mv sslkeyfile.txt key.log`

## Add SSL Key file to decrypt TLS traffic

`edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename (Browse == key.log)`

## find the decrypted flag

# Doing the Same thing but with `tshark` Much Easier

1. Decrypt Pcap into a new file
    tshark -r ContactUs.pcap -V -x -o tls.keylog_file:key.log  > results
2. grep to win for the flag
    grep 'flag{' results

# Final Flag `flag{m@r$hm3ll0w$}`
