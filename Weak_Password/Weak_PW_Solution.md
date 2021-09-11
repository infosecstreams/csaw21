| Author | Challenge From | Type |
| ------ | -------------- | ---- |
| OreoByte |  Misc | Curstom Wordlist & Password Cracking |

# Create the dates part of the wordlist with a `python3` script

```python
#!/usr/bin/python3
# month/day/year
from datetime import date, timedelta
sdate = date(1900,1,1)
edate = date(2022,1,1)
delta = edate -sdate

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    #print(day.month,day.day,day.year)
    print(day.year,day.month,day.day)
```

# remove the spacebar character that is created from the python script

`sed -e 's/ //g' dates > mdy`

# Modify the dates file `mdy` with `name` and `special characters`

```bash
#!/bin/bash
sed -e 's/^/Aaron/' mdy > cap_user_date
sed -e 's/^/aaron/' mdy >> cap_user_date
sed -e 's/$/aaron/' mdy >> cap_user_date
sed -e 's/$/Aaron/' mdy >> cap_user_date
sed -e 's/^/Aaron /' mdy >> cap_user_date
sed -e 's/$/Aaron /' mdy >> cap_user_date

# special chars
cp cap_user_date final.lst
sed -e 's/$/!/' cap_user_date >> final.lst
sed -e 's/$/@/' cap_user_date >> final.lst
sed -e 's/$/#/' cap_user_date >> final.lst
sed -e 's/$/$/' cap_user_date >> final.lst
sed -e 's/$/%/' cap_user_date >> final.lst
sed -e 's/$/^/' cap_user_date >> final.lst
sed -e 's/$/&/' cap_user_date >> final.lst
sed -e 's/$/*/' cap_user_date >> final.lst
for i in {0..9}; do sed -e 's/$/$i/' cap_user_date >> final.lst; done
```

# ID hash and crack with hashcat with custom wordlist
`https://www.tunnelsup.com/hash-analyzer/`
OR
`hashid 7f4986da7d7b52fa81f98278e6ec9dcb`

## Cracking Hash With Hascat with a rule file `OneRuleToRuleThemAll.rule`

`hashcat -D 2,3 -m 0 7f4986da7d7b52fa81f98278e6ec9dcb final.lst -r ~/tools/Optimised-hashcat-Rule/OneRuleToRuleThemAll.rule`
`hashcat -D 2,3 -m 0 7f4986da7d7b52fa81f98278e6ec9dcb final.lst -r ~/tools/Optimised-hashcat-Rule/OneRuleToRuleThemAll.rule --show`
`7f4986da7d7b52fa81f98278e6ec9dcb:Aaron19800321`

# final flag `flag{Aaron19800321}`