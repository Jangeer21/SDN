from urllib import request
import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()


DNA_CENTER = {
    "host" : "sandboxdnac.cisco.com",
    "port":"443",
    "username":"devnetuser",
    "password":"Cisco123!"
}

def get_auth_token():
    endpoint = '/dna/system/api/v1/auth/token'
    url = 'https://'+ DNA_CENTER["host"]+endpoint

    RESPONSE = requests.post(url, auth=HTTPBasicAuth(DNA_CENTER["username"],DNA_CENTER["password"]),verify=False)
    token = RESPONSE.json()['Token']

    print("Token is -> ".format(token))

    return token

if __name__ == "__main__":
    get_auth_token()

