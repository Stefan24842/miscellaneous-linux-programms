#!/bin/bash
while true
do
    battery_level=`acpi -b | grep -P -o '[0-9]+(?=%)'`
    if [ $battery_level -le 20 ]; then
       notify-send "Batterie unter 20%!" "Aktuell: ${battery_level}%" -i battery -u critical -t 300
       sleep 900
    fi

    sleep 120 # 300 seconds = 5 minutes
done
