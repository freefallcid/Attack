#!/bin/sh

WLAN=$(echo $1 | awk '{ print $1 }')

if [ ! $# -eq 1 ]
then
  echo "Which wlan interface to use?"
  read WLAN
fi

ifconfig $WLAN down
#macchanger -A $WLAN
iw reg set BO
ifconfig $WLAN up
iwconfig $WLAN channel 13
iwconfig $WLAN txpower 30
iwconfig $WLAN rate 1M
airmon-ng start $WLAN
ifconfig ${WLAN}mon down
macchanger -A ${WLAN}mon
ifconfig ${WLAN}mon up

