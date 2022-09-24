from netmiko import ConnectHandler

# ip_list = pyexcel.get_records('//10.220.1.202/AzerConnect_LLC/Corporate Folder/CTO/Transport and Backbone Network Department/OTN Modernization/Implementation documentation of OTN-MB/OTN-MB_numbering_scheme_v2.4.4.xlsx')

with open('./Documents/Azerconnect/IOS-XR Automation/ip_list.txt') as f:
    ip_list = f.readlines()

for ip in ip_list:
    cisco_ncs_540 = {'device_type': 'cisco_xr','ip': ip,'username': 'admin','password': 'admin1234'}
    net_connect = ConnectHandler(**cisco_ncs_540)
    print(" /n Configuring: " + ip)
    net_connect.send_config_from_file(config_file='./Documents/Azerconnect/IOS-XR Automation/prefix_set.txt')
    net_connect.send_config_set('commit')
    output = net_connect.send_command('show run prefix-set PR-ST-L2-Loopbacks-CORE')
    print(output)
