from genie.testbed import load
import unicon

testbed = load('./PreAgg.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],
                      log_stdout=False,learn_hostname=True)
        mgmt = iosxr.parse('show interfaces mgmtEth 0/RP0/CPU0/0')
        print(mgmt['MgmtEth0/RP0/CPU0/0']['ipv4'])
       # iosxr.configure('''
     #                   interface mgmtEth 0/RP0/CPU0/0
     #                    no ip address
     #                  ''')

        iosxr.disconnect()

    except (unicon.core.errors.ConnectionError,KeyError):
        print("Device Unavailable")
        continue



