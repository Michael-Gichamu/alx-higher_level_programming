#!/bin/bash
# Displays all HTTP methods the server will accept
headers=$(curl -s -I "$1")
allowed_methods=$(echo "$headers" | awk -F ': ' '/^Allow:/ {print $2}')
echo "$allowed_methods"

