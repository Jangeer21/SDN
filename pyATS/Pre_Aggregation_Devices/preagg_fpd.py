from genie.testbed import load
import unicon

testbed = load('./ncs540_testbed.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],
                      log_stdout=False,learn_hostname=True)
        fpd = iosxr.execute('sh hw-module fpd Primary-BIOS')
        print(fpd)
        iosxr.disconnect()

    except unicon.core.errors.ConnectionError:
        print("Device Unavailable")
        continue



