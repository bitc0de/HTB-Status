#!/bin/bash
var=$(curl -L "https://www.hackthebox.eu/badge/306151" -A "Mozilla/5.0 (compatible;  MSIE 7.01; Windows NT 5.0)")
var2=$(echo "$var" | cut -d '"' -f 2)
var3=$(echo "$var2" | base64 -d)
echo "$var3" > status.txt


