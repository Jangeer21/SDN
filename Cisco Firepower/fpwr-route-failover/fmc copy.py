import requests
import urllib3
from pprint import pprint

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com/api/fmc_config/latest/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords/a54ab61c-e0d7-11ec-9b30-a15f66449288/routing/virtualrouters"

payload={}
headers = {
  'X-auth-access-token': 'af1363f2-5abb-48e3-961a-8a8604abf533',
  'X-auth-refresh-token': '1829b79a-03ca-43a9-bd19-abf1f636c0a8'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

pprint(response.text)
