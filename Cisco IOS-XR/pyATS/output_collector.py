from genie.testbed import load
import unicon

#Storing all commands in a variable
command_file = open("./command_content.txt", "r")

#Reading content of commads file and storing it in a new variable
commands = command_file.read()

#Adding commands into list by splitting newlines
command_list = commands.split("\n")
command_file.close()

testbed = load('./Core_Devices/Core.yaml')
iosxr = testbed.devices['AZT-PE-1']
iosxr.connect(init_exec_commands=[],init_config_commands=[],log_stdout=False,learn_hostname=True)
for command in command_list:
    print("Sending command -> " + command)

    try:
        output = iosxr.execute(command, read_timeout=90)
        with open("tac_commands.txt","a") as file:
            file.write(command + ": \n" + output + "\n\n")

    except unicon.core.errors.ConnectionError:
        print("Unknown command")
        continue
    iosxr.disconnect()
