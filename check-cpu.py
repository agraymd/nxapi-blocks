import requests
import json
import authenticate_store_token #contains authentication function - mainly testing imports

# Sets token to value of token from authentication post
token = authenticate_store_token.nx_authenticate_get_token('admin', 'cisco!123', '10.122.176.117')

# Checks CPU usage 
url = "https://10.122.176.117/api/node/mo/sys/procsys/sysload.json?query-target=self"

headers = {
  'content-type': 'application/json',
  'Cookie': 'APIC-Cookie=' + token
}

response = requests.get(url, headers=headers, verify=False)

print(response.json())

'''
# Down interface test - Puts E1/1 in down state -- This is only here to test, above is check CPU script
url = "https://10.82.142.106/api/mo/sys/intf.json"
headers = {
  'content-type': 'application/json',
  'Cookie': 'APIC-cookie=' + token
}

payload = {
  "interfaceEntity": {
    "children": [
      {
        "l1PhysIf": {
          "attributes": {
            "id": "eth1/1",
            "adminSt": "down",
            "userCfgdFlags" : "admin_layer"
          }
        }
      }
    ]
  }
}

#had to change this request to 'json=payload' to get it to work
response = requests.post(url, headers=headers, verify=False, json=payload) 

print(response.json())
'''
