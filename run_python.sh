#!/bin/bash

# Run the Bluetooth check script
./bluetooth_check.sh

# If Bluetooth is on (exit status of last command is 0), run the Python script
if [ $? -eq 0 ]; then
    python3 zero.py
else
    echo "Not running the Python script because Bluetooth is off."
fi
