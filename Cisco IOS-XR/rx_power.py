from netmiko import ConnectHandler
import json
from pprint import pprint

ip = input("Enter loopback IP address: ")
intf = input("Enter interface: ")

cisco_ncs_540 = {'device_type': 'cisco_xr','ip': ip,'username': 'admin','password': 'admin1234'}
    
net_connect = ConnectHandler(**cisco_ncs_540)

print("Connecting to -> " + ip)
output1 = net_connect.send_command(f'sh controllers {intf} phy | include Receive Power')
output2 = net_connect.send_command(f'sh controllers {intf} phy | include Rx')
print(output1 + output2)
