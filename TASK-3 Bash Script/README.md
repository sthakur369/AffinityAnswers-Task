## Bash Script

**Task:** Extract the Scheme Name and Asset Value fields from given [link](https://www.amfiindia.com/spages/NAVAll.txt) and saves them in a .tsv file

**Files:**
> script.sh: Script file

> amfiindia.tsv: Extrated file

**Run command:**
``` bash script.sh ``` 

```
#!/bin/bash

url="https://www.amfiindia.com/spages/NAVAll.txt"

# awk: to extract
curl "$url" | awk -F ';' '{print $4 "\t" $5}' > amfiindia.tsv

# remove empty lines and save to temp file
awk 'NF > 0' scheme_asset_values.tsv > temp.tsv

# rename it to orignal file name
mv temp.tsv amfiindia.tsv

echo "Done"
```