import requests
import urllib3
import json

#Defining Variables.
username = "admin"
password = "!v3G@!4@Y"
def get_token():
    # url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    # payload = {
    #     "aaaUser" : {
    #         "attributes" : {
    #             "name" : "unamea",
    #             "pwd" : "pwd"
    #             }
    #         }
    #     }
    # headers = {
    #     "content-type" : "application/json"
    # }
    requests.packages.urllib3.disable_warnings()
    r = requests.post('https://sandboxapicdc.cisco.com/api/aaaLogin.json', json={"aaaUser": {"attributes": {"name": username, "pwd": password}}}, verify=False)
    response = r.json()


    # response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()
    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    return token
    # print(token)

get_token()