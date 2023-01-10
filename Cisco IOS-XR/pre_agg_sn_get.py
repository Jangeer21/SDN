
from genie.testbed import load

testbed = load('./PreAgg.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    iosxr.connect(init_exec_commands=[],
    init_config_commands=[],
    log_stdout=False,
    learn_hostname=True)

    show_inventory = iosxr.parse('show inventory')
    print("Serial number: " + show_inventory["module_name"]["Rack 0"]["sn"])
   # cfg = iosxr.configure("netconf agent tty")

    iosxr.disconnect()
