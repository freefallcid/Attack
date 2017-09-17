#!/bin/sh

adb forward tcp:4352 tcp:4352
gpsd -N -n -D5 tcp://localhost:4352
