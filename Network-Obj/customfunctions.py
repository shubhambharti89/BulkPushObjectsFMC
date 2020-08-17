"""
This python module was created by Shubham Bharti.
Feel free to send comments/suggestions/improvements.  Either by email: shbharti@cisco.com or more importantly via a pull
request from the github repository: https://github.com/shubhambharti89/FMCAPI
"""

import csv

# Function to convert a CSV to JSON
def csvtojson(csvFilePath):

    host = []
    ranges = []
    network = []

    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            if rows['type'] == "Host":
                host.append(rows)
            if rows['type'] == "Range":
                ranges.append(rows)
            if rows['type'] == "Network":
                network.append(rows)

    return host,ranges,network
