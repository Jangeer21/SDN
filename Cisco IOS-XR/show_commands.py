from netmiko import ConnectHandler
from netmiko import (NetMikoAuthenticationException, NetMikoTimeoutException)

ip = input("Enter IP address: ")

device = {'device_type':'cisco_xr', 'ip' : ip, 'username' : 'jahangir', 'password':'Teconfio@22'}

command_list = ["show interface hundredGigE0/6/0/2",
"show interface hundredGigE0/3/0/5",
"show controllers hundredGigE0/6/0/2 all",
"show controllers hundredGigE0/3/0/5 all",
"show controllers optics hundredGigE0/6/0/2",
"show controllers optics hundredGigE0/3/0/5",
"show platform",
"show install active summary",
"show version",
"cfs check",
"show hw-module fpd",
"show alarms",
"show environment all",
"show media",
"show inventory",
"show running",
"show log",
"show logging events buffer bistate-alarms-set",
"show context location all",
"show process blocked location all",
"show memory summary location all",
"show watchdog memory-state location all",
"dir harddisk:/dumper/"]

ssh =  ConnectHandler(**device)

for command in command_list:
    print("Sending command -> " + command)

    try:
        output = ssh.send_command(command, read_timeout=50)
        with open("tac_sfp.txt","a") as file:
            file.write(command + ": \n" + output + "\n\n")

    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        print("Unknown command")
        continue

