import requests
import json

URL  = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/deviceclusters/ftddevicecluster"
USERNAME = "jahangiri"
PASSWORD = "6rRhtbqF"

header = {"X-auth-access-token" : "b0da7dc1-f540-4937-9554-a30b5ee1cc04",
"X-auth-refresh-token" : "57564925-64ad-4808-b754-896e40e31cb1"}

RESPONSE = requests.get(URL,headers=header,verify=False)

DEVICE_LIST = json.dumps(RESPONSE.json(), indent=2)
print(DEVICE_LIST)