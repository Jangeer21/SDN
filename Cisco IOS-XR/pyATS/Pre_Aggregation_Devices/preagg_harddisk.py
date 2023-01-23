from genie.testbed import load
import unicon
from tqdm import tqdm

testbed = load('./PreAgg.yaml')

pbar = tqdm(total = len(testbed.devices))

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],log_stdout=False,learn_hostname=True)         
        hdd = iosxr.parse('dir harddisk:')
        if hdd["dir"]["files"]["ncs540l-7.5.2.CSCwd50606.tar"]:
            print("SMU is in hard disk")
        else:
            print("No SMU detected")
        iosxr.disconnect()

    except (unicon.core.errors.ConnectionError, KeyError):
        print("Device Unavailable")
        continue
    pbar.update(1)

pbar.close()
   # cfg = iosxr.configure("netconf agent tty")

