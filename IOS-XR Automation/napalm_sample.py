from napalm import get_network_driver

driver = get_network_driver('iosxr')

device = driver('10.64.40.55','admin','admin1234')

device.open()

print(device.get_interfaces())
print('')
print(device.get_interfaces_counters())
print('')
print(device.get_users)

device.close()
