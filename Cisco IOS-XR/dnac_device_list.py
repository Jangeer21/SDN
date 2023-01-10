#Creating a network device list with a Python function
from os import device_encoding
import re
import requests
from requests.auth import HTTPBasicAuth


DNAC_IP = "sandboxdnac.cisco.com"
DNAC_PORT = 443
DNAC_USER = "devnetuser"
DNAC_PASS = "Cisco123!"

def get_device_list():
    TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY2NDk3MTAwOCwiaWF0IjoxNjY0OTY3NDA4LCJqdGkiOiIwM2JlN2VhOS00ZDE4LTQzNGYtODc3OC1jNDZhNzkyYjI2Y2QiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.TOaVSqPNfZNu8-_Y1KbTYTN3anLMh_JAcGTc5buRz2mskqy5MFoXI34q36aPTvZVRItw-y-d7RyAvtBlc8ag1jlkrMHo4x-pmrS3kKpBGz0NfRV2VHXPUGrUdJsGCrzXAGo1VSVQwN35fuuUzi7IdxFasDLmN6mf1yUun1PP2SpmX-ib_IohpmficjxwZhFfoIKBYXkSRqKY4R5Ga3JnuWik7Ab-BYiXYlfyeAVGYArQ4A4FP5fbeAbQck5RPVswDCNoJsUGa3nTkX8a51Fh4--YHntjL6PGqBiPhflymDnfXpoPMMNKNXapU-lKqAA9rtHsZ7llmliPvaVjiiYxBQ"
    URL = "https://sandboxdnac.cisco.com/api/v1/network-device"
    HEADER = {'x-auth-token':TOKEN, 'content-type' : 'application/json'}
    RESPONSE = requests.get(URL,headers=HEADER,verify=False)
    device_list = RESPONSE.json()
    print_device_list(device_list)

def print_device_list(device_json):
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))


    
