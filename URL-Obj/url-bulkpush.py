"""
This python module was created by Shubham Bharti.
Feel free to send comments/suggestions/improvements.  Either by email: shbharti@cisco.com or more importantly via a pull
request from the github repository: https://github.com/shubhambharti89/FMCAPI
"""


import requests
import json
import time
from requests.auth import HTTPBasicAuth
from getpass import getpass
import customfunctions as cf

addr = input("Enter IP Address of the FMC: ")
username = input ("Enter Username: ")
password = getpass("Enter Password: ")

csvFilePath = input("Please enter the CSV Filepath (For eg. : path/to/file/objects.csv) : ")

api_uri = "/api/fmc_platform/v1/auth/generatetoken"

url = "https://" + addr + api_uri
response = requests.post(url, verify=False, auth=HTTPBasicAuth(username, password))

accesstoken = response.headers["X-auth-access-token"]
refreshtoken = response.headers["X-auth-refresh-token"]
DOMAIN_UUID = response.headers["DOMAIN_UUID"]


urls = cf.csvtojson(csvFilePath)

urls_payload = json.dumps(urls)

urls_api_uri = "/api/fmc_config/v1/domain/" + DOMAIN_UUID + "/object/urls?bulk=true"


urls_url = "https://" + addr + urls_api_uri

headers = {
  'Content-Type': 'application/json',
  'x-auth-access-token': accesstoken
}

if urls != []:
    response = requests.request("POST", urls_url, headers=headers, data = urls_payload, verify = False)

    if response.status_code == 201 or response.status_code == 202:
        print("URL Objects successfully pushed")

    else:
        print("URL Object creation failed - Please check the log files for more detail")

    logfile = "log_"+ str(time.perf_counter_ns()) + ".txt"

    log = open(logfile,"w+")
    log.write(response.text)
    log.close


else :
    print("Please Validate that the CSV file provided is correct or at correct location")
