from genie.testbed import load
import unicon
from pprint import pprint

testbed = load('./PreAgg.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],log_stdout=False,learn_hostname=True)         
        rpm = iosxr.execute('show install active summary | inc CSCwd50606')
        print(rpm)
        iosxr.disconnect()

    except unicon.core.errors.ConnectionError:
        print("Device Unavailable")
        continue

   # cfg = iosxr.configure("netconf agent tty")

