from netmiko import ConnectHandler
from netmiko import (NetMikoAuthenticationException, NetMikoTimeoutException)

ip = input("Enter IP address: ")

device = {'device_type':'cisco_xr', 'ip' : ip, 'username' : 'jahangir', 'password':'Teconfio@22'}

#Storing all commands in a variable
command_file = open("Cisco IOS-XR/command_content.txt", "r")

#Reading content of commands file and storing it in a new variable
commands = command_file.read()

#Adding commands into list by splitting newlines
command_list = commands.split("\n")
command_file.close()

ssh =  ConnectHandler(**device)

for command in command_list:
    print("Sending command -> " + command)

    try:
        output = ssh.send_command(command, read_timeout=50)
        with open("tac_commands.txt","a") as file:
            file.write(command + ": \n" + output + "\n\n")

    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        print("Unknown command")
        continue

