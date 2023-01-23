#!/usr/bin/python3
'''
This script possesses multiple API methods to interact with Cisco DNA center platform
'''
import requests
from pathlib import Path
import json
import base64
from pprint import pprint

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

#Loading necessary options to access target device
optionFile = Path(__file__).parent / './options.json'
with open(optionFile, "rb") as opt:
    options = json.load(opt)['DNA']
    HOSTNAME = options['address']
    PORT = options['port']
    USERNAME = options['username']
    PASSWORD = options['password']

#Base64 encoding of credentials
credentials = USERNAME + ':' + PASSWORD
credentials_string_bytes = credentials.encode("ascii")
base64_bytes = base64.b64encode(credentials_string_bytes)
encoded_credentials = base64_bytes.decode("ascii")

base_url = f"https://{HOSTNAME}:{PORT}"

class DNA():

    def __init__(self):
        with requests.Session() as self.s:
            self.token = self.get_Token()

    def get_Token(self):
        #TOKEN RETRIEVAL
        endpoint = "/dna/system/api/v1/auth/token"
        auth_url = base_url + endpoint
        headers = {"Authorization" : "Basic " + encoded_credentials}
        print("\n *** RETRIEVING AUTHENTICATION TOKEN *** \n")
        RESPONSE = self.s.post(auth_url, headers = headers, verify=False)
        if RESPONSE.status_code == 200:
            print("$$$ TOKEN SUCCESSFULLY RETRIEVED $$$")
            return RESPONSE.json()['Token']
        else:
            print("AUTHENTICATION FAILED! \n")
            print(RESPONSE.text)

    def get_DeviceList(self):
        #DEVICE LIST RETRIEVAL
        endpoint = "/dna/intent/api/v1/network-device"
        device_list_url = base_url + endpoint
        headers = {"X-Auth-Token" : self.token}
        print("*** GETTING LIST OF DEVICES *** \n")
        RESPONSE = self.s.get(device_list_url, headers=headers, verify=False)
        if RESPONSE.status_code == 200:
            print("*** DEVICE LIST SUCCESSFULLY RETRIEVED *** \n")
            return RESPONSE.json()['response']
        else:
            print("FAILED TO GET DEVICE LIST! \n")
            print(RESPONSE.text)
    
    def get_DeviceID(self):
        #DEVICE ID RETRIEVAL BY ID
        device_list = self.get_DeviceList()
        for device in device_list:
            print(" GETTING ID FROM --> " + device['hostname'])
            return device['id']

        
    
if __name__ == "__main__":
    dev = DNA().get_DeviceID()
    pprint(dev, indent=2)


