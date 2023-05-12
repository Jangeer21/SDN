from genie.testbed import load
import json
import unicon

testbed = load('./ncs540_testbed.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],log_stdout=False,learn_hostname=True)         
        show_xml = iosxr.execute('sh running-config xml')
        print(type(json.loads(show_xml)))
        
        iosxr.disconnect()

    except (unicon.core.errors.ConnectionError):
        print("Device Unavailable")
        continue

   # cfg = iosxr.configure("netconf agent tty")

