#!/usr/bin/env python3
"""
Before running script, enable XML API on IOS-XR devices by issuing following commands on configuration mode:
xml agent tty
xml agent tty iteration off
"""

from napalm import get_network_driver
import json
from pprint import pprint

driver = get_network_driver('iosxr')

device = driver('10.200.203.4','admin','admin1234')

device.open()

output = device.get_lldp_neighbors()
print(type(output))
pprint(output)

device.close()


