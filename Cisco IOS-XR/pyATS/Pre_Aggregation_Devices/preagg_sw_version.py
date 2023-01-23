from genie.testbed import load
import unicon

testbed = load('./PreAgg.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],
                      log_stdout=False,learn_hostname=True)
        xr_version = iosxr.parse('show version')
        print(device + " software version: " + xr_version["software_version"])
       # print(device + " platform: " + xr_version["device_family"])
        iosxr.disconnect()

    except unicon.core.errors.ConnectionError:
        print("Device Unavailable")
        continue



