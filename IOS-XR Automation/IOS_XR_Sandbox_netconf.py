from ncclient import manager

IOS_XR_HOST = "sandbox-iosxr-1.cisco.com"
NETCONF_PORT = "830"
USERNAME = "admin"
PASSWORD = "C1sco12345"

def get_capabilities():
    with manager.connect(
        host = IOS_XR_HOST,
        port = NETCONF_PORT,
        username = USERNAME,
        password = PASSWORD,
        hostkey_verify = False) as device:

        print('\n***NETCONF Capabilities for device {}***\n'.format(IOS_XR_HOST))
        for capability in device.server_capabilities:
            print(capability)

if __name__ == '__main__':
    get_capabilities()