#!/bin/bash

# URL of the file
url="https://www.amfiindia.com/spages/NAVAll.txt"

# Fetch the content of the file using curl and filter using awk
curl "$url" | awk -F ';' '{print $4 "\t" $5}' > scheme_asset_values.tsv

# Clean up the output file using awk to remove extra whitespace
awk 'NF > 0' scheme_asset_values.tsv > temp.tsv
mv temp.tsv scheme_asset_values.tsv



echo "Extraction and saving completed."
