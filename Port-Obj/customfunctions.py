"""
This python module was created by Shubham Bharti.
Feel free to send comments/suggestions/improvements.  Either by email: shbharti@cisco.com or more importantly via a pull
request from the github repository: https://wwwin-github.cisco.com/shbharti/FMCAPI
"""

import csv

# Function to convert a CSV to JSON
def csvtojson(csvFilePath):

    port = []
    icmpv4 = []
    icmpv6 = []



    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            if rows['type'] == "ProtocolPortObject":
                port.append(rows)
            if rows['type'] == "ICMPV4Object":
                icmpv4.append(rows)
            if rows['type'] == "ICMPV6Object":
                icmpv6.append(rows)

    # Delete the Key:Value pair of ICMP Type and Code for TCP/UDP Protocol Objects
    port_new = [{k: v for k, v in d.items() if k != "code" and k != "icmpType"} for d in port]

    # Delete the Key:Value pair of Protocol and Port for ICMP Objects
    icmpv4_new = [{k: v for k, v in d.items() if k != "protocol" and k != "port"} for d in icmpv4]

    # Delete the Key:Value pair of Protocol and Port for ICMP Objects
    icmpv6_new = [{k: v for k, v in d.items() if k != "protocol" and k != "port"} for d in icmpv6]


    return port_new, icmpv4_new, icmpv6_new