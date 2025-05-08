#!/bin/bash

# Input and output file names
input_file=$1
output_file=$2

# Temporary file to store unique lines
temp_file=$(mktemp)

# Iterate through the file and remove duplicates based on the first three columns (State, City, Suburb)
awk -F, '!seen[$1,$2,$3]++' "$input_file" > "$temp_file"

# Copy the result to the output file
mv "$temp_file" "$output_file"

echo "Duplicate rows removed and saved to $output_file."

