from genie.testbed import load
import unicon

testbed = load('./PreAgg.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],log_stdout=False,learn_hostname=True)         
        show_inventory = iosxr.parse('show inventory')
        print("Serial number: " + show_inventory["module_name"]["Rack 0"]["sn"])
        iosxr.disconnect()

    except unicon.core.errors.ConnectionError:
        print("Device Unavailable")
        continue

   # cfg = iosxr.configure("netconf agent tty")

