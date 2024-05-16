#!/bin/bash

# Use the systemctl command to check Bluetooth status
if systemctl is-active --quiet bluetooth; then
    echo "Bluetooth is on."
    exit 0
else
    echo "Bluetooth is off."
    exit 1
fi
