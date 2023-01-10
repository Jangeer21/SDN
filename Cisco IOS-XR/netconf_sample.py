from operator import contains
from ncclient import manager

IOS_XR_HOST = "10.64.40.52"
NETCONF_PORT = "830"
USERNAME = "admin"
PASSWORD = "admin1234"

with manager.connect(
    host = IOS_XR_HOST,
    port = NETCONF_PORT,
    username = USERNAME,
    password = PASSWORD,
    hostkey_verify = False) as device:

    print('\n***NETCONF Capabilities for device {}***\n'.format(IOS_XR_HOST))
    for capability in device.server_capabilities:
      if capability == "openconfig":
        print(capability)


        