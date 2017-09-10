#!/bin/sh
# Flush table 'filter' and 'nat'

iptables -F FORWARD
iptables -F INPUT
iptables -F OUTPUT
iptables -t nat -F INPUT
iptables -t nat -F OUTPUT
iptables -t nat -F POSTROUTING
iptables -t nat -F PREROUTING

