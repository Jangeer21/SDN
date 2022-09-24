import requests

URL = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

RESPONSE = requests.post(URL,USERNAME,PASSWORD)